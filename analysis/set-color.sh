#!/bin/bash
colorEcho() {
    local color=$1
        shift
        if [ -c /dev/stdout ] ; then
# if stdout is console, turn on color output.
            echo -ne "\033[1;${color}m"
                echo -n "$@"
                echo -e "\033[0m"
        else
            echo "$@"
                fi
}
redEcho() {
    colorEcho 31 "$@"
}
greenEcho() {
    colorEcho 32 "$@"
}
redEcho $1
greenEcho $1

