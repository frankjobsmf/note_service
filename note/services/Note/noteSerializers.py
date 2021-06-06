#django rest framework
from rest_framework import serializers

#models
from ...models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'id',
            'user_id',
            'title',
            'content',
            'date'
        )