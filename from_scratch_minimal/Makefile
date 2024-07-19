MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := serve
.DELETE_ON_ERROR:
.SUFFIXES:

build/main.py: main.py
	cp -f $< $@

.PHONY: serve
serve: build/main.py
	(cd build && FLASK_ENV=development FLASK_APP=main flask run)
