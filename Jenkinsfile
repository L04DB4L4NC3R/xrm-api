pipeline {
	agent any
	
	stages {
		stage("Audit") {
			steps {
				sh 'npm audit --json'
			}
		}
	}
}
