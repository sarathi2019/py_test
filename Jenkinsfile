pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                sh 'python -m py_compile source/my_build.py ' 
                stash(name: 'compiled-results', includes: 'source/*.py*')
                bat "C:\WareHouse\2023-2024\mygit\test\py_test\source\my_build.py"				
            }
        }
    }
}