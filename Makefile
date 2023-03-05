.DEFAULT_GOAL := help

help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

tidy: ## Tidy code
	pipenv run tidy

lint: ## Lint the code
	pipenv run lint

test: ## Run tests
	pipenv run test

convert-pdf: ## Converts pdf to mp3
	pipenv run python src/pdf_to_mp3.py src/Sample.pdf
