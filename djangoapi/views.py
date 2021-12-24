from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.renderers import JSONRenderer


class MovieListView(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

