Zabbix-agent Домашнее задание к занятию 10 «Jenkins»
=========

Основная часть
------------
1) Был сделан Freestyle Job, который работает следующим образом:
```
rm -rf /tmp/jenkins/ && git clone https://github.com/SkillPropil/zabbix-agent.git /tmp/jenkins && cd /tmp/jenkins && molecule test -s default

отрабатывает успешно
[34mINFO    [0m Verifier completed successfully.
[34mINFO    [0m Pruning extra files from scenario ephemeral directory
Finished: SUCCESS
```
<img width="968" alt="freestyle" src="https://github.com/SkillPropil/zabbix-agent/assets/56190694/d0a66f31-d3bf-4ee2-939f-40ca01cf9cf3">

2) Перенес в декларативный стиль 

```
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

завершился успешно:

[34mINFO    [0m Verifier completed successfully.
[34mINFO    [0m Pruning extra files from scenario ephemeral directory
[Pipeline] }
[Pipeline] // dir
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // withEnv
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS
```
<img width="1424" alt="declarative st1" src="https://github.com/SkillPropil/zabbix-agent/assets/56190694/643c414b-b8fc-417f-a13c-1e76f2b3d623">

3) Перенос в Jenkinsfile
--------------

Все перенес, результат работы:

```
Finished: SUCCESS

```
<img width="969" alt="declarative st2" src="https://github.com/SkillPropil/zabbix-agent/assets/56190694/95097d16-75bd-491e-8302-b590c5d2146b">

4) Сделано, ветка была всего одна, но файл он собрал
------------

```
Started by user admin
[Sun Jun 30 22:39:55 MSK 2024] Starting branch indexing...
 > git --version # timeout=10
 > git --version # 'git version 1.8.3.1'
using GIT_ASKPASS to set credentials log[ass
 > git ls-remote https://github.com/SkillPropil/zabbix-agent.git # timeout=10
 > git rev-parse --resolve-git-dir /var/lib/jenkins/caches/git-4ea9616a24aca0de594159bf42f49a59/.git # timeout=10
Setting origin to https://github.com/SkillPropil/zabbix-agent.git
 > git config remote.origin.url https://github.com/SkillPropil/zabbix-agent.git # timeout=10
Fetching & pruning origin...
Listing remote references...
 > git config --get remote.origin.url # timeout=10
 > git --version # timeout=10
 > git --version # 'git version 1.8.3.1'
using GIT_ASKPASS to set credentials log[ass
 > git ls-remote -h https://github.com/SkillPropil/zabbix-agent.git # timeout=10
Fetching upstream changes from origin
 > git config --get remote.origin.url # timeout=10
using GIT_ASKPASS to set credentials log[ass
 > git fetch --tags --progress --prune origin +refs/heads/*:refs/remotes/origin/* # timeout=10
Checking branches...
  Checking branch main
      ‘Jenkinsfile’ found
    Met criteria
Scheduled build for branch: main
Processed 1 branches
[Sun Jun 30 22:39:58 MSK 2024] Finished branch indexing. Indexing took 2.9 sec
Finished: SUCCESS




INFO     Verifier completed successfully.

INFO     Pruning extra files from scenario ephemeral directory

```
<img width="958" alt="multibranch" src="https://github.com/SkillPropil/zabbix-agent/assets/56190694/2c852f13-d3b0-4a73-84e5-1b3231b67edd">

5-6 и остальное
------------
код у меня получился вооот такой:

```
node("linux"){
    stage("Git checkout"){
        git credentialsId: 'ffe96819-81dc-41b1-a681-4c8bf4dd9039', url: 'https://github.com/aragastmatb/example-playbook.git'
    }
    stage("Sample define secret_check"){
        secret_check=params.PROD_RUN
    }
    stage("Run playbook"){
        if (secret_check){
            sh 'ansible-playbook site.yml -i inventory/prod.yml'
        }
        else{
            sh 'ansible-playbook site.yml -i inventory/prod.yml --check --diff'
        }
        
    }
}
```
Собсна все работает, проверено

<img width="1433" alt="scripted" src="https://github.com/SkillPropil/zabbix-agent/assets/56190694/1bf7587b-5122-4af6-a7fa-dd66b1e185e4">

