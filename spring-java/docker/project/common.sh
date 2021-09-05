REPO_DIR=$(realpath $(realpath $(dirname $PWD)/dependencies))
HOSTNAME=arthur-MS-7B24
DOCKER_DIR=$REPO_DIR
IMAGE_NAME=${IMAGE_NAME:-project-java-tomcat}
CONTAINER_USER=user
CONTAINER_NAME=project-java-tomcat
HOST_HOME=/home/arthur
