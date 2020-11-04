cd /var/lib/jenkins/workspace/DVNA-Pipeline
npm audit --json > /var/lib/jenkins/reports/audit.json
echo $? > /dev/null
