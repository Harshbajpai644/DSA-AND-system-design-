import random

class RandomizedSet:

    def __init__(self):
        self.num_to_index = {}
        self.num_list = []

    def insert(self, val: int) -> bool:
        if val in self.num_to_index:
            return False
        
        self.num_to_index[val] = len(self.num_list)
        self.num_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_to_index:
            return False
        
        idx_to_remove = self.num_to_index[val]
        last_element = self.num_list[-1]
        
        self.num_list[idx_to_remove] = last_element
        self.num_to_index[last_element] = idx_to_remove
        
        self.num_list.pop()
        del self.num_to_index[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.num_list)
