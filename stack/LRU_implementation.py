class LRU:
    class Node:
        def __init__(self, _key, _val):
            self.key = _key
            self.val = _val
            self.next = None
            self.prev = None

    def __init__(self, capacity):
        self.cap = capacity
        self.m = {}

        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)

        # 🔥 IMPORTANT FIX
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNode(self, newNode):
        temp = self.head.next
        newNode.next = temp
        newNode.prev = self.head
        self.head.next = newNode
        temp.prev = newNode

    def delNode(self, delNode):
        delPrev = delNode.prev
        delNext = delNode.next
        delPrev.next = delNext
        delNext.prev = delPrev

    def get(self, key):
        if key in self.m:
            resNode = self.m[key]
            res = resNode.val

            self.delNode(resNode)
            self.addNode(resNode)

            self.m[key] = self.head.next
            return res
        return -1

    def put(self, key, val):
        if key in self.m:  
            existingNode = self.m[key]
            self.delNode(existingNode)
            del self.m[key]

        if len(self.m) == self.cap:
            lru_node = self.tail.prev
            self.delNode(lru_node)
            del self.m[lru_node.key]

        newNode = self.Node(key, val)
        self.addNode(newNode)
        self.m[key] = newNode


# Test
l1 = LRU(3)
l1.put(4, 10)
l1.put(5, 15)
l1.put(6, 18)

print(l1.get(6))  
print(l1.get(5))
l1.put(8,12)
l1.put(9,1)
print(l1.get(6))