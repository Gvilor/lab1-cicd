pipeline {
    agent any

    environment {
        PATH = "/Applications/Docker.app/Contents/Resources/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    }

    stages {
        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build --pull=false -t lab2-app .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker stop lab2-container || true'
                sh 'docker rm lab2-container || true'
                sh 'docker run -d -p 8000:8000 --name lab2-container lab2-app'
            }
        }
    }
}