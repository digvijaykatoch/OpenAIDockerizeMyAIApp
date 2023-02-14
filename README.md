# OpenAIDockerizeMyAIApp
Dockerfile and other configs for dockerizing my python + html5 + js app

To combine the Python Flask API app and the HTML5 frontend in a Dockerfile, you can follow these steps:

1.  Create a new directory for the project, and navigate into it:

-   `mkdir myapp
    cd myapp`

    -  Download/checkout this project into that myapp folder.

2.  Open a terminal window, and navigate to the project directory.

3.  Build the Docker image by running the following command:

    `docker build -t myapp .`

4.  Run the Docker container by running the following command:

`docker run -d -p 5000:5000 myapp`

5.  Open a web browser, and navigate to `http://localhost:5000` to see the application running.
