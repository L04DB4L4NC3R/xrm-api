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
				sh '/var/lib/jenkins/reports/audit.sh'
			}
		}

		stage("Retire") {
	               steps {
                               sh 'retire --path `pwd` --outputformat json --outputpath /var/lib/jenkins/reports/retire.json'
                       }		
		}

                  stage("NodeJsScan") {
                       steps {
                               sh 'nodejsscan -d `pwd` --output nodejsscan_report.json'
                       }
                }		


	}
}
