#!/bin/bash

if [[ $EUID > 0 ]]
then
    echo "Please run as root"
    exit
fi

wget -O- http://neuro.debian.net/lists/noble.de-m.full > /etc/apt/sources.list.d/neurodebian.sources.list
apt-key adv --recv-keys --keyserver hkps://keyserver.ubuntu.com 0xA5D32F012649A5A9

cat <<EOF > /etc/apt/preferences.d/neurodebian
Package: *
Pin: release o=NeuroDebian
Pin-Priority: -1
EOF

cat <<EOF > /etc/apt/preferences.d/git-annex
Package: git-annex-standalone
Pin: release o=NeuroDebian
Pin-Priority: 500
EOF
