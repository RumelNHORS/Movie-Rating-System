from rest_framework import generics, status
from rest_framework.response import Response
from .models import User, Movie, Rating
from .serializers import UserSerializer, MovieSerializer, RatingSerializer

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class RatingListView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class RatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class AddRatingView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class MovieAverageRatingView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        ratings = instance.rating_set.all()
        if ratings:
            average_rating = sum(rating.rating for rating in ratings) / len(ratings)
            data = {'average_rating': average_rating}
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'No ratings available for this movie.'}, status=status.HTTP_404_NOT_FOUND)
