#django urls
from django.urls import path, re_path

#NoteService
from .services.Note.NoteService import (
    #list notes by id user
    ListNotesByUserId,
    #list nots by id
    ListNoteById,
    #add
    AddNote,
    #update
    UpdateNote,
    #delete
    DeleteNote,
)

urlpatterns = [
    #list
    # re_path(
    #     r'^notes-userid/(?P<id>[0-9])$',
    #     ListNotesByUserId.as_view(),
    # ),

    #list notes by id user
    path(
        'notes-userid/id=<int:id>',
        ListNotesByUserId.as_view(),
    ),
    #list note by id 
    path(
        'note-id/id=<int:id>',
        ListNoteById.as_view(),
    ),
    #add
    path(
        'add',
        AddNote.as_view(),
    ),
    #update
    path(
        'update/id=<int:id>',
        UpdateNote.as_view(),
    ),
    #delete
    path(
        'delete/id=<int:id>',
        DeleteNote.as_view(),
    ),
]
