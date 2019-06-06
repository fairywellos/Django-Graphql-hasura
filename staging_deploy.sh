#!/usr/bin/env bash
sudo su
sudo chown -R $USER .
git pull
docker-compose down -v --rmi all --remove-orphans
