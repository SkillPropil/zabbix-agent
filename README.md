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

```
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
3) Перенос в Jenkinsfile
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
