test: 
	python -m unittest discover -p "*_test.py"

deploy:
	sls deploy --stage=dev