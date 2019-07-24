.PHONY: build shell test poc

build:
	docker build -f ops/Dockerfile -t punsy:latest .

shell: build
	docker run -it punsy:latest bash

test: build
	docker run -it punsy:latest bash -c "python -m unittest"

poc: build
	docker run -it punsy:latest bash -c "./punsy/cmu.py /home/punsy/cmudict-0.7b.utf8 'Napoleon Dynamite' 4"
