from django.conf import settings


def global_settings(request):
    # return any necessary values
    return {
        # Extend this with all settings constants that should be accessible in templates
        # 'BASE_DIR': settings.BASE_DIR
    }