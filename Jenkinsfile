pipeline {
    agent any

    environment {
        // Private Docker image repository
        DOCKER_REPOSITORY= "rakeshbasnet/flask-s3file-upload"
    }

    stages {
       stage('Build Docker Image') {
            steps {
                script {
                    // Building docker image
                    sh '''
                    echo "Building docker image"
                    docker build -t ${DOCKER_REPOSITORY}::{BUILD_NUMBER} .
                    echo "Docker image built successfully!"
                    '''
                }
            }
        }
        stage('Push docker image to Registry') {
            steps {
                script {
                    // Pushing docker image to Dockerhub
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-creds') {
                        docker.image("${DOCKER_REPOSITORY}:${BUILD_NUMBER}").push('latest')
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed.'
        }
        always {
            echo 'Pipeline completed successfully.'
        }
    }
}