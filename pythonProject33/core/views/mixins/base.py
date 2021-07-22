class SoftDeleteMixin:

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
