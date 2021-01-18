class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.prehead = Node(None,None)
        
    def search(self,key):
        p = self.prehead.next
        while p:
            if p.key == key:
                return p
            p = p.next
        return None
    
    def add(self,key,value):
        p = self.search(key)
        if p:
            p.value = value
        else:
            node = Node(key,value)
            self.prehead.next,node.next = node,self.prehead.next
    
    def get(self,key):
        p = self.search(key)
        if p:
            return p.value
        else:
            return None
    
    def remove(self,key):
        prev = self.prehead 
        curr = prev.next
        while curr:
            if curr.key == key:
                break
            curr,prev = curr.next,curr
        if curr:
            prev.next = curr.next
            
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1023
        self.arr = [LinkedList() for _ in range(self.size)]
    
    def _hash(self,key):
        return key % self.size
    
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        h = self._hash(key)
        self.arr[h].add(key,value)
        
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        h = self._hash(key)
        result = self.arr[h].get(key)
        if result is not None:
            return result
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        h = self._hash(key)
        self.arr[h].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)