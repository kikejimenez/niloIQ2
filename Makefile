REQUERIMENTS=$(shell cat settings.ini | grep -o "requirements =.*" | cut -f3- -d' ')

install_dependencies:
	pip install $(REQUERIMENTS)

		