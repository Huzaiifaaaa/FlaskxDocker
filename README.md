# FlaskxDocker

This is a project that demonstrates running a Flask application both locally and using Docker.

## Running the Flask Application Locally

To run the Flask application locally, follow these steps:

1. Make sure you have Python installed on your machine.
2. Install the required dependencies by running the following command in your terminal:

   ```shell
   pip install -r requirements.txt
2. Run Main file:

   ```shell
   python Main.py
## Running the Flask Application via Docker

1. **Build the Docker image:**

    ```bash
    docker build -t <image_name>:<tag> .
    ```

    Replace `<image_name>` and `<tag>` with your desired names. The `.` at the end indicates that the Dockerfile is in the current directory. For example:

    ```bash
    docker build -t myapp:latest .
    ```

2. **Run a container from the built image:**

    ```bash
    docker run --name <container_name> -p 5001:5001 <image_name>:<tag>
    ```

    Replace `<container_name>`, `<image_name>`, and `<tag>` with appropriate values. `-p` is used to map ports between the host and the container. For example:

    ```bash
    docker run --name mycontainer -p 5001:5001 myapp:latest
    ```

    This command will run a container named `mycontainer` from the `myapp:latest` image, mapping port `5001` of the host to port `5001` of the container, assuming your Flask application is running on port `5001`.