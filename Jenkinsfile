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
				sh 'npm i'
                               sh 'retire --path `pwd` --outputformat json --outputpath /var/lib/jenkins/reports/retire.json --exitwith 0'
                       }		
		}

                stage ("SCA - EsLint"){
                    steps {
                            sh '/var/lib/jenkins/reports/lint.sh'
			}

		}
                  stage("NodeJsScan") {
                       steps {
                               sh 'nodejsscan -d `pwd` --output /var/lib/jenkins/reports/nodejsscan_report.json'
                       }
                }		

	}
}
