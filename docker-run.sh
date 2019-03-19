#!/usr/bin/env bash
docker run -d -p 8080:8080 \
  -e HASURA_GRAPHQL_DATABASE_URL=postgres://"${HASURA_SAAS_USER}":"${HASURA_SAAS_PASSWORD}"@host.docker.internal:5432/"${HASURA_SAAS_DATABASE}" \
  -e HASURA_GRAPHQL_ENABLE_CONSOLE=true \
  -e HASURA_GRAPHQL_ACCESS_KEY="${HASURA_SAAS_ACCESS_KEY}" \
  -e HASURA_GRAPHQL_AUTH_HOOK=http://@host.docker.internal":8000""${HASURA_SAAS_AUTH_WEBHOOK}" \
  hasura/graphql-engine:latest