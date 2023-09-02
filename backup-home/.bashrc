#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '






# ALIASES

alias cat=bat
alias ls='ls -l'
alias ll='ls -la'

# Starship startup
eval "$(starship init bash)"
