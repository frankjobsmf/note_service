#django urls
from django.urls import path, re_path

#NoteService
from .services.Note.NoteService import (
    #list
    ListNotesByUserId,
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
    #add
    path(
        'notes-userid/id=<int:id>',
        ListNotesByUserId.as_view(),
    ),
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
