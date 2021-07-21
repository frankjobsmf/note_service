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
    #list notes by id user
    path(
        'notes-userid/id=<id>',
        ListNotesByUserId.as_view(),
    ),
    #list note by id 
    path(
        'note-id/id=<id>',
        ListNoteById.as_view(),
    ),
    #add
    path(
        'add',
        AddNote.as_view(),
    ),
    #update
    path(
        'update/id=<id>',
        UpdateNote.as_view(),
    ),
    #delete
    path(
        'delete/id=<id>',
        DeleteNote.as_view(),
    ),
]
