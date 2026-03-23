pipeline {
    agent any

    stages {
        stage('Setup Python') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t lab1-app .'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker stop lab1-container || exit 0'
                bat 'docker rm lab1-container || exit 0'
                bat 'docker run -d -p 8000:8000 --name lab1-container lab1-app'
            }
        }
    }
}