class MyHashMap:

    def __init__(self):
      self.hashmap = []
        

    def put(self, key: int, value: int) -> None:
        print('Looking to put kvp', key, value, 'in ', self.hashmap)

        index = 0        
        for kvp in self.hashmap:
            if kvp[0] == key:
                print('\tFound an existing kvp, removing')
                self.hashmap.pop(index)
            
            index += 1

        self.hashmap.append([key, value])
        print('\tAppended, current hashmap value: ', self.hashmap)

    def get(self, key: int) -> int:
        print('Looking to get key', key, 'in ', self.hashmap)
        if len(self.hashmap) == 0:
            return -1

        index = 0        
        for kvp in self.hashmap:
            print('\tlookin at kvp: ', kvp, ' for key: ', key)
            if kvp[0] == key:
                print('\t\tFound, returning value: ', self.hashmap[index][1])
                return self.hashmap[index][1]
            index += 1

        print('\tNo match found, returning -1')
        return -1 # no match

    def remove(self, key: int) -> None:
        print('Looking to remove key', key, 'in ', self.hashmap)

        index = 0    
        for kvp in self.hashmap:
            if kvp[0] == key:
                print('\tFound match: ', kvp, '. Removing')
                self.hashmap.pop(index)
                return

            index += 1

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)