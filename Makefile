NAMESPACE  ?= tmck-code
REPOSITORY ?= punsy
IMAGE      ?= $(NAMESPACE)/$(REPOSITORY)
TAG        ?= $(shell git log -1 --format=%h)

build:
	docker build -f ops/Dockerfile -t $(IMAGE):base .
	docker build -f ops/Pip.dockerfile -t $(IMAGE):$(TAG) .

shell: build
	docker run -it $(IMAGE):$(TAG) bash

test: build
	docker run -it $(IMAGE):$(TAG) bash -c "python -m unittest"

poc: build
	docker run -it $(IMAGE):$(TAG) bash -c \
		"punsy --sentence 'Napoleon Dynamite' --offset 4 -v"

deploy/test: build
	docker run -it $(IMAGE):$(TAG) bash -c \
		"punsy --sentence 'napoleon dynamite' && \
		python -m twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*"

deploy/prod: build
	docker run -it $(IMAGE):$(TAG) bash -c \
		"punsy --sentence 'napoleon dynamite' && \
		python -m twine upload --skip-existing dist/*"

.PHONY: build shell test poc deploy/test deploy/prod
