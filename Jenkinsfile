pipeline {
    agent { label 'vm2' }
    environment
    {
        GHCR_USERNAME = 'Oum789'
        GHCR_TOKEN = credentials('ghcr-pat')  // ดึง PAT จาก Jenkins Credentials
        IMAGE_NAME = 'ghcr.io/Oum789/sample-api'
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

        stage('Build & Push Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
                sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
            }
        }

    }
}
