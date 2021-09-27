#!/bin/bash
WORKSPACE=$1
MACHINE=$2

cd $WORKSPACE && DOCKER_HOST="ssh://$MACHINE" docker-compose ps | awk 'NR>2' || exit 1
