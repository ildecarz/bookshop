from django.urls import path
from .views import BookListView, AuthorListView, LibraryListView
from .api_views import *

urlpatterns = [
    path('book/', BookListView.as_view(), name = 'book-view' ),
    path('author/', AuthorListView.as_view(), name = 'author-view' ),
    path('library/', LibraryListView.as_view(), name = 'library-view' ),
    # API VIEWS
    path('api/library/', LibraryCreateAPIView.as_view(), name = 'library-create-api-view'),
    path('api/library/<int:pk>', LibraryRetrieveUpdateAPIView.as_view(), name = 'library-update-api-view'),
    path('api/book/', BookCreateAPIView.as_view(), name = 'book-create-api-view'),
    path('api/book/<int:pk>', BookRetrieveUpdateAPIView.as_view(), name = 'book-update-api-view'),
    path('api/author/', AuthorCreateAPIView.as_view(), name = 'author-create-api-view'),
    path('api/author/<int:pk>', AuthorRetrieveUpdateAPIView.as_view(), name = 'author-update-api-view'),
    path('api/lead/', LeadsCreateAPIView.as_view(), name = 'leads-api-view'),
]
