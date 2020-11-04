eslint ./lib/*.js --format=json -o /var/lib/jenkins/reports/eslint_lib.json
eslint ./*.js --format=json -o /var/lib/jenkins/reports/eslint_root.json
echo $? > /dev/null
