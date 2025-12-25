import sys

sys.path.extend(['../'])
from graph import tools

num_node = 18
self_link = [(i, i) for i in range(num_node)]
inward = [(0, 17), (17, 7), (7, 8), (9, 8), (10, 9), (14, 8), (15, 14),
          (16, 15), (11, 8), (12, 11), (13, 12), (1, 0), (2, 1), (3, 1), 
          (4, 0), (5, 4), (6, 5)]
outward = [(j, i) for (i, j) in inward]
neighbor = inward + outward

class Graph:
    def __init__(self, labeling_mode='spatial'):
        self.A = self.get_adjacency_matrix(labeling_mode)
        self.num_node = num_node
        self.self_link = self_link
        self.inward = inward
        self.outward = outward
        self.neighbor = neighbor

    def get_adjacency_matrix(self, labeling_mode=None):
        if labeling_mode is None:
            return self.A
        if labeling_mode == 'spatial':
            A = tools.get_spatial_graph(num_node, self_link, inward, outward)
        else:
            raise ValueError()
        return A


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import os

    # os.environ['DISPLAY'] = 'localhost:11.0'
    A = Graph('spatial').get_adjacency_matrix()
    for i in A:
        plt.imshow(i, cmap='gray')
        plt.show()
    print(A)
