from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, Serializer, IntegerField, CharField, BooleanField, ChoiceField, ReadOnlyField, PrimaryKeyRelatedField
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(ModelSerializer):
    owner = ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'owner', 'style')


class UserSerializer(ModelSerializer):
    snippets = PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
