#!/bin/bash
WORKSPACE=$1
MACHINE=$2

cd $WORKSPACE && DOCKER_HOST="ssh://$MACHINE" docker-compose up --build --detach || exit 1
