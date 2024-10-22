---
layout: post
title: Set default editor system-wide
categories: linux, editor, configuration
---

Set vim as default editor for everything and everyone (instead of setting EDITOR, SYSTEMD_EDITOR, etc. separately for users and make sure to preserve them when using sudo):
```
sudo update-alternatives --config editor
```


For preserving environment variables when using `sudo` one can use the `-E` command switch.
Alternatively, the variable to be preserved can be added to the `/etc/sudoers` file using `sudo visudo`, e.g.:
```
Defaults env_keep += "SYSTEMD_EDITOR"
```