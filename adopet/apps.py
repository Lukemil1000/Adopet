from django.apps import AppConfig


class AdopetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'adopet'

    def ready(self) -> None:
        from adopet import signals
