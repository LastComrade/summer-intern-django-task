from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Graph
from .serializers import GraphSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/graph-list/',
        'Detail View': '/graph-detail/<int:id>',
        'Create': '/graph-create/',
        'Update': '/graph-update/<int:id>',
        'Delete': '/graph-delete/<int:id>',
    }

    return Response(api_urls)


@api_view(['GET'])
def GraphList(request):
    graphs = Graph.objects.all()
    serializer = GraphSerializer(graphs, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def GraphDetail(request, gid):
    if Graph.objects.filter(graph_id=gid).exists():
        graph = Graph.objects.filter(graph_id=gid)
        serializer = GraphSerializer(graph, many=True)
        return Response(serializer.data)
    else:
        return Response("Graph with this id does not exists")


@api_view(['GET'])
def DeleteGraph(request, gid):
    if Graph.objects.filter(graph_id=gid).exists():
        graph = Graph.objects.filter(graph_id=gid)
        graph.delete()
        return Response("Graph is deleted")
    else:
        return Response("Graph with this id does not exists")


@api_view(['GET'])
def EdgeDetail(request, eid):
    if Graph.objects.filter(id=eid).exists():
        edge = Graph.objects.filter(id=eid)
        serializer = GraphSerializer(edge, many=True)
        return Response(serializer.data)
    else:
        return Response("Edge with this id does not exists")


@api_view(['POST'])
def CreateEdge(request):
    serializer = GraphSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("Entered edge data is not valid")


@api_view(['POST'])
def UpdateEdge(request, eid):
    if Graph.objects.filter(id=eid).exists():
        graph = Graph.objects.get(id=eid)
        serializer = GraphSerializer(instance=graph, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    else:
        return Response("Edge with this id does not exists")


@api_view(['GET'])
def DeleteEdge(request, eid):
    if Graph.objects.filter(id=eid).exists():
        edge = Graph.objects.get(id=eid)
        edge.delete()
        return Response("Edge is deleted")
    else:
        return Response("Edge with this id does not exists")
