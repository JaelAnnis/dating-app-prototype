from django.apps import AppConfig


class UnmaskConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'UnMask'

    def ready(self):
        import UnMask.signals