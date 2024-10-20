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
                    docker build -t ${DOCKER_REPOSITORY}:${BUILD_NUMBER} .
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
                        docker.image("${DOCKER_REPOSITORY}:${BUILD_NUMBER}").push()
                    }
                }
            }
        }
        stage('Update Deployment File') {
            environment {
                GIT_REPO_NAME = "DevOps-CI-CD-2024-project-manifests"
                GIT_USER_NAME = "rakeshbasnet"
            }
            steps {
                withCredentials([string(credentialsId: 'github-token', variable: 'GITHUB_TOKEN')]) {
                    sh '''
                        git config user.email "rakeshbasnet086@gmail.com"
                        git config user.name "Rakesh Basnet"
                        BUILD_NUMBER=${BUILD_NUMBER}
                        sed -i "s/ImageTag/${BUILD_NUMBER}/g" flask-image-manifests/deployment.yml
                        git add flask-image-manifests/deployment.yml
                        git commit -m "Update deployment image to version ${BUILD_NUMBER}"
                        git push https://${GITHUB_TOKEN}@github.com/${GIT_USER_NAME}/${GIT_REPO_NAME} HEAD:main
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
        always {
            echo 'Pipeline completed.'
        }
    }
}