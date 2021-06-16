import sys

# Stack (LIFO) implementation using lists 
class Stack:
    # Initiliazing an empty stack
    def __init__(self):
        self.stack = []
    
    # Pushing elements to the stack
    def push(self,data):
        self.stack.append(data)

    # Popping / Removing element
    def pop(self):
        if(not self.isEmpty()):
            self.stack.pop()
    
    # Check whether stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    def peek(self):
        if(not self.isEmpty()):
            return self.stack[len(self.stack)-1]
        return -1




# Method to validate Well Formed Formula
def validateString(input):
    brackets = Stack()

    # Possilbe bracket types
    open_brackets = ['(','{','[']
    close_brackets = [')','}',']']

    
    # Iterating over each character in the input string
    for char in input:
        if(char in open_brackets):
            isValid = True 
            brackets.push(char)
        elif(char in close_brackets):
            isValid = True

            # Cross comparing the closed bracket with the relevant open brack
            if(open_brackets[close_brackets.index(char)] == brackets.peek()):
                brackets.pop()
            else:
                return False
    
    # Returns True if its a WFF 
    return brackets.isEmpty() 
        


# Main method
if __name__ == '__main__':

    # User input
    inp = input("Enter string: ")

    # Calling method to validate WFF input
    result = validateString(inp)

    if(result):
        print("TEST_PASS")
    else:
        print("TEST_FAIL")



    