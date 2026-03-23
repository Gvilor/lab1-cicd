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

        stage('Build') {
            steps {
                echo 'Build successful'
            }
        }

        stage('Deploy') {
            steps {
                bat 'if not exist deploy mkdir deploy'
                bat 'copy main.py deploy\\main.py'
            }
        }
    }
}