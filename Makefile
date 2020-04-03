.PHONY: build shell test poc testr

NAMESPACE ?= tmck-code
REPOSITORY ?= punsy
TAG ?= $(shell git log -1 --format=%h)
IMAGE ?= $(NAMESPACE)/$(REPOSITORY)

build:

shell: build
	docker run -it $(IMAGE) bash

test: build
	docker run -it $(IMAGE) bash -c "python -m unittest"

deploy/build:
	docker build -f ops/Dockerfile -t $(IMAGE):base .
	docker build -f ops/Pip.dockerfile -t $(IMAGE):$(TAG) .

poc: build deploy/build
	docker run -it $(IMAGE):$(TAG) bash -c \
		"punsy --sentence 'Napoleon Dynamite' --offset 4"

deploy/test: build deploy/build
	docker run -it $(IMAGE):$(TAG) bash -c \
		"punsy --sentence 'napoleon dynamite' && \
		python -m twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*"

deploy/prod: build deploy/build
	docker run -it $(IMAGE):$(TAG) bash -c \
		"punsy --sentence 'napoleon dynamite' && \
		python -m twine upload --skip-existing dist/*"
