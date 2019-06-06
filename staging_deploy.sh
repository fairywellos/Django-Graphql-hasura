#!/usr/bin/env bash
sudo su
git pull
docker-compose down -v --rmi all --remove-orphans &&
