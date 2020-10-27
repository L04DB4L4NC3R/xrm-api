pipeline {
	agent any

	stages {
		stage("SonarScanner Stage") {
			environment {
				scannerHome = tool 'SonarQube Scanner'
			}
			steps {
				withSonarQubeEnv('SonarQube Scanner') {
					sh '${sonarHome}/bin/sonar-scanner'
				}
			}
		}
	}
}
