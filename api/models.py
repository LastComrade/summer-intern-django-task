from django.db import models


class Graph(models.Model):
    src_node = models.TextField()
    dest_node = models.TextField()
    edge = models.IntegerField()
    graph_id = models.IntegerField()

    def __str__(self):
        return self.src_node + "--" + str(self.edge) + "--" + self.dest_node + " -> (" + str(self.graph_id) + ")"
