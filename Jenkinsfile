pipeline {
    agent any

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
                sh '/usr/local/bin/docker build --pull=false -t lab2-app .'
            }
        }

        stage('Deploy') {
            steps {
                sh '/usr/local/bin/docker stop lab2-container || true'
                sh '/usr/local/bin/docker rm lab2-container || true'
                sh '/usr/local/bin/docker run -d -p 8000:8000 --name lab2-container lab2-app'
            }
        }
    }
}