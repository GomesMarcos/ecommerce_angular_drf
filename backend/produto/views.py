from rest_framework import viewsets
from .models import *
from .serializers import *

class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutosSerializer