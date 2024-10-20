pipeline {
    agent any

    environment {
        // Private Docker image repository
        DOCKER_REPOSITORY = "rakeshbasnet/flask-s3file-upload"
        GIT_REPO_NAME = "DevOps-CI-CD-2024-project-manifests"
        GIT_USER_NAME = "rakeshbasnet"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    // Build the Docker image
                    sh "docker build -t ${DOCKER_REPOSITORY}:${BUILD_NUMBER} ."
                    echo "Docker image built successfully!"
                }
            }
        }

        stage('Push Docker Image to Registry') {
            steps {
                script {
                    echo "Pushing Docker image to Docker Hub..."
                    // Push the Docker image to Docker Hub
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-creds') {
                        docker.image("${DOCKER_REPOSITORY}:${BUILD_NUMBER}").push()
                    }
                    echo "Docker image pushed successfully!"
                }
            }
        }

        stage('Update Deployment File') {
            steps {
                withCredentials([string(credentialsId: 'github-token', variable: 'GITHUB_TOKEN')]) {
                    script {
                        echo "Checking out the deployment repository..."

                        // Checkout the deployment repository
                        checkout([
                            $class: 'GitSCM',
                            branches: [[name: '*/main']],
                            userRemoteConfigs: [[
                                url: "https://${GITHUB_TOKEN}@github.com/${GIT_USER_NAME}/${GIT_REPO_NAME}.git"
                            ]]
                        ])

                        // Check out the main branch
                        sh "git checkout main"

                         // Configure Git user
                        sh '''
                            git config --global user.email "rakeshbasnet086@gmail.com"
                            git config --global user.name "Rakesh Basnet"
                        '''

                        echo "Updating deployment file..."
                        // Update the deployment.yml file
                        sh "sed -i 's#image: rakeshbasnet/flask-s3file-upload:.*#image: rakeshbasnet/flask-s3file-upload:${BUILD_NUMBER}#' flask-image-manifests/deployment.yml"

                        // Commit and push the changes
                        sh """
                            git add flask-image-manifests/deployment.yml
                            git commit -m "Update deployment image to version ${BUILD_NUMBER}" || echo "No changes to commit"
                            git push origin main
                        """
                        echo "Deployment file updated and pushed successfully!"
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
            echo 'Pipeline failed!'
        }
        always {
            echo 'Pipeline completed.'
        }
    }
}
