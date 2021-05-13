PROJECT_NAME=grokking-deep-learning
TEST_PATH=./


help:
	@echo "install - install project in dev mode using conda"
	@echo "test -  run tests quickly within env: $(PROJECT_NAME)"


test:
	@echo "\n--- If the env $(PROJECT_NAME) doesn't exist, run 'make install' before ---\n"n
	@echo "\n--- Running tests at $(PROJECT_NAME) ---\n"
	bash -c "source activate $(PROJECT_NAME) &&  py.test --verbose --color=yes $(TEST_PATH)"


install:
	@bash install.sh
