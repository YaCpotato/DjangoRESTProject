from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from shop.models import TsunList
from shop.models import User
from .serializers import TsunListSerializer
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """CRUDをおこなうAPI"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TsunListViewSet(viewsets.ModelViewSet):

    queryset = TsunList.objects.all()
    serializer_class = TsunListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

  #  def getAllTsunList():
   #     queryset = TsunList.objects.all()
   #     serializer = TsunListSerializer(queryset, many=True)
   #     return serializer.data

