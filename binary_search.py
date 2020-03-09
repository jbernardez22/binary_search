#!/bin/python3

def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    HINT: 
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    left = 0
    right  = len(xs)-1
    if(xs==[]):
        return None
    def go(left, right):
        mid = (left+right)//2
        if(left==right):
            if(xs[right]<0):
                return None 
        if 0 < xs[mid]:
            right = mid
        if 0 >= xs[mid]:
            left = mid+1
        if mid == 0:
            if xs[mid]>0:
                return mid
        if 0 >= xs[mid-1] and xs[mid]>0 :
            return mid
        return go(left, right)
    return go(left, right)
#print(find_smallest_positive([0, 1, 2, 3]))
#print(find_smallest_positive([-3, -2, -1, 0, 1, 2, 3]))
#print(find_smallest_positive([1, 2, 3]))
#print(find_smallest_positive([-3, -2, -1]) is None)




def find_larger(xs, x):
    if(xs==[]):
        return 0
    left = 0
    right = len(xs)-1
    def find(left, right):
        mid = (right-left)//2+left
#        print("left=", left, "right=", right, "mid=", mid)
        if left == right:
            if xs[left]==x:
                return left
            else:
                return 0
        if left == right-1:
            if xs[left]>x:
                return right
            else:
                return left
        if x < xs[mid]:
            left = mid
        if x >= xs[mid]:
            right = mid
        return find(left, right)
    return find(left, right)

lis = [6, 5, 5, 4, 4, 4, 3, 3, 2, 1]
print(find_larger(lis, 3))
#list_one = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#print("testing find larger", find_larger(list_one, 1))

def find_smaller(xs, x):
    if(xs==[]):
        return 0
    left = 0
    right = len(xs)-1
    def find_small(left, right):
        mid = (right-left)//2 + left
       # print("left=", left, "right=", right, "mid=", mid)
        if left == right:
            if xs[left]==x:
                return left
            else:
                return 0
        if left == right-1:
            if xs[right]<x:
                return left
            else:
                return right 
        if x <= xs[mid]:
            left = mid
        if x > xs[mid]:
            right = mid
           # right = mid+1
        return find_small(left, right)
    return find_small(left, right)
lis = [6, 5, 5, 4, 4, 4, 3, 3, 2, 1]
print("test smaller", find_smaller(lis, 3))


def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    HINT:
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2

    I highly recommend creating stand-alone functions for steps 1 and 2
    that you can test independently.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([3, 2, 1], 4)
    0
    '''
    print("small=", find_smaller(xs, x))
    print("large=", find_larger(xs, x))
    if(xs==[]):
        return 0
    smaller = find_smaller(xs, x)
    larger = find_larger(xs, x)
    value = smaller-larger +1
    if((smaller==0 and larger==0 and xs[0]!=x) or (smaller==len(xs)-1 and larger==len(xs)-1 and xs[len(xs)-1]!=x)):
        return 0
    return value 


def argmin(f, lo, hi, epsilon=1e-3):
    '''
    Assumes that f is an input function that takes a float as input and returns a float with a unique global minimum,
    and that lo and hi are both floats satisfying lo < hi.
    Returns a number that is within epsilon of the value that minimizes f(x) over the interval [lo,hi]

    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
               depending on which one is the smallest, 
               you recursively call your function on the interval [lo,m2] or [m1,hi]

    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''

    if(hi-lo<epsilon):
        return hi
    left = lo
    right = hi
    def go(left, right):
        m1 = (high-low)/10 + left
        m2 = (high-low)/5 + left
        if  high - low < epsilon:
            return high
        if f(m1) > f(m2):
            return go(m1, high)
        if f(m1) < f(m2):
            return go(low, m2)
    return go(low, high)


