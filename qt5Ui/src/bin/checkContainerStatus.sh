#!/bin/bash
WORKSPACE=$1
MACHINE=$2

ssh -q -o ConnectTimeout=5 $MACHINE exit || exit 1
cd $WORKSPACE && DOCKER_HOST="ssh://$MACHINE" docker-compose ps | awk 'NR>2' || exit 1
