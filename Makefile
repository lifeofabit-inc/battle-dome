.PHONY: list new-feature new-hotfix delete-branch run-jupyter

GITHUB_TEAM := lifeofabit-inc
REPO_NAME := battle-dome


list:
	@echo "Available commands: \n \
		*  new-feature\n \
		*  new-hotfix\n \
		*  delete-branch\n \
"

new-feature:
# Ex: make new-feature name=cool-stuff
# TODO - Integrate hub package for PR?
	git checkout develop
	git pull origin develop
	git checkout -b feature/${name} develop
	git commit --allow-empty -m "make pull request"
	git push origin feature/${name}
	open https://github.com/${GITHUB_TEAM}/${REPO_NAME}/compare/develop...feature/${name}\?title\=Feature:+${name}\&labels\=enhancement

new-hotfix:
# Ex: make new-hotfix name=fix-stuff
	git checkout main
	git pull origin main
	git checkout -b hotfix/${name} main
	git commit --allow-empty -m "make pull request"
	git push origin hotfix/${name}
	open https://github.com/${GITHUB_TEAM}/${REPO_NAME}/compare/main...hotfix/${name}\?title\=Hotfix:+${name}\&labels\=bug

merge-feature:
# Ex: make merge-feature name=cool-stuff
	git checkout develop
	git pull origin develop
	git checkout feature/${name}
	git pull origin feature/${name}
	git merge develop 
# TODO - Magic happens here 
# git merge --squash feat-fuu-backup && git push -f -u origin feat-fuu (https://gist.github.com/aortbals/2aeb557bf127dd7ae88ea63da93479fc)
# curl -X PUT -H "Authorization: token ${adminToken}" --data '{"merge_method":"squash"}' https://github.<>.com/api/v3/repos/:org/:repo/pulls/${PR_ID}/merge 
# TODO - DELETE THE FEATURE BRANCH

delete-branch:
# Ex: make delete-branch name=feature/cool-stuff
	git checkout develop
	git push origin --delete ${name}
	git branch -D ${name}

run-jupyter:
	docker build -t lifeofabit/jupyter-notebook analysis/
	docker run -p 8888:8888 -v ${PWD}/analysis:/home/jovyan/work/analysis -v ${PWD}/data:/home/jovyan/work/data lifeofabit/jupyter-notebook
