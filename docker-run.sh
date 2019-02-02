docker run -d -p 8080:8080 \
  -e HASURA_GRAPHQL_DATABASE_URL=postgres://"${HASURA_SAAS_USER}":"${HASURA_SAAS_PASSWORD}"@host.docker.internal:5432/"${HASURA_SAAS_DATABASE}" \
  -e HASURA_GRAPHQL_ENABLE_CONSOLE=true \
  hasura/graphql-engine:latest