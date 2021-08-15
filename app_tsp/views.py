from django.shortcuts import render
from .models import TravellingSalesmanProblem
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from pathlib import Path
# Create your views here.

BASE_DIR = Path(__file__).resolve().parent.parent

# def index(request):
#     length = False
#     graph = {(1, 2): 10, (2, 3): 35, (3, 1): 15, (3, 4): 30, (1, 4): 20, (2, 4): 25}
#     travel_sales = TravellingSalesmanProblem()
#     nodes, min_dist, fastest_route = travel_sales.TSP(graph, starting_point=1)
#     # travel_sales.plotGraph(graph)
#     # plt.savefig(os.path.join(BASE_DIR, 'static/images')+'/mainGraph.jpg')
#     # graphimg = 'mainGraph.jpeg'
#     if len(fastest_route) > 1:
#         length = True
#     return render(request, "index.html", {'min_dist': min_dist, 'fastest_route': fastest_route, 'length': length, 'graphimg': graphimg})

def index(request):
    # number_nodes = request.POST.get('nodes_num')
    # print(number_nodes)
    return render(request, "index.html")
#
# def add(request):
#     tot_nodes = int(request.GET['nodes_num'])
#     travel_sales = TravellingSalesmanProblem()
#     nodes = travel_sales.create_nodes(tot_nodes)
#     combs = travel_sales.create_combs(tot_nodes)
#     # if form.is_valid():
#     #     print(form)
#     #     # for field in form:
#     #     #     print(field.value())
#     # print(request.POST.get('id_field'))
#     return render(request, "input_index.html", {'nodes':nodes, 'combs':combs})

def result(request):

    tot_nodes = int(request.POST['nodes_num'])
    dist = request.POST['dist']
    distance = [int(i) for i in dist.split(",")]
    travel_sales = TravellingSalesmanProblem()
    combs = travel_sales.create_combs(tot_nodes)
    graph = travel_sales.make_graph(combs, distance)
    nodes, min_dist, fastest_route = travel_sales.TSP(graph, starting_point=1)
    travel_sales.plotGraph(graph)
    plt.savefig(os.path.join(BASE_DIR, 'static/images')+'/mainGraph.jpg')
    graphimg = 'mainGraph.jpg'
    return render(request, "result.html", {'min_dist': min_dist, 'fastest_route': fastest_route, 'graphimg': graphimg, 'nodes': nodes})

