.PHONY: ship test

test:
	flake8 slackdown
	coverage run setup.py test
	coverage report -m

ship:
	python setup.py sdist bdist_wheel
	twine upload dist/* --skip-existing
