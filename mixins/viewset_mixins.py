class SerializerClassesMixin:
    RETRIEVE = None
    LIST = None

    def set_serializers(self):
        serializer_classes = {
            'list': self.LIST,
            'retrieve': self.RETRIEVE
        }
        return serializer_classes

    def get_serializer_class(self):
        return self.set_serializers().get(self.action, self.set_serializers()['retrieve'])

