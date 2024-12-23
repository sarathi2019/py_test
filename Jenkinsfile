pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'python -m py_compile source/my_build.py ' 
                stash(name: 'compiled-results', includes: 'source/*.py*')
                bat 'source/my_build.py'				
            }
        }
    }
}