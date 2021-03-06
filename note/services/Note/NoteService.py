#python
from datetime import datetime
now = datetime.now()

#rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#models
from ...models import Note

#serializers
from .noteSerializers import (
    NoteSerializer
)

#list
class ListNotesByUserId(APIView):

    def get(self, request, id, *args, **kwargs):
        
        notes_get = Note.objects.filter(
            user_id=id
        )
        
        notes = NoteSerializer(notes_get, many=True)
        
        return Response({
            "notes": notes.data,
            "status_code": status.HTTP_200_OK
        })

class ListNoteById(APIView):
    def get(self, request, id, *args, **kwargs):
        
        try:
            note_get = Note.objects.get(id=str(id))

            note = NoteSerializer( note_get )

            return Response({
                "note": note.data,
                "status_code": status.HTTP_200_OK
            })

        except:
            return Response({
                "note": "Nota no existe",
                "status_code": status.HTTP_404_NOT_FOUND
            })


#add
class AddNote(APIView):
    def post(self, request, *args, **kwargs):
        
        note_post = self.request.data['note_dict']
        
        Note.objects.create(
            user_id=note_post['user_id'],
            title=note_post['title'],
            content=note_post['content'],
            date=note_post['date']
        )

        note = NoteSerializer(note_post)
        
        return Response({
            "message": note.data,
            "status_code": status.HTTP_201_CREATED
        })
        
#update
class UpdateNote(APIView):
    
    def put(self, request, *args, **kwargs):
    
        #buscamos la nota por su id para luego actualizar la nota
        note = Note.objects.get(id=str(kwargs['id']))

        note_put = self.request.data['note_dict']
        
        #entregamos los parametros necesarios
        note.title = note_put['title']
        note.content = note_put['content']
        
        #guardamos
        note.save()
        
        return Response({
            "message": "Nota actualizada con exito",
            "status_code": status.HTTP_200_OK
        })
        
#delete
class DeleteNote(APIView):
    
    def delete(self, request, *args, **kwargs):
    
        #buscamos la nota por su id para luego actualizar la nota
        note_delete = Note.objects.get(id=str(kwargs['id']))
        
        #eliminamos
        note_delete.delete()
        
        return Response({
            "message": "Nota eliminada con exito",
            "status_code": status.HTTP_204_NO_CONTENT
        })