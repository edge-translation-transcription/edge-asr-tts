pipeline {
    agent { label 'docker' }
    options {
        buildDiscarder(logRotator(numToKeepStr: '5', daysToKeepStr: '30'))
        timestamps()
    }
    environment {
        SCANNERS            = 'protex,checkmarx'
        PROJECT_NAME        = 'edge-translation-transcription'
        SDLE_UPLOAD_PROJECT_ID = '22409'

    }
    stages {
        stage('Bandit') {
            agent {
                docker {
                    image 'amr-registry.caas.intel.com/rbhe-public/bandit-build-agent:latest'
                    reuseNode true
                }
            }

            steps {
                sh 'bandit -f txt **/*.py | tee bandit_scan.txt'
            }
        }

        stage('Static Code Analysis') {
            environment {
                SCANNERS     = 'trivy'           // required
                PROJECT_NAME = 'edge-translation-transcription' // required

                TRIVY_SEVERITY_THRESHOLD_CVE = 'CRITICAL'
            }
            steps {
                rbheStaticCodeScan()
            }
        }
    }
    post {
        always {
            archiveArtifacts allowEmptyArchive: true, artifacts: 'bandit_scan.txt'
            jcpSummaryReport() // Calling this function will automatically post data at the end of the build
            intelLogStashSend failBuild: false, verbose: true
        }
    }
}
