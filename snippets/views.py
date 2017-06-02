from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class SnippetList(ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
