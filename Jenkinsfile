pipeline {
    agent {
  label 'ansible'
    }
  environment {
        
        GIT_REPO_URL = 'https://github.com/SkillPropil/zabbix-agent.git'

    }
    stages {
        stage('First') {
            steps {
                sh 'rm -rf /tmp/jenkins'
            }
        }
        stage('Second') {
            steps{
                dir('/tmp/jenkins') {
                sh 'git clone $GIT_REPO_URL'
            }
          }
        }
        stage('Third'){
            steps {
                dir('/tmp/jenkins/zabbix-agent') {
                    sh 'molecule test -s default'
                }
            }
        }
    }
}