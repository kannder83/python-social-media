## Commands:

To inicialice prodution:
docker-compose -f production.yml build

To start:
docker-compose -f production.yml up -d

For delete
docker-compose -f production.yml down --remove-orphans -v

## Create tables of DB:

In the instance of API is necesary runn:
alembic upgrade head
