## Using Your Terminal with the wasm-pack Container

This container is configured to mount your external project directory (set in the `.env` file) into `/workspace` inside the container. You can build your project using `wasm-pack` in an isolated Rust environment.

### 1. Start the container

Navigate to this directory and run:

```shell
docker compose up -d
```

### 2. Access the container shell

Open a bash shell inside the running container:

```shell
docker compose exec wasm-pack /bin/bash
```

### 3. Build your project

Inside the container shell, navigate to the mounted project directory and run:

```shell
cd /workspace
wasm-pack build
```

### 4. Stop the container

When finished, exit the shell and stop the container:

```shell
docker compose down
```
