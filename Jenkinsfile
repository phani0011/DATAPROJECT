pipeline {
    agent any

    stages {

        stage('Check Docker') {
            steps {
                sh 'docker --version'
            }
        }

        stage('Checkout Code') {
            steps {
                echo 'Cloning GitHub repo...'
            }
        }

        stage('Build Flask Docker Image') {
            steps {
                sh 'docker build -t flask-app -f docker/flask.dockerfile .'
            }
        }
    }
}




