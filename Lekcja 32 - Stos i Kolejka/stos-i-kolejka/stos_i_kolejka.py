# STOS
# - elementy ponumerowane (w określonej kolejności)
# - LIFO (Last In First Out)
# - np. historia przeglądnia


# - dodawanie na stos [+]
# - zdejmowanie ze stosu [+]
# - co jest na wierzchu? []
# - czy stos jest pusty? [+]
# - rozmiar stosu? [+]

class Stack(): 
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            self.stack.pop() # domyłsnie usuwa ostatni

    def is_empty(self):
        return len(self.stack) == 0 # True/False
    
    def size(self):
        return len(self.stack)

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

# [1,  2,  56]
# 0    1    2
# -3  -2   -1

stos = Stack()

stos.push('A') # pomarancz
stos.push('B') # fiolet
stos.push('C') # niebieski

print(stos.peek()) # C

stos.pop()

print(stos.peek()) # B
print(stos.size()) # 2
print(stos.is_empty()) # False



# KOLEJKA
# - elementy ponumerowane (w określonej kolejności)
# - FIFO (First In First Out)
# np. kolejka dokumnetów do druku

# - dodawanie na koniec kolejki [+]
# - usuwanie z początku [+]
# - co jest na początku? [+]
# - czy jest pusta? [+]
# - rozmiar kolejki [+]

class Queue():
    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)

    def size(self):
        return len(self.queue)
    
    def delete(self):
        if self.is_empty() == False:
            return self.queue.pop(0)
        
    def is_empty(self):
        return len(self.queue) == 0 # True/False
    
    def peek(self):
        # if self.is_empty():
        #     pass
        # else:
        #     return self.queue[0]
        if not self.is_empty():
            return self.queue[0]


print("Kolejka:")
kolejka = Queue()
kolejka.add("Andrzej")
kolejka.add("Hania")
kolejka.add("Ignacy")

print(kolejka.peek()) # Andrzej
print(kolejka.delete())
print(kolejka.peek()) # Hania
print(kolejka.is_empty()) # False
print(kolejka.size()) # 2