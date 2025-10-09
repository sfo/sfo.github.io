#!/bin/bash

PREFIX="/usr"
SHAREDIR="share"
ZSH_COMPLETIONS_PATH="${PREFIX}/${SHAREDIR}/zsh/site-functions"

install -d ${ZSH_COMPLETIONS_PATH}
git-annex --zsh-completion-script git-annex 2>/dev/null > ${ZSH_COMPLETIONS_PATH}/_git-annex

