
""" implementation of stack """
from sys import argv


class Stack:

    def __init__(self):
        self._stack = []

    def isEmpty(self):
        if not self._stack:
            return True
        return False

    def push(self, item):
        self._stack.append(item)
        print(f"{self._stack}")

    def pop(self):
        self._popped=self._stack[-1]
        self._stack.remove(self._stack[-1])
        return self._popped

    def print_items(self):
        for item in self._stack:
            print(item)


class main_class:

    def main_function(self):
        print("""
            Welcome to stack class-
            Press 1. Push item
            Press 2. Pop item
            Press 3. To check if it is empty
            Press 4. Print items
            Press anything else to exit
            """)
        s=Stack()
        flag=True
        while flag:
            inputs=input()
            if(inputs=='1'):
                print("Enter item to be pushed")
                _new=input()
                s.push(_new)
            elif(inputs=='2'):
                var=s.pop()
                print("Item"+str(var)+"popped")
            elif(inputs=='3'):
                print(s.isEmpty())
            elif(inputs=='4'):
                s.print_items()
            else:
                flag=False
