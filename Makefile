IMAGE_NAME = sims4
CONTAINER_NAME = sims4
SSH_PORT = 2222
MOUNT_DIR_HOST ?= /Users/jafffy/workspace/sims4
MOUNT_DIR_CONTAINER ?= /app

.PHONY: build run stop start logs

build:
	docker buildx build -t $(IMAGE_NAME) --platform linux/arm64/v8 .

run:
	docker run -d -p $(SSH_PORT):22 -v $(MOUNT_DIR_HOST):$(MOUNT_DIR_CONTAINER) --name $(CONTAINER_NAME) $(IMAGE_NAME)

stop:
	docker stop $(CONTAINER_NAME)

start:
	docker start $(CONTAINER_NAME)

logs:
	docker logs $(CONTAINER_NAME)

attach:
	docker attach $(CONTAINER_NAME)

exec:
	docker exec -it $(CONTAINER_NAME) bash

clean:
	docker rm $(CONTAINER_NAME)

