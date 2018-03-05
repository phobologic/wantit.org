build:
	pipenv run stacker build --region us-east-1 ./stacker.yml

env:
	pipenv install stacker_blueprints==1.0.7
