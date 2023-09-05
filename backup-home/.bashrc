#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '


cd(){
	builtin cd $@;
	ls -1;


}



# ALIASES

alias ls='ls -1 --color=auto'
alias ll='ls -lh --color=auto'
alias check='bat'





# SERVERS
alias sshvyda='ssh -i ~/.ssh/vyda vyda@vyda.mx'
alias sshfsvyda='sshfs -o IdentityFile=~/.ssh/vyda vyda@vyda.mx:/var/www/vyda-project ~/server/'
alias sshinteract='ssh -i ~/.ssh/interact interact@interactspeakingcenter.com'
alias sshfsinteract='sshfs -o IdentityFile=~/.ssh/interact interact@interactspeakingcenter.com:/var/www/vyda-project ~/server/'


# Starship startup
eval "$(starship init bash)"
