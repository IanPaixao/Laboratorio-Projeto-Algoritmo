
import sys
from pythonds.basic.stack import Stack

'''
The followng method change the infix way of reading the sentence to postfix way of reading
'''
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "abcdefghijklmnopqrstuvwxyz"or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)
pass


class Node:
  # Constructor
  def __init__(self, values):
    self.values = values
    self.left = None
    self.right = None
  pass
pass

def isOperador(val):
  if (val == '+' or val == '-' or val == '*' or val == '/' or val == '^'):
    return True
  else:
    return False
pass

"""
the following method will print the generated tree

"""
def treePrint(root):
  thislevel = [root]
  i = 0
  while thislevel:
    nextlevel = list()

    """
    Given a level search for elements in the tree
    """
    array = []
    for n in thislevel:
      array.append(n.values)
      if n.left: nextlevel.append(n.left)
      if n.right: nextlevel.append(n.right)
      thislevel = nextlevel
    pass

    temp = "Nivel "+str(i)+": "

    sys.stdout.write(temp)
    for x in range (len(array)):
      sys.stdout.write(str(array[x]))
    print('')
    del array[:]
    i = i + 1

"""
Insert postfix sentence into the tree
"""
def insert(sentence):
  stack = []

  for char in sentence:
    if not isOperador(char):
      # if what you found was not an operator create a root node and add it to the stack
      root = Node(char)
      stack.append(root)
    else:
      # else
      root = Node(char)
      # Remove the elements that follows the operator
      node1 = stack.pop()
      node2 = stack.pop()
      # Connect the elements to the operator
      root.right = node1
      root.left = node2
      # Finally add it  in the stack
      stack.append(root)
    pass
  pass
  aws = stack.pop()
  return aws
pass

def main():

  for statementsin sys.stdin:
      statements = input()
      statements = infixToPostfix(statements)
       statements = statements.replace(" ","")
      Tree = insert(statements)
      treePrint(Tree)
main()





