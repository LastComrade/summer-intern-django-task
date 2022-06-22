from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('graph-list', views.GraphList, name='graph-list'),
    path('graph-detail/<int:gid>', views.GraphDetail, name='graph-detail'),
    path('graph-delete/<int:gid>', views.DeleteGraph, name='graph-delete'),
    path('edge-detail/<int:eid>', views.EdgeDetail, name='edge-detail'),
    path('edge-create', views.CreateEdge, name='edge-create'),
    path('edge-update/<int:eid>', views.UpdateEdge, name='edge-update'),
    path('edge-delete/<int:eid>', views.DeleteEdge, name='edge-delete'),
]
