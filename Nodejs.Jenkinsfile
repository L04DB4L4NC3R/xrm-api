pipeline {
	agent any

	stages {
		stage("Make package-lock") {
			steps {
				sh 'npm i --package-lock-only'
			}
		}
                  stage("NodeJsScan") {
                       steps {
                               sh 'nodejsscan -d `pwd` --output /var/lib/jenkins/reports/nodejsscan_report.json'
                       }
                }		

	}
}
