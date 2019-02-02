**How to setup this project**
----------

This short doc assumes you have docker installed on your computer.
If you do not have, [Install](https://docs.docker.com/get-started/) here.

**Compulsory environmental variables**
* HASURA_SAAS_DATABASE: *This is the postgres database name you want to you, assumes you have the database created.*
* HASURA_SAAS_USER: *This is the postgres user name.*
* HASURA_SAAS_PASSWORD: *This is the postgres user password*


**Steps to run**
-----
* **Run django migrations:** ``python manage.py migrate_schemas --shared``. This creates the database relations and the schemas for the tenants.
* **Run django project:** ``python manage.py runserver``
* **Run Docker container to spin up hasura: ``./docker-run.sh``.**
*If you get a permission error trying to run the bash file. * Run ``chmod u+x docker-run.sh``



**Other useful commands*
--
- Create superuser ``./manage.py createsuperuser --username=admin --schema=customer1``. **customer1** here is the schema name.
- Run migrations in parallel when there are many tenants: ``python manage.py migrate_schemas --executor=parallel``
- When you want to execute a normal django command, but targeted at a specific schema, use the `tenant_command`. E.g To load data for *customer1* schema. 
``./manage.py tenant_command loaddata --schema=customer1``.
- List tenants: 
    ```
    for t in $(./manage.py list_tenants | cut -f1);
    do
        ./manage.py tenant_command dumpdata --schema=$t --indent=2 auth.user > ${t}_users.json;
    done    
    ```
- Perform tenant post save actions:
    ```
    from tenant_schemas.signals import post_schema_sync
    from tenant_schemas.models import TenantMixin
    
    def foo_bar(sender, tenant, **kwargs):
        ...
        #This function will run after the tenant is saved, its schema created and synced.
        ...
    
    post_schema_sync.connect(foo_bar, sender=TenantMixin)
    ```
We'd find more [here](https://django-tenant-schemas.readthedocs.io/en/latest/use.html)
