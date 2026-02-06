# Docker

## installation

`sudo apt install docker-compose`
`sudo usermod -aG docker $USER`

## docker compose
indide the project dir:  

`docker-compose up -d` run in background  
`docker-compose down` stop and remove non persistent data  
`docker-compose stop` stop services  
`docker-compose ps` list processus  
`docker-compose logs -f prometheus` check live log  

## docker
`sudo service docker status/start/stop`  
`docker ps -a` list all container
`docker volume ls` list volumes  
`docker volume inspect volume-name` give the path of a volume  
`docker volume rm volume-name` remove a volume  
`docker volume prune` remove unused volumes  
`docker system prune` remove all volumes  
`docker container inspect`  
`docker network inspect`  
`docker network ls`  

