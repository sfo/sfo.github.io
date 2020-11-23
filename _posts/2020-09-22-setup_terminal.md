---
layout: post
title: Setting up my Terminal
categories: linux, terminal, zsh, configuration
---

## Introduction

- install the following packages
  - zsh
  - tmux
  - vim
  - git

## Setup

### dotfiles

- clone dotfiles repository: `git clone git@github.com:sfo/.dotfiles.git ~/.dotfiles`
- link the files:
```
ln -s ~/.dotfiles/.gitconfig ~/
ln -s ~/.dotfiles/.tmux.conf ~/
ln -s ~/.dotfiles/.vimrc ~/
```

### zsh

- prefer version >=5.4

### oh-my-zsh

- install the [oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh) stuff
- clone [my repo](git@github.com:sfo/ohsfozsh.git) into oh my zsh's custom folder
```
rm -rf ~/.oh-my-zsh/custom
git clone git@github.com:sfo/ohsfozsh.git ~/.oh-my-zsh/custom
```

### dircolors

- for Gnome Terminal, install [this](https://github.com/aruhier/gnome-terminal-colors-solarized)
```
git clone git@github.com:aruhier/gnome-terminal-colors-solarized.git ~/.solarized
cd ~/.solarized
./install.sh
```
- for XFCE4 Terminal, install [this](https://github.com/seebi/dircolors-solarized)
```
git clone git@github.com:seebi/dircolors-solarized.git ~/.dircolors
echo 'eval `dircolors ~/.dircolors/dircolors.256dark`' >> ~/.zshrc
```

### vim

- install vundle package manager:
```
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
``` 
