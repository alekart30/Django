from django.conf.urls import url, include
from .models import Person
from rest_framework import routers, serializers, viewsets

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

router = routers.DefaultRouter()
router.register(r'persons', PersonViewSet)
urlpatterns = [ url(r'^', include(router.urls)),url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework'))
]
