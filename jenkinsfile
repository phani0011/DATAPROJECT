pipeline {
    agent any

    environment {
        FLASK_IMAGE = "flask-app"
        SPARK_IMAGE = "spark-app"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Cloning GitHub repo..."
                checkout scm
            }
        }

        stage('Build Flask Docker Image') {
            steps {
                echo "Building Flask image..."
                sh 'docker build -t $FLASK_IMAGE -f docker/flask.dockerfile .'
            }
        }

        stage('Build Spark Docker Image') {
            steps {
                echo "Building Spark image..."
                sh 'docker build -t $SPARK_IMAGE -f docker/spark.dockerfile .'
            }
        }

        stage('Load Images into Minikube') {
            steps {
                echo "Loading images into Minikube..."
                sh 'minikube image load $FLASK_IMAGE'
                sh 'minikube image load $SPARK_IMAGE'
            }
        }

        stage('Deploy Flask to Kubernetes') {
            steps {
                echo "Deploying Flask app..."
                sh 'kubectl apply -f k8s/flask-deployment.yaml'
            }
        }

        stage('Run Spark Job') {
            steps {
                echo "Running Spark job..."
                sh 'kubectl delete job spark-job || true'
                sh 'kubectl apply -f k8s/spark-job.yaml'
            }
        }
    }

    post {
        success {
            echo "CI/CD Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs."
        }
    }
}

