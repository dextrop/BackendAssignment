.PHONY: help
all: help
help: Makefile
	@echo
	@echo " Commands:"
	@echo
	@sed -n 's/^##//p' $< | sed -e 's/^/ /' | sort
	@echo

## runserver             	Run Backend API Server
runserver:
	python manage.py runserver 0.0.0.0:8000

## migrate             		Run Database migration
migrate:
	python manage.py makemigrations api
	python manage.py migrate

## migrate             		Run Database migration
install:
	pip install -r requirements.txt