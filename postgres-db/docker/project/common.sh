REPO_DIR=$(realpath $(realpath $(dirname $PWD)/dependencies))
HOSTNAME=$(cat /etc/hostname)
DOCKER_DIR=$REPO_DIR
IMAGE_NAME=${IMAGE_NAME:-project-postgresql-db}
CONTAINER_USER=user
CONTAINER_NAME=project-postgresql-db
DB_TMP_DIR=$HOME/Desktop/db_tmp
