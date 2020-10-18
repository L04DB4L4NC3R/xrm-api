pipeline {
	agent any

	stages {
		stage("Make package-lock") {
			steps {
				sh 'npm i --package-lock-only'
			}
		}

		stage("Npm Audit") {
			steps {
				sh 'npm audit'
			}
		}
	}
}
