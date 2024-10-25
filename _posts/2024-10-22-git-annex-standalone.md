---
title: Install most recent git-annex on Ubuntu
categories:
  - Blog
tags:
  - linux
  - git
  - ubuntu
  - configuration
---

# Problem Description

At work, I am managing some Ubuntu server VMs running either 20.04 or 22.04.
Both of which do not ship with the latet git-annex version.
However, on my work PCs I run the latest Ubuntu 24.04 and on my Laptop it's Fedora 40, both providing git-annex version 10 in their repositories.
Therefore, the local git repository is requiring git-annex 10 to work with:

```shell
user@host:~/dev/mwe$ git annex version
git-annex version: 10.20240927-g3d7f94ea398b5e84dab3bc89bc5b37746de1d40c
build flags: Assistant Webapp Pairing Inotify DBus DesktopNotify TorrentParser MagicMime Servant Benchmark Feeds Testsuite S3 WebDAV
dependency versions: aws-0.24.1 bloomfilter-2.0.1.2 crypton-0.33 DAV-1.3.4 feed-1.3.2.1 ghc-9.4.7 http-client-0.7.14 persistent-sqlite-2.13.2.0 torrent-10000.1.3 uuid-1.3.15 yesod-1.6.2.1
key/value backends: SHA256E SHA256 SHA512E SHA512 SHA224E SHA224 SHA384E SHA384 SHA3_256E SHA3_256 SHA3_512E SHA3_512 SHA3_224E SHA3_224 SHA3_384E SHA3_384 SKEIN256E SKEIN256 SKEIN512E SKEIN512 BLAKE2B256E BLAKE2B256 BLAKE2B512E BLAKE2B512 BLAKE2B160E BLAKE2B160 BLAKE2B224E BLAKE2B224 BLAKE2B384E BLAKE2B384 BLAKE2BP512E BLAKE2BP512 BLAKE2S256E BLAKE2S256 BLAKE2S160E BLAKE2S160 BLAKE2S224E BLAKE2S224 BLAKE2SP256E BLAKE2SP256 BLAKE2SP224E BLAKE2SP224 SHA1E SHA1 MD5E MD5 WORM URL GITBUNDLE GITMANIFEST VURL X*
remote types: git gcrypt p2p S3 bup directory rsync web bittorrent webdav adb tahoe glacier ddar git-lfs httpalso borg rclone hook external
operating system: linux x86_64
supported repository versions: 8 9 10
upgrade supported from repository versions: 0 1 2 3 4 5 6 7 8 9 10
local repository version: 10
```

To meet this requirement on my Ubuntu VMs, I could install the latest git-annex within a conda environment.
This however requires to either have this specific environment activated all the time or to install the package within all environments, which is quite cumbersome.

However, there is another way of installing a more recent package on the system than what is provided in the official Ubuntu repos.
I just found that [NeuroDebian](https://neuro.debian.net) is providing -- besides some other packages -- a specific standalone version of git-annex also for Ubuntu 24.04.

Here, I will now show how I use this repository to install the more recent version of git-annex on my system.

# Setup A Third-Party Package Repository

Adding the NeuroDebian repository to your system is actually quite easy.
First, we have to add it to the apt package management system by placing a specific file under `/etc/apt/sources.list.d/`.
Luckily, the repository's maintainers provide such a file, which can even be [configured online](https://neuro.debian.net/install_pkg.html) to match your system and a specific download server.

```shell
user@host:~$ wget -O- http://neuro.debian.net/lists/noble.de-m.full | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list
```

Next, we need to add the signing key, so apt can verify the integrity of downloaded packages:

```shell
user@host:~$ sudo apt-key adv --recv-keys --keyserver hkps://keyserver.ubuntu.com 0xA5D32F012649A5A9
```

Finally, a classic `sudo apt update` will fetch all the contents from the new repository.
Since NeuroDebian provides lot of packages, you may encounter a message that there are updates available.
Therefore, we need to _pin_ those packages that we do not want to be installed from NeuroDebian.

# Pinning

To change the priority for all packages from the NeuroDebian to be lower than that of the Ubuntu's default repositories (which is 500), we create a file under `/etc/apt/preferences.d/` with the following content:

```shell
user@host:~$ cat /etc/apt/preferences.d/neurodebian
Package: *
Pin: release o=NeuroDebian
Pin-Priority: -1
```

A negative value for `Pin-Priority` essentially disables the repository for the packages mentioned (which is all packages in this case, due to the wildcard).

To be able to still install that one package (`git-annex-standalone`), we create another file like that but this time with a positive priority value:

``` shell
user@host:~$ cat /etc/apt/preferences.d/neurodebian
Package: git-annex-standalone
Pin: release o=NeuroDebian
Pin-Priority: 500
```

Now we can install `git-annex-standalone` without worrying about pulling in other packages from a source other than the Ubuntu repositories (or others, if you configure additional third-party repositories).
