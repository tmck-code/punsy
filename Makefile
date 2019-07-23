.PHONY: fetch build shell test

fetch:
	./ops/data.sh
	./ops/normalise.py cmudict-0.7b

build:
	docker build -f ops/Dockerfile -t punsy .

shell: build
	docker run -it punsy:latest bash

test: build
	docker run -it -v $(shell pwd):/home/punsy punsy bash -c "python -m unittest"

