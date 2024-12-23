pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'python -m py_compile source/my_build.py ' 
                stash(name: 'compiled-results', includes: 'source/*.py*')
                bat '"\\smtcf01019.rd.corpintra.net\RANGASS$\data\My Documents\GitHub\py_test\source\my_build.py"				
            }
        }
    }
}