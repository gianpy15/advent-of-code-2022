SRC_DIR		= src
TEST_DIR	= tests
CHECK_DIRS = $(SRC_DIR) $(TEST_DIR)
DOCS_DIR 	= docs
path = src/advent-of-code-2022
prefix = $(path)/day$(shell date +%d)

.PHONY: install
install: poetry run pip install --upgrade pip
	poetry install -v


.PHONY: format
format: ## Format repository code
	poetry run black $(CHECK_DIRS)
	poetry run isort $(CHECK_DIRS)

.PHONY: clean
clean: ## Clean the repository
	rm -rf dist
	rm -rf *.egg-info

.PHONY: run
run:
	python $(prefix)/main.py

.PHONY: new-day
new-day:
	mkdir -p $(prefix)

	cp $(path)/day00/main.py $(prefix)/main.py
	touch $(prefix)/input.txt

.PHONY: help
help: ## Show the available commands
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

