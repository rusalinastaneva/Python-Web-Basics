from django.urls import path

from testing_app.views.index import index
from testing_app.views.query_params import query_params_view

urlpatterns = [
    path('', index, name='profiles'),
    path('query_params/', query_params_view, name='query_params'),
]