<div align="center">

# TagHub.Dev 
**Next-gen text analytics platform**

</div>

# I. Installation 

1. Install [Docker](https://www.docker.com/get-started/) and have it opened
2. Run:  `docker build . -t taghub`
3. Run: `docker run -p 4000:4000 --env PORT:4000 -t taghub:latest`

# II. API Documentation:
Documentation can be accessed via `localhost:4000` (Also depends on which port you used in [I])

# III. Development

1. Follow (I) 1+2 for the environment setup
3. Run: `docker run -d -p 4000:4000 --env PORT=4000 -v ${PWD}/src:/code taghub:latest`
2. Change the code, save and see these services react to your changes
3. Whenever you add a new package, please run `docker-compose up -d --build` again

**Note**:
`-v` is a "volume" that allows you to mount a local volume to a container's filesystem

# IV. Roadmap
@TODO: To be updated

# V. Contributing
@TODO: To be updated

# VI. License
GPLv3