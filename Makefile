.DEFAULT_GOAL := help

.PHONY: help
help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: tidy
tidy: ## Tidy code
	pipenv run tidy

.PHONY: lint
lint: ## Lint the code
	pipenv run lint

.PHONY: test
test: ## Run tests
	pipenv run test