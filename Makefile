.PHONY: build shell test poc testr

NAMESPACE ?= tmck-code
REPOSITORY ?= punsy
TAG ?= $(shell git log -1 --format=%h)
IMAGE ?= $(NAMESPACE)/$(REPOSITORY):$(TAG)

build:
	docker build -f ops/Dockerfile -t $(IMAGE) .

shell: build
	docker run -it $(IMAGE) bash

test: build
	docker run -it $(IMAGE) bash -c "python -m unittest"

dist-build:
	docker tag $(IMAGE) $(REPOSITORY):latest
	docker build -f ops/Pip.dockerfile -t $(NAMESPACE)/$(REPOSITORY):deploy .

poc: build dist-build
	docker run -it $(NAMESPACE)/$(REPOSITORY):deploy bash -c \
		"punsy --sentence 'Napoleon Dynamite' --offset 4"

dist-test: build dist-build
	docker run -it $(NAMESPACE)/$(REPOSITORY):deploy bash -c \
		"punsy --sentence 'napoleon dynamite' && \
		python -m twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*"

dist-prod: build dist-build
	docker run -it $(NAMESPACE)/$(REPOSITORY):deploy bash -c \
		"punsy --sentence 'napoleon dynamite' && \
		python -m twine upload --skip-existing dist/*"
