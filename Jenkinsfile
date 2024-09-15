pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Simulate a build step
                sh 'echo "Building the project..."'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing...'
                // Simulate a test step
                sh 'echo "Running tests..."'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Simulate a deployment step
                sh 'echo "Deploying the application..."'
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