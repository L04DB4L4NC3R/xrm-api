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
				sh '/var/lib/jenkins/scripts/audit.sh'
			}
		}
	}
}
