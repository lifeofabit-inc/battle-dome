.PHONY: all feature

GITHUB_TEAM := loab-revolt
REPO_NAME := battle-dome


all:
	@echo "Available commands: \n \
		*  \n \
"

feature:
# Ex: make feature name=cool-stuff
# TODO - Integrate hub package for PR?
# TODO - Query parameters?
	git checkout develop
	git pull origin develop
	git checkout -b feature/${name} develop
	git commit --allow-empty -m "make pull request"
	git push origin feature/${name}
	open https://github.com/${GITHUB_TEAM}/${REPO_NAME}/compare/develop...feature/${name}\?title\=Feature:+${name}\&labels\=enhancement

hotfix:
# Ex: make hotfix name=fix-stuff
	git checkout main
	git pull origin main
	git checkout -b hotfix/${name} main
	git commit --allow-empty -m "make pull request"
	git push origin hotfix/${name}
	open https://github.com/${GITHUB_TEAM}/${REPO_NAME}/compare/main...hotfix/${name}\?title\=Hotfix:+${name}\&labels\=bug


delete-branch:
# Ex: make delete-branch name=feature/cool-stuff
	git checkout develop
	git push origin --delete ${name}
	git branch -D ${name}






# push_dag:
# # Pushes a DAG file to the MWAA dagbag
# # Ex: make push_dag stack_env=dev dag_file=segment_dag.py
# 	aws s3 cp dags/${dag_file} s3://${AIRFLOW_BUCKET}/dags/
# 	@echo "Pushed ${dag_file} to S3 bucket ${AIRFLOW_BUCKET}"
