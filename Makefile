.PHONY: all

all: build-a build-b

build-a: node-a/*
	docker build -t epif-poc/node-a node-a

build-b: node-b/*
	docker build -t epif-poc/node-b node-b

run-a:
	docker run --rm -t --privileged epif-poc/node-a "$(shell hostname -s)"

run-b:
	docker run --rm -t -p 1080:1080 epif-poc/node-b
