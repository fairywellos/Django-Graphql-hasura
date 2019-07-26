from django.conf import settings


def generate_client_url(main_domain, subdomain):
    main_domain, port = main_domain.split(":")

    if settings.IS_GAE:
        return f'{subdomain}-dot-{main_domain}'
    return f'{subdomain}.{main_domain}'
