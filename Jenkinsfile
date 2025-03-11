pipeline {
    agent any
    environment {
        DOCKER_CREDENTIALS_ID = 'nexus-credentials'  // Nexus kimlik bilgilerinin ID'si
        NEXUS_DOCKER_REPO_URL = '188.245.124.4:8082/repository/berkenerji'  // Nexus Docker repository URL'si
        DOCKER_IMAGE_NAME = 'berkenerji'  // Docker imajının ismi
        DOCKER_TAG_LATEST = 'latest'  // Son imajın tag'ı
        DOCKER_TAG_BUILD = "${BUILD_NUMBER}"  // Jenkins build numarasına dayalı tag
    }
    stages {
        stage('Build') {
            steps {
                script {
                    // Docker image build et (latest ve build numarası tag'iyle)
                    sh "docker build -t ${DOCKER_IMAGE_NAME}:${DOCKER_TAG_LATEST} -t ${DOCKER_IMAGE_NAME}:${DOCKER_TAG_BUILD} ."
                }
            }
        }
        stage('Login to Nexus') {
            steps {
                script {
                    // Nexus Docker repository'e login ol
                    withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS_ID, passwordVariable: 'PASSWORD', usernameVariable: 'USERNAME')]) {
                        sh "echo ${PASSWORD} | docker login -u ${USERNAME} --password-stdin ${NEXUS_DOCKER_REPO_URL}"
                    }
                }
            }
        }
        stage('Push to Nexus') {
            steps {
                script {
                    // Docker image'ı Nexus'a tag'leyip pushla (hem latest hem build numarası ile)
                    sh """
                        docker tag ${DOCKER_IMAGE_NAME}:${DOCKER_TAG_LATEST} ${NEXUS_DOCKER_REPO_URL}/${DOCKER_IMAGE_NAME}:${DOCKER_TAG_LATEST}
                        docker push ${NEXUS_DOCKER_REPO_URL}/${DOCKER_IMAGE_NAME}:${DOCKER_TAG_LATEST}

                        docker tag ${DOCKER_IMAGE_NAME}:${DOCKER_TAG_BUILD} ${NEXUS_DOCKER_REPO_URL}/${DOCKER_IMAGE_NAME}:${DOCKER_TAG_BUILD}
                        docker push ${NEXUS_DOCKER_REPO_URL}/${DOCKER_IMAGE_NAME}:${DOCKER_TAG_BUILD}
                    """
                }
            }
        }

    }
}