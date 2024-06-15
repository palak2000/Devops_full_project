pipeline {
    agent any

    environment {
        DOCKERHUB_REPO = 'Devops_frontend_backend_project/flask-app'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "this stage is passed"
                // git branch: 'main', url: 'https://github.com/your-repo/flask-app.git', credentialsId: 'Docker_pass'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${env.DOCKERHUB_REPO}:${env.BUILD_ID}")
            }
        }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop and remove any existing container
                    sh '''
                    docker stop flask-app || true
                    docker rm flask-app || true
                    '''

                    // Run the new container
                    docker.image("${env.DOCKERHUB_REPO}:${env.BUILD_ID}").run('-d -p 5000:5000 --name flask-app')
                }
            }
        }
    }

    post {
        success {
            echo 'Application deployed successfully!'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}
