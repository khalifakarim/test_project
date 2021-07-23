class SoftDeleteMixin:

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class SerializerChooseMixin:
    read_only_serializer = None
    write_serializer = None

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "list":
            return self.read_only_serializer
        return self.write_serializer
