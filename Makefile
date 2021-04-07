SHELL := /bin/bash

.PHONY: package
package: packaged.zip

packaged.zip: cfn-publish.config template.yaml $(shell find functions/ -type f)
	zip -r $(@) $(<) \
		-x '**/__pycache*' @

.PHONY: test
test:
	cfn-lint template.yaml
	cfn_nag template.yaml

.PHONY: setup
setup:
	pip3 install -r requirements.txt && pre-commit install

.PHONY: version
version:
	@echo $(shell cfn-flip template.yaml | python -c 'import sys, json; print(json.load(sys.stdin)["Metadata"]["Version"])')
