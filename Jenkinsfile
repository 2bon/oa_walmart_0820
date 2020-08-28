pipeline {
    environment {
        registry = "docker_hub_account/repository_name"
        registryCredential = 'dockerhub'
    }
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('build docker Image') {
            steps {
                echo 'build'
                script {
                    def customImage = docker.build("hi_walmart-image:${env.BUILD_ID}")
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'

            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying docker image to registry'
               script {
                    docker.withRegistry( '', registryCredential ) {
                      customImage.push()
                    }
                  }
            }
        }
        stage('Integration Test') {
            steps {
                echo 'Integration Test'

            }
        }
        stage('Deploy to Production') {
            steps {
                echo 'Deploy to Production'

            }
        }
        stage('etc') {
            steps {
                echo 'etc'

            }
        }

    }
}