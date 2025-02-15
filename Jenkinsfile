pipeline {
    agent { label 'vm2' }

    environment
    {
        GHCR_USERNAME = 'Oum789'
        GHCR_TOKEN = credentials('ghcr-pat')  // ดึง PAT จาก Jenkins Credentials
        IMAGE_NAME = 'ghcr.io/oum789/sample-api'
        IMAGE_TAG = 'lastest'
    }

    stages {

        stage('Clone API Repo') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Oum789/CICD-Testing.git'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh './venv/bin/python -m unittest discover -s tests'
            }
        }

        stage('Login to GHCR') {
            steps {
                withCredentials([string(credentialsId: 'ghcr-pat', variable: 'GHCR_TOKEN')]) {
                sh 'echo "$GHCR_TOKEN" | docker login ghcr.io -u $GHCR_USERNAME --password-stdin'
                }

            }

        }

        stage('Build Image') {
            steps {
                sh "docker build -t $IMAGE_NAME:$IMAGE_TAG ."
            }
        }

        stage('Create Container and Map Port')
        {
            steps{
                // sh "docker rm -f sample-api"
                sh "docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME:$IMAGE_TAG" // เป็น bridge network จะใช้ ip เครื่อง VM ที่ run jenkins master
            }
        }

        stage('Clone Robot Repo') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Oum789/CICD-Robot-Testing.git'
            }
        }

        stage('Run Robot Tests') {
            steps {
                sh '''#!/bin/bash
                source ./venv/bin/activate && ./venv/bin/python -m robot test-calculate.robot
                '''
            }
        }

        stage('Push sample-api image')
        {
            steps{
                sh "docker push $IMAGE_NAME:$IMAGE_TAG"
            }
        }



    }
}
