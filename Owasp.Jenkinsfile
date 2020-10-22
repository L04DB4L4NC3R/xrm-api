pipeline {
	agent any
		stages {
			stage("Make package-lock") {
				steps {
					sh 'npm i --package-lock-only'
				}
			}
			stage("OWASP") {
				steps {
					sh '/var/lib/jenkins/dependency-check/bin/dependency-check.sh --scan `pwd` --format JSON --out /var/lib/jenkins/reports/owasp.json'
				}
			}


		}
}
