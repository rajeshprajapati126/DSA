class ArrayStack:

    def __init__(self,size=1000):
        self.stack = [0] * size 
        self.capacity = size 
        self.topIndex = -1
    def push(self,x):

        if (self.topIndex >= (self.capacity -1)) :
            print("Index Overflow")
        self.topIndex += 1
        self.stack[self.topIndex] = x 
    def pop(self):

        if self.topIndex==-1:
            print("No Element in the stack")
            return -1
        pop_ele = self.stack[self.topIndex]
        self.topIndex -= 1
        return pop_ele
    def top(self):
        return self.topIndex
    def empty(self):
        if self.topIndex==-1:
            return True
        return False

stack = ArrayStack()
commands = ["ArrayStack", "push", "push", "top", "pop", "empty"]
inputs = [[], [5], [10], [], [], []]

for i in range(len(commands)):
    if commands[i] == "push":
        stack.push(inputs[i][0])
        print("null", end=" ")
    elif commands[i] == "pop":
        print(stack.pop(), end=" ")
    elif commands[i] == "top":
        print(stack.top(), end=" ")
    elif commands[i] == "empth":
        print("true" if stack.empty() else "false", end=" ")
    elif commands[i] == "ArrayStack":
        print("null", end=" ")