---
layout: post
title: Setup automount using systemd
categories: linux, systemd, mount, network, configuration
---

Install cifs, e.g. on Ubuntu:
```bash
sudo apt install cifs-utils
```

Create mount points, e.g.
```bash
sudo mkdir /mnt/iflglw
```

Create automount systemd service file. File name must match the mount point, e.g.:
```bash
sudo systemctl edit --full --force mnt-iflglw.automount
```
with following content:
```ini
[Unit]
Description=Automount IFL Group Share
ConditionPathExists=/mnt/iflglw

[Automount]
Where=/mnt/iflglw
TimeoutIdleSec=0

[Install]
WantedBy=multi-user.target
```

Enable and start the service via
```bash
sudo systemctl enable mnt-iflglw.automount
sudo systemctl start mnt-iflglw.automount
```

Create the mount systemd servive file:
```bash
sudo systemctl edit --full --force mnt-iflglw.mount
```
with content:
```ini
[Unit]
Description=IFL Group Share
After=network-online.target
Wants=network-online.target

[Mount]
What=//vs-grp04.zih.tu-dresden.de/ifl
Where=/mnt/iflglw
Options=credentials=/home/stanley/Documents/keyfiles/tud.creds,uid=1000,gid=1000,iocharset=utf8,file_mode=0644,dir_mode=0755,noperm
Type=cifs
TimeoutSec=30

[Install]
WantedBy=multi-user.target
```

Finally, a credentials file (here: `/home/stanley/Documents/keyfiles/tud.creds`) has to be created with the following content:
```
user=
domain=
pass=
```