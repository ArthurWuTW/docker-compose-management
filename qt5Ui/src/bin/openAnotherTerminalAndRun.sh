#!/bin/bash
xterm -hold -e ssh -t arthur@10.1.1.16 'docker exec --env TERM=xterm-256color --interactive --tty --user user project-postgres-db-standby bash -c "cd /home && /bin/bash -l" && /bin/bash'