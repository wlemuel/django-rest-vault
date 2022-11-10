.DEFAULT_GOAL := help

.PHONY: clean help build test_publish publish

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  help                                 display this help message"
	@echo "  clean                                delete build files"
	@echo "  build                                build package"
	@echo "  test_publish                         push dist to testpypi"
	@echo "  publish                              push dist to pypi"
	@echo ""

build:
	python -m build

test_publish:
	python -m twine upload --repository testpypi dist/*

publish:
	python -m twine upload dist/*

clean:
	@rm -rf django_rest_vault.egg_info
	@rm -rf dist
