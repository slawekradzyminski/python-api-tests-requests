pipeline {
    agent { docker 'python:3.13.1' }
    stages {
        stage('install and run tests on python 3.13') {
            steps {
                sh 'python -m venv .venv'
                sh 'source .venv/bin/activate'
                sh 'pip install -r requirements.txt'
                sh 'pytest --html=report_313.html --self-contained-html'
            }
        }
    }
}