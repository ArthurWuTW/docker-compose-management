# django-docker-scripts
> This repository provides several scripts to create an isolated environment for django application

## Prerequisites
#### 1. Install Docker Engine on Ubuntu 16.04
```sh
cd install_docker
./ubuntu-16-04-install-docker-script -t -r
```
Run the script to start Docker installation/test and usermod setup(reboot to activate config), system will reboot after 20 seconds when installation done.

#### 2. Build Docker Image
```
cd docker/
./project-build-image
```

#### 3. Docker Operation
- Start Container

```sh
cd docker
./project-start-container
```

- Enter Container Shell

```sh
cd docker
./project-enter-container
```

- Stop Container
```sh
cd docker
./project-stop-container
```

## Container Settings
> All settings in **[docker/project/run-container](https://github.com/ArthurWuTW/django-docker-script/blob/master/docker/project/run-container)**. For django_project, the commonly-used params are shown in the following code piece.

```sh
# file: run-container
...
# container port 0.0.0.0:8000 mapped to host port 8000
PORT_MAPPING_OPTS="\
    -p 0.0.0.0:8000:8000  \
"

# mount persistent database files to replace origin empty database files
DATABASE_OPTS="\
     --volume $HOME/Desktop/django_project/data_directory/postgresql:/var/lib/postgresql \
"
...

docker run \
    ...
# Delete the specific line if you want to disable custom settings
    $PORT_MAPPING_OPTS \
    $DATABASE_OPTS \
    ...
...

```
