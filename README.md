# My Discord Rank

肝白名單

## how to build

docker build -t my-discord-rank . --no-cache

## how to run

### for product

docker run -i -t -d
-e Token={{auth_token}}
-e Channel_Id={{channel_id}}
--name {{container_name}} my-discord-rank

### for develop

docker run -i -t --rm -v "$PWD":/usr/src/myapp -w /usr/src/myapp
-e Token={{auth_token}}
-e Channel_Id={{channel_id}}
--name test my-discord-rank

## eagle

### build

docker build -f EagleDockerfile -t eagle-chat .

### run

docker run -i -t -d \
 -e Token={{token}} \
 --name {{container_name}} eagle-chat

## pokemon

### build

docker build -f PokemonDockerfile -t pokemon .

### run

docker run -i -t \
 -e Token={{token}} \
 --name {{container_name}} pokemon
