# DragonDocker

Launch your projects safely into space with DragonDocker.

# Requirements

1. A `public server` with `Docker` installed.
2. A local machine running `Python3`.

# How it Works

DragonDocker pushes a directory of Docker based projects up to your private server runs them. Each project is then accessible at /projectName because a `Nginx server` acting as a `reverse proxy` forwards requests to the correct address.

`Projects survive` server restarts and shutdowns as containers are started with the `restart always` policy.

# How to Use

1. Place your Docker based projects inside the apps directory.
2. Run `build.py`.
3. Run `push.py`.
4. Visit `/` for a list of projects, or `/projectName` to visit a specific project.

# Note

Containers should, expose, and serve content over `port 8080`. 
