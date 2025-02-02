# svelte-python-inventory-app

This project is a simple inventory web application with features including:
* User Authentication
* Inventory management via CRUD operations
* Separate items per user
* Modern front-end design

The code is distributed in two main directories, each with its own README explaining how they work.
1. [/frontend](./frontnend): Contains all of the frontend code, dependencies and README
2. [/backend](./backend): Contains all of the backend code dependencies and README
3. [/charts](./charts): Includes the helm charts for deploying the project on Kubernetes

This application was developed following the microservices architecture, meaning each component gets deployed separately as a docker container. The configuration of each one can be viewed in the [docker-compose.yml](./docker-compose.yml) file.

## Running the app

To run the project locally using docker, clone the repository and run `docker compose up -d --build` from the root directory. Everything should be automatically installed and launched. Access `localhost:3000` on the host machine to view the web app.
