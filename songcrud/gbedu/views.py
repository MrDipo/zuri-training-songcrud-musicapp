from rest_framework import viewsets
from musicapp.models import Artiste, Song, Lyric
from gbedu.serializers import ArtisteSerializer, SongSerializer, LyricSerializer


# @api_view(['GET'])
# def gbeduOverview(request):
#     api_urls = {
#         'all_artistes': '/',
#         'Search by Artiste': '/?category=category_name',
#         'Search by Song': '/?subcategory=category_name',
#         'Add': '/create',
#         'Update': '/update/pk',
#         'Delete': '/artiste/pk/delete'
#     }
  
#     return Response(api_urls)


# @api_view(['POST'])
# def add_artistes(request):
#     artiste = ArtisteSerializer(data=request.data)
  
#     # validating for already existing data
#     if Artiste.objects.filter(**request.data).exists():
#         raise serializers.ValidationError('This data already exists')
  
#     if artiste.is_valid():
#         artiste.save()
#         return Response(artiste.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)



# @api_view(['GET'])
# def view_artistes(request):
    
#    # checking for the parameters from the URL
#    if request.query_params:
#       artistes = Artiste.objects.filter(**request.query_param.dict())
#    else:
#       artistes = Artiste.objects.all()
#    serializer = ArtisteSerializer(artistes, many=True)
  
#    # if there is something in artistes else raise error
#    if artistes:
#       return Response(serializer.data)
#    else:
#       return Response(status=status.HTTP_404_NOT_FOUND)



# @api_view(['POST'])
# def update_artistes(request, pk):
#    artiste = Artiste.objects.get(pk=pk)
#    data = ArtisteSerializer(instance=artiste, data=request.data)
  
#    if data.is_valid():
#       data.save()
#       return Response(data.data)
#    else:
#       return Response(status=status.HTTP_404_NOT_FOUND)

class ArtisteViewSet(viewsets.ModelViewSet):
   queryset = Artiste.objects.all()
   serializer_class = ArtisteSerializer


class SongViewSet(viewsets.ModelViewSet):
   queryset = Song.objects.all()
   serializer_class = SongSerializer


class LyricViewSet(viewsets.ModelViewSet):
   queryset = Lyric.objects.all()
   serializer_class = LyricSerializer