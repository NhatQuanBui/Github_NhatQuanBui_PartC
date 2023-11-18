run:
	python mypackage/main.py
install:
	pip install -r requirement.txt
build:
	python setup.py build bdist_wheel
compile:
	#if it's a Python application, no compilation is needed.
test:
	python -m unittest discover -s . -p 'test_*.py'
clean:
	if exist "./build" rd /s /q build
	if exist "./dist" rd /s /q dist
	if exist "./myprojectname.egg-info" rd /s /q myprojectname.egg-info
