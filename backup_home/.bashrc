#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '






# ALIASES

alias ls='ls -1 --color=auto'
alias ll='ls -lah --color=auto'
alias check='bat'
alias clear="printf '\033c'"
cd(){
	builtin cd $@;
	ls -1;


}




sshfsvyda(){
	mkdir -p ~/vyda/
	sshfs -o IdentityFile=~/.ssh/vyda vyda@vyda.mx:/var/www/vyda-project ~/vyda/

}
sshfsinteract(){
	mkdir -p ~/interact/
	sshfs -o IdentityFile=~/.ssh/interact interact@interactspeakingcenter.com:/var/www/new_ia ~/interact/
}


# SERVERS
alias sshvyda='ssh -i ~/.ssh/vyda vyda@vyda.mx'
alias sshinteract='ssh -i ~/.ssh/interact interact@interactspeakingcenter.com'


# Starship startup
eval "$(starship init bash)"
. "$HOME/.cargo/env"
