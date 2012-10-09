[ -f /is/etc/hostid.is ] && {
  HNAME=$(cat /is/etc/hostid.is)
  export PS1="[\\u@$HNAME \\W]\\$ "
  export PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HNAME}:${PWD/#$HOME/~}"; echo -ne "\007"'
  export IS_HOSTID=$HNAME
}
