# Sports-Hub Application Python Back-End

## Project Description

This is a draft pet project for testing Generative AI on different software engineering tasks. It is planned to evolve and grow over time. Specifically, this repo will be a Python & FastAPI playground.

The application's legend is based on the sports-hub application description from the following repo: [Sports-Hub](https://github.com/dark-side/sports-hub).

## Available Front-End applications
- [React.js](https://github.com/dark-side/sports_hub_react_skeleton)
- [Angular](https://github.com/dark-side/sports_hub_angular_skeleton)

## Dependencies

- Docker
- Docker Compose

The mentioned dependencies can be installed using the official documentation [here](https://docs.docker.com/compose/install/).

## Setup and Running the Application

### Clone the Repositories

To run the web application with the React front-end, clone the following repositories within the same folder:

```sh
git clone git@github.com:dark-side/sports_hub_python_skeleton.git
git clone git@github.com:dark-side/sports_hub_react_skeleton.git
```

### Navigate to the back-end application directory

All commands should be run from the `sports_hub_python_skeleton` directory.

### Create .env File

Copy the .env.example file to .env in the root of the project directory:

```sh
cp .env.example .env
```

Update the .env file with your local development credentials and secrets. Make sure not to commit this .env file to version control. 

### Run Docker Compose

Navigate to the back-end application directory and run (`-d` for detached mode to run in the background):

```sh
docker compose up -d
```

### Attach to the Backend Container (Optionally)

Run `docker ps` and copy the `backend` application container ID. Then, connect to the container with the following command:

```sh
docker exec -ti <CONTAINER ID> /bin/bash
```

### Reset the Database

Inside the `backend` application container, run the following command to reset the database if needed:

```sh
<TBD>
```

### Running on Windows (Tips & Tricks)

While running the App on Windows 11 using WSL, you may face issues related to Unix-style line endings (especially if you are storing the project(s) under the host machine filesystem, not the WSL one (e.g., the project is cloned to the disc `c:` or any other disk you have instead of being cloned to the WSL filesystem). Working within the WSL filesystem is a best practice when developing on Windows, as it helps prevent line ending and permission issues that can arise when using the Windows filesystem. I'm just reminding you that this will save you time and headaches for future projects.

If you are still reading this, please ensure your host machine converts related script(s) to Unix-style line endings.

```sh
# Install dos2unix if not already installed
sudo apt-get install dos2unix

# Convert all files in the project directory to Unix-style line endings
find . -type f -exec dos2unix {} \;

# Convert one file (example)
dos2unix bin/docker-entrypoint
```

Also, if you face issues with `bin` directory files not being executable, you can fix it with the following commands:

```sh
# check current permissions on the file
ls -l bin/docker-entrypoint

# ensure the file is executable
chmod +x bin/docker-entrypoint
```

### Accessing the Application

To access the application in a browser locally, open the following URL:

- Mac, Linux - `http://localhost:3000/`
- Windows - `http://127.0.0.1:3000/`

### Local development environment setup

0. Python 3.12
1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) Package Manager
2. Run command:

```sh
uv install
```

### How to run tests

To run tests, run the following command:

```sh
pytest tests/
```

### How to run code checkers & formatter

```sh
ruff format api/ tests/
ruff check api/ tests/ --fix
```

## License

Licensed under either of

- [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)
- [MIT license](http://opensource.org/licenses/MIT)

Just to let you know, at your option.

## Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in your work, as defined in the Apache-2.0 license, shall be dual licensed as above, without any additional terms or conditions.

**Should you have any suggestions, please create an Issue for this repository**
