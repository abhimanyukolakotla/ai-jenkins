# AI Jenkins

## Docker setup for Jenkins and Node

### Create Docker Images

> `docker build . -t jenkins-image`

> `docker build . -t node-jenkins-image`

> `docker build . -t py-jenkins-image`

### Create Docker Container

> `docker run -p 8080:8080 --name jenkins-container jenkins-image`

> `docker run -p 3000:3000 --name node-jenkins-container node-jenkins-image`

> `docker run -p 80:80 --name py-jenkins-container py-jenkins-image`

### Stop Docker Container

> `docker stop jenkins-container`

> `docker stop node-jenkins-container`

### Start/Restart Docker Container

> `docker start jenkins-container`

> `docker start node-jenkins-container`

<hr />

## Jenkins Setup

> Create a user and update credentials in .env file

> After this then create image for node project and then run node container
