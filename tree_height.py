# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    height = n*[-1]
    
    def augstums(node):
        if height[node] != -1:
            return height[node]
        if parents[node] == -1:
             height[node] = 1
        else:
             height[node] = augstums(parents[node])+1
        return  height[node]
   
    max_height = 0
    
    for root in range(n):
        max_height = max(max_height,augstums(root))
    return max_height


def main():
    teksts=input("I or F: ")
    if "I" in teksts:
       n=int(input())
       parents=list(map(int, input().split()))
    elif "F" in teksts:
        filename = input()
        tests ='./test/'
        file = tests+filename
        if "a" not in filename:
            try:
                with open(file) as x:
                    n=int(x.readline())
                    parents=list(map(int,x.readline().split()))
            except Exception as y:
                print("Error",str(y))
                return
        else:
            print("Error")
            return    
        
    print(compute_height(n,parents))    
    
    
   
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
