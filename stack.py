class Stack(list):
    def is_empty(self):
        "Check if the stack is empty."
        return len(self) == 0
    
    def push(self, item):
        "Add an element to the top of the stack."
        self.append(item)

    def pop(self):
        "Remove and return the top element of the stack."
        if not self.is_empty():
            _item = self[-1]
            self.__delitem__(-1)
        return _item
    
    def peek(self):
        "Return the top element of the stack without removing it."
        if not self.is_empty():
            return self[-1]
        
    def size(self):
        "Return the number of elements in the stack."
        return len(self)