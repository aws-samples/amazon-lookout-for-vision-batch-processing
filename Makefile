SHELL := /bin/bash

package:
	zip -r packaged.zip \
		functions \
		cfn-publish.config \
		template.yaml \
		-x '**/__pycache*' @

test:
	cfn-lint template.yaml
	cfn_nag template.yaml

version:
	@echo $(shell cfn-flip template.yaml | python -c 'import sys, json; print(json.load(sys.stdin)["Metadata"]["Version"])')
