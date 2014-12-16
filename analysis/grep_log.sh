#!/bin/bash
colorEcho() {
    local color=$1
        shift
        if [ -c /dev/stdout ] ; then
# if stdout is console, turn on color output.
            echo  "\033[1;${color}m"
            echo -n "$@"
            echo  "\033[0m"
        else
            echo "$@"
                fi
}
redEcho() {
    colorEcho 31 "$@"
}

prefixFile='site_feifei-'$1'_'
dir='/mnt/mfs/log/tiger/site_feifei'
filterText=$2
find ${dir} -iname $prefixFile'*' | while read jarFile
do
    redEcho "analysis file" ${jarFile}
    #egrep "$filterText"  ${jarFile}
done


