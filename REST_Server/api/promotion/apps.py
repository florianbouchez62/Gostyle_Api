from django.apps import AppConfig
from django.db.models.signals import post_migrate


class PromotionConfig(AppConfig):
    name = 'promotion'

    def ready(self) -> None:
        import promotion.signals
        from .signals import populate_models
        post_migrate.connect(populate_models, sender=self)
