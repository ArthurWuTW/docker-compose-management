#!/bin/bash
WORKSPACE=$1
MACHINE=$2

cd $WORKSPACE && DOCKER_HOST="ssh://$MACHINE" docker-compose down || exit 1
