import sys
import heapq

class Vertex(object):

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacentList = sys.maxsize

    def __cmp__(self, othervertex):
        return self.cmp(self.minDistance, otherVertex.minDistance)

    def __it__(self, other):
        selfPriority = self.minDistance
        otherPriority = other.minDistance
        return selfPriority < otherPriority

class Edge(object):

    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

def calculateShortestPath(self, vertexList, startVertex):
    heap = []
    startVertex.minDistance = 0
    heapq.heappush(heap, startVertex)

    while len(queue)>0:
        actualVertex = heapq.heappop(queue)

        for edge in actualVertex.adjacentList:
            u = edge.startVertex
            v = edge.targetVertex
            newDistance = u.minDistance + edge.weight

            if newDistance < v.minDistance:
                v.predecessor = u
                v.minDistance = newDistance
                heapq.heappush(queue, v)

def getShortestPath(self, targetVertex):
    print("Shortest Path to target is: {}",format(targetVertex.minDistance))

    node = targetVertex

    while node is not None:
        print(node.name+"->")
        node = node.predecessor

node1 = Vertex('A')
node2 = Vertex('B')
node3 = Vertex('C')

edge1 = Edge(1, node1, node2)
edge2 = Edge(1, node2, node3)
edge3 = Edge(10, node1, node3)

node1.adjacentList.append(edge1)
node2.adjacentList.append(edge2)
node3.adjacentList.append(edge3)

vertexList = (node1, node2, node3)

calculateShortestPath(vertexList, node1)
getShortestPath(node3)