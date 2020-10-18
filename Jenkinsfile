pipeline {
	agent any

	stages {
		stage("Make package-lock") {
			sh 'npm i --package-lock-only'
		}

		stage("Npm Audit") {
			sh 'npm audit'
		}
	}
}
