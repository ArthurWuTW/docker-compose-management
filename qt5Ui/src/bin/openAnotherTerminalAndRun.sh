#!/bin/bash

MACHINE=$1
LOGIN_USER=$2
CONTAINER=$3
xterm -hold -e ssh -t $MACHINE 'docker exec --env TERM=xterm-256color --interactive --tty --user '$LOGIN_USER' '$CONTAINER' bash -c "cd /home && /bin/bash -l" && /bin/bash'