pipeline {
    agent any 
	triggers {
        cron('2 13 * * *') // Schedule to run every day at 1:00 PM
    }
    stages {
        stage('Build') { 
            steps {
                sh 'python -m py_compile source/my_build.py ' 
                stash(name: 'compiled-results', includes: 'source/*.py*')
                bat ' python C:\\WareHouse\\2023-2024\\mygit\\test\\py_test\\source\\my_build.py'				
            }
        }
    }
}