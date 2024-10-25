---
title: Setting up my Terminal
categories:
  - Blog
tags:
  - linux
  - terminal
  - zsh
  - configuration
---

## Prerequisites

- install the following packages
  - zsh
  - tmux
  - vim
  - git


## Setup

### dotfiles

- clone dotfiles repository: `git clone https://github.com/sfo/.dotfiles.git`
- link the files:
```
ln -s ~/.dotfiles/.gitconfig ~/
ln -s ~/.dotfiles/.tmux.conf ~/
ln -s ~/.dotfiles/.vimrc ~/
ln -s ~/.dotfiles/.condarc ~/
```


### vim

- install vundle package manager:
```
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

- open vim and install plugins:
```
:PluginInstall
```


### zsh

- prefer version >=5.4

#### oh-my-zsh

- install the [oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh) stuff
```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

- clone [my repo](https://github.com/sfo/ohsfozsh.git) into oh my zsh's custom folder
```
rm -rf ~/.oh-my-zsh/custom
git clone --recurse-submodules https://github.com/sfo/ohsfozsh.git ~/.oh-my-zsh/custom
```
- sometimes, an additional submodule upate is necessary:
```
git submodule update --init --recursive
```


- replace `.zshrc` with link to dotfiles repository:
```
ln -sf ~/.dotfiles/.zshrc ~/
```

- run new zsh session or execure `omz reload`

#### dircolors

- list available color schemes:
```
lssolarized
```

- configure color scheme:
```
setupsolarized dircolors.ansi-light
```


### tmux

- install TMUX Plugin Manager:
```
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```

- start a new tmux server and install plugins listed in .tmux.conf via `CTRL-B`+`SHIFT-I`


### htop

- in case you can't see numbers in htop anymore, change the theme to "Broken Gray"
