'''
1. Stack: Implement Stack Using a List ( ** Interview Question)
In the Stack: Intro video we discussed how stacks are commonly implemented using a list instead of a linked list.

Create a constructor for Class Stack that implements a new stack with an empty list called stack_list.'''

'''
2. Stack: Push for Stack That Uses List ( ** Interview Question)
Add a method to push a value onto the Stack implementation that we began in the last Coding Exercise.

Remember: This Stack implementation uses a list instead of a linked list.'''

'''
3. Stack: Pop for Stack That Uses List ( ** Interview Question)
Add a method to pop a value from the Stack implementation that we began in the last two Coding Exercises.

Remember: This Stack implementation uses a list instead of a linked list.'''

'''
4. Stack: Parentheses Balanced ( ** Interview Question)
Check to see if a string of parentheses is balanced or not.

By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in the correct order. 
For example, the string "((()))" has three pairs of balanced parentheses, so it is a balanced string. On the other hand,
the string "(()))" has an imbalance, as the last two parentheses do not match, so it is not balanced.  
Also, the string ")(" is not balanced because the close parenthesis needs to follow the open parenthesis.

Your program should take a string of parentheses as input and return True if it is balanced, or False if it is not. 
In order to solve this problem, use a Stack data structure.

Function name:
is_balanced_parentheses

Remember: this is not a method within the Stack class, this is a separate function.  Indent all the way to the left.'''


class Stack:
    # 1. WRITE CONSTRUCTOR THAT IMPLEMENTS STACK WITH EMPTY LIST #
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    # 2. WRITE PUSH METHOD HERE #
    def push(self, value):
        self.stack_list.append(value)

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    # 3. WRITE POP METHOD HERE #

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.stack_list.pop()


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

my_stack.print_stack()

"""
    EXPECTED OUTPUT:
    ----------------
    3 
    2
    1

"""

print("Stack before pop():")
my_stack.print_stack()

print("\nPopped node:")
print(my_stack.pop())

print("\nStack after pop():")
my_stack.print_stack()

"""
    EXPECTED OUTPUT:
    ----------------
    Stack before pop():
    3
    2
    1

    Popped node:
    3

    Stack after pop():
    2
    1

"""