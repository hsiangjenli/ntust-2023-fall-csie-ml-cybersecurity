cpindex:
	cp docs/source/index.rst README.rst

cleanup:
	cd docs && rm -rf build

build:
	make cpindex
	cd docs && make html