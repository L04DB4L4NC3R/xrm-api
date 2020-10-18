pipeline {
	agent any
	
	stages {
		stage("Install") {
			steps {
				sh 'npm install'
			}
		}
		stage("Audit") {
			steps {
				sh 'npm audit --json'
			}
		}
	}
}
