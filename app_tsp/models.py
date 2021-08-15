from django.db import models

# Create your models here.
from itertools import permutations
import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations

class TravellingSalesmanProblem:
    # def __init__(self):#, graph, starting_point=1):
    #     # self.graph = graph
    #     # self.starting_point = starting_point
    def create_nodes(self, nodes_num):
        nodes = [i for i in range(1, nodes_num+1)]
        return nodes
    def create_combs(self, nodes_num):
        combs = [per for per in combinations(range(1,nodes_num + 1), 2)]
        return combs

    def make_graph(self, combs, distances):
        graph = {}
        for i,j in zip(combs, distances):
            graph[i] = j
        return graph

    def TSP(self, graph, starting_point=1):
        self.graph = graph
        self.starting_point = starting_point

        temp = list(zip(*graph.keys()))
        nodes = list(set(temp[0] + temp[1]))
        other_nodes = nodes.copy()
        other_nodes.remove(starting_point)

        other_combs = [per for per in permutations(other_nodes, len(other_nodes))]
        all_path = []
        for combs in other_combs:
            temp_path = [starting_point]
            for ele in combs:
                temp_path.append(ele)
            temp_path.append(starting_point)
            all_path.append(list(zip(temp_path, temp_path[1:])))

        dist_path = {}
        for path in all_path:
            dist = 0
            for n in path:
                if n in graph.keys() or n[::-1] in graph.keys():
                    try:
                        dist += graph[n]
                    except:
                        dist += graph[n[::-1]]
            dist_path[tuple(path)] = dist

        min_dist = min(dist_path.values())
        opt_path = []
        for k, v in dist_path.items():
            if v == min_dist:
                new_temp = list(dict.fromkeys(list(sum(k, ()))))
                new_temp.append(starting_point)
                opt_path.append(new_temp)
        try:
            if min_dist == 0:
                raise Exception("Distance is 0")
        except Exception:
            print("Total Distance is 0. Please check the distances between nodes and retry.")
        else:
            return nodes, min_dist, opt_path

    def plotGraph(self, graph):

        """
        Plots the graph of nodes and edges of the Travelling Salesman problem with given data
        :param data: dict, Data to be plotted
        :return plot: fig, Plot of the updated graph
            nodes: list, list of all the nodes in the given data
            edges: list, List of all edges in the given data
        """

        if not type(graph) is dict:
            raise TypeError("Input should be a dictionay of nodes and distances")

        nodes = []
        edges = []
        G = nx.Graph()
        G.clear()
        temp = list(zip(*graph.keys()))
        nodes = list(set(temp[0] + temp[1]))
        edges = list(graph.keys())

        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        # labels = {(1,2):10, (2,3):35, (3,1): 15, (3,4): 30, (1,4): 20, (2,4): 25}
        pos = nx.random_layout(G, seed=123)
        # plt.figure()
        nx.draw(G, pos, with_labels=True, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=self.graph, font_size=10)

        # nx.draw(G, with_labels=True,font_weight='bold')
        return plt

    def node_check(self, node):

        temp = list(zip(*self.graph.keys()))
        nodes = list(set(temp[0] + temp[1]))
        if node in nodes:
            print(f"{node} already exits! Please enter other node.")
            return False
        else:
            return True

    def add_node(self,current_graph, new_node):
        temp = list(zip(*current_graph.keys()))
        nodes = list(set(temp[0] + temp[1]))
        for i in range(len(nodes)):
            inner_check = False
            while not inner_check:
                try:
                    if nodes[i] != new_node:
                        new_dist = int(input(f"Enter distance from {nodes[i]} to {new_node}: "))
                except ValueError:
                    print("Enter distance of type int")
                else:
                    current_graph[nodes[i], new_node] = new_dist
                    inner_check = True

        temp = list(zip(*current_graph.keys()))
        updated_nodes = list(set(temp[0] + temp[1]))
        return current_graph, updated_nodes

    def delete_node(self, del_choice, graph, nodes):
        # if len(nodes) > 2:
        updated_graph = dict([(k,v) for k,v in graph.items() if del_choice not in k])
        nodes.remove(del_choice)
        return updated_graph, nodes
        # else:
        #     print("Need at least two nodes to calculate distance!")
