import sys

class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):

        if self.stack_list:
            return self.stack_list.pop()

        else:
            return -1


    def size(self):

        return len(self.stack_list)

    def empty(self):
        if len(self.stack_list) == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.stack_list:
            return self.stack_list[-1]

        else:
            return -1

stack = Stack()

N = int(input())

for i in range(N):
    command = sys.stdin.readline().rstrip()
    if command in ['pop', 'size', 'empty', 'top']:
        print(getattr(stack, command)())
    else:
        command, push_value = command.split()
        getattr(stack, command)(push_value)