import heapq

class Node:
    def __init__(self, freq, symbol):
        self.freq = freq
        self.symbol = symbol
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(chars, freq):
    nodes = [Node(freq[i], chars[i]) for i in range(len(chars))]
    heapq.heapify(nodes)

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        combined = Node(left.freq + right.freq, left.symbol + right.symbol)
        combined.left, combined.right = left, right
        heapq.heappush(nodes, combined)

    return nodes[0]

def print_huffman_codes(node, val=''):
    if not node:
        return
    if not node.left and not node.right:
        print(f"{node.symbol} -> {val}")
    print_huffman_codes(node.left, val + "0")
    print_huffman_codes(node.right, val + "1")

if __name__ == "__main__":
    instr=input("Enter strings with spaces: ")
    chars=instr.split()
    freqin=input("Enter corresponding frequencies: ")
    freq = freqin.split()
    print(chars)
    print(freq)
    root = build_huffman_tree(chars, freq)
    print_huffman_codes(root)
