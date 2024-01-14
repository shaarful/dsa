class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print(self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)

        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start not in self.graph_dict:
            return None
        if start == end:
            return path

        shorted_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
            if sp:
                if shorted_path is None or len(sp) < len(shorted_path):
                    shorted_path = sp
        return shorted_path


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    start = 'Mumbai'
    end = 'New York'
    route_graph = Graph(routes)
    print(route_graph.get_paths(start, end))
    print(route_graph.get_shortest_path(start, end))
