class HashTable:

    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def add(self, key, value):
        h = self.get_hash(key)
        # self.arr[h] = value
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
        if not found:
            self.arr[h].append((key, value))

    def get(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                return element[1]

    def print_all(self):
        for a in self.arr:
            for b in a:
                print(f"{b[0]}: {b[1]}")

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.add(key, value)

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]


if __name__ == '__main__':
    # ht = HashTable()
    # ht.add('march 6', 130)
    # ht.add('march 7', 135)
    # ht['march 8'] = 140
    # ht['march 17'] = "fds"
    # # print(ht.get_hash("march 17"))
    # print(ht['march 6'])
    # print(ht['march 8'])
    # print(ht['march 17'])
    # print(type(ht['march 17']))
    # print(ht['march 17'])
    wc = HashTable()
    with open("data/poem.txt") as file:
        for line in file:
            words = line.split()
            for word in words:
                if not wc[word]:
                    wc[word] = 0
                    # print(word)
                wc[word] += 1
                # print(type(wc[word]))
    wc.print_all()
