pipeline {
    agent any
    
    triggers {
        githubPush()
    }

    stages {

        stage('Delete old Repo') {
            steps {
                sh '''  
                    #!/bin/bash
                    cd /home/arthur/Desktop/jenkins-tmp-dir
                    rm -rf docker-java || echo 'No repo exists!'
                '''
            }
        }

        stage('Clone Respository') {
            steps {
                sh '''  
                    #!/bin/bash
                    cd /home/arthur/Desktop/jenkins-tmp-dir
                    git clone https://github.com/ArthurWuTW/docker-java
                '''
            }
        }

        stage('Copy 3Party Package') {
            steps {
                sh '''  
                    #!/bin/bash
                    cd /home/arthur/Desktop/jenkins-tmp-dir
                    cp ./3party/eclipse-jee-2020-03-R-incubation-linux-gtk-x86_64.tar.gz \
                        ./docker-java/dependencies/eclipse_tar_dir/
                '''
            }
        }

        stage('Stop Container') {
            steps {
                sh '''  
                    #!/bin/bash
                    cd /home/arthur/Desktop/jenkins-tmp-dir
                    cd ./docker-java/docker
                    ./project-stop-container || echo 'No container started!'
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh '''  
                    #!/bin/bash
                    cd /home/arthur/Desktop/jenkins-tmp-dir
                    cd ./docker-java/docker
                    ./project-build-image
                '''
            }
            
        }
        
        stage('Start Container') {
            steps {
                sh '''  
                    #!/bin/bash
                    cd /home/arthur/Desktop/jenkins-tmp-dir
                    cd ./docker-java/docker
                    ./project-start-container
                '''
            }
        }

        stage('Delete Temp Repo') {
            steps {
                sh '''  
                    #!/bin/bash
                    cd /home/arthur/Desktop/jenkins-tmp-dir
                    rm -r ./docker-java
                '''
            }
        }
    }
}
