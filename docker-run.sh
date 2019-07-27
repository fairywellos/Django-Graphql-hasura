#! /bin/bash
DB_USER=django-saas
DB_PASSWORD=r1zEAflGfKLl1Fb3
DB_NAME=django-saas
HASURA_SAAS_AUTH_WEBHOOK=http://localhost:8080/hasura/webhook/auth/

#docker run -d -p 8080:8080 \
#-e HASURA_GRAPHQL_DATABASE_URL=postgres://"${DB_USER}":"${DB_PASSWORD}"@localhost:5432/"${DB_NAME}" \
#-e HASURA_GRAPHQL_ENABLE_CONSOLE=true \
##       -e HASURA_GRAPHQL_AUTH_HOOK=http://@host.docker.internal":8000""${HASURA_SAAS_AUTH_WEBHOOK}" \
#-e HASURA_GRAPHQL_AUTH_HOOK=http://localhost:8080/hasura/webhook/auth/ \
#hasura/graphql-engine:latest

#!/usr/bin/env bash
docker run -d --net=host \
  -e HASURA_GRAPHQL_DATABASE_URL=postgres://"${DB_USER}":"${DB_PASSWORD}"@localhost:5432/"${DB_NAME}" \
  -e HASURA_GRAPHQL_ENABLE_CONSOLE=true \
  hasura/graphql-engine:latest
  