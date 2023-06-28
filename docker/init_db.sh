#!/bin/bash
cd docker || exit
docker-compose up -d && docker exec -i demo_go_db mysql -uroot -ppassword demo_go < db_create.sql
