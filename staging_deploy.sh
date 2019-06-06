#!/usr/bin/env bash
git pull
docker-compose down -v --rmi all --remove-orphans &&
