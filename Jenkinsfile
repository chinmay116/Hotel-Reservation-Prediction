pipeline{
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "mlops-463410"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
    }

    stages{
        stage('Cloning Github Repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github Repo to Jenkins..........'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/chinmay116/Hotel-Reservation-Prediction.git']])
                }
            }
        }

        stage('Setting up our Virtual Environment & Installing Dependencies'){
            steps{
                script{
                    echo 'Setting up our Virtual Environment & Installing Dependencies.............'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }

        stage('Building & Pushing Docker Image to GCR'){
            steps{
                withCredentials([file(credentialsId : 'gcp-key', variable : 'GOOGLE_APP_CREDENTIALS')]){
                    script{
                        echo 'Building & Pushing Docker Image to GCR.......................'
                        sh '''
                        export PATH=$PATH:$(GCLOUD_PATH)

                        gcloud auth activate-service-account --key-file=${GOOGLE_APP_CREDENTIALS}

                        gcloud config set project ${GCP_PROJECT}

                        gcloud auth configure-docker --quiet

                        docker build -t gcr.io/${GCP_PROJECT}/hotel-reservation:latest .
                        
                        docker push gcr.io/${GCP_PROJECT}/hotel-reservation:latest
                        '''
                    }
                }
            }
        }
    }
}