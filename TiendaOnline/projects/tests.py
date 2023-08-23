from django.test import TestCase

# Create your tests here.
from rest_framework.generics import CreateAPIView

class TestCreateApiView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
     