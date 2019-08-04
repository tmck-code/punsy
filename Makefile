.PHONY: build shell test poc

build:
	docker build -f ops/Dockerfile -t punsy/punsy:latest .

shell: build
	docker run -it punsy/punsy:latest bash

test: build
	docker run -it punsy/punsy:latest bash -c "python -m unittest"

poc: build
	docker run -it punsy/punsy:latest bash -c \
		"punsy --cmu-file /home/punsy/cmudict-0.7b.utf8 --sentence 'Napoleon Dynamite' --offset 4"

