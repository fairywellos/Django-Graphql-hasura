**How to setup this project**
----------

This short doc assumes you have docker installed on your computer.
If you do not have, [Install](https://docs.docker.com/get-started/) here.
The project runs on Postgres only because of the multi-tenancy strategy.

**Compulsory environmental variables**
* HASURA_SAAS_DATABASE: *This is the postgres database name you want to you, assumes you have the database created.  It defaults to 'hasura_saas'.*
* HASURA_SAAS_USER: *This is the postgres user name.  It defaults to 'postgres'.*
* HASURA_SAAS_PASSWORD: *This is the postgres user password.  It defaults to 'postgres'.*
* MAIN_DOMAIN_URL: *This is required to register the public schema on first run. It defaults to 'localhost'.*
* HASURA_SAAS_AUTH_WEBHOOK: *webhook URL for hasura to perform authentication on requests, this URL should just carry the auth server path,
like this ``/api/v1/users/webhook/auth/`` without the domain, since the hasura engine and the django application which serves as the auth server all run on the same machine, in a case where the django application runs on a specific port, then this 
url will be like ``:8000/api/v1/users/webhook/auth/`` where `8000` is the port number*.

**Steps to run**
-----
* **Run django migrations:** ``python manage.py migrate_schemas --shared``. This creates the database relations and the schemas for the tenants.
* **Run django project:** ``python manage.py runserver``
* **Run Docker container to spin up hasura: ``./docker-run.sh``.**
*If you get a permission error trying to run the bash file. * Run ``chmod u+x docker-run.sh``
* By default, graphql API is accessible at `http://<domain>:8080/v1alpha1/graphql`
* You can also register an account on the django app at endpoint `/api/v1/users/` on any of the domains, endpoint collects payload
```json
    {
        "username": "test",
        "first_name": "Test",
        "last_name": "Test",
        "is_tenant": true,
        "password": "mostsecure",
        "subdomain": "test",
        "email": "test@localhost.com",
        "is_superuser": true
    }
```



**Other useful commands*
--
- Create superuser ``./manage.py createsuperuser --username=admin --schema=customer1``. **customer1** here is the schema name.
- Run migrations in parallel when there are many tenants: ``python manage.py migrate_schemas --executor=parallel``
- When you want to execute a normal django command, but targeted at a specific schema, use the `tenant_command`. E.g To load data for *customer1* schema. 
``./manage.py tenant_command loaddata --schema=customer1``.
- List tenants: 
    ```bash
    for t in $(./manage.py list_tenants | cut -f1);
    do
        ./manage.py tenant_command dumpdata --schema=$t --indent=2 auth.user > ${t}_users.json;
    done    
    ```
- Perform tenant post save actions:
    ```python
    from tenant_schemas.signals import post_schema_sync
    from tenant_schemas.models import TenantMixin
    
    def foo_bar(sender, tenant, **kwargs):
        ...
        #This function will run after the tenant is saved, its schema created and synced.
        ...
    
    post_schema_sync.connect(foo_bar, sender=TenantMixin)
    ```
We'd find more [here](https://django-tenant-schemas.readthedocs.io/en/latest/use.html)
