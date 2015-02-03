aa= [5,6,4,7,8,9]
bb= [222,333,444,9]
cc = list(set(aa) | set(bb))
print (cc)

def unique(a):
    """ return the list with duplicate elements removed """
    return list(set(a))

def intersect(a, b):
    """ return the intersection of two lists """
    return list(set(a) & set(b))

def union(a, b):
    """ return the union of two lists """
    return list(set(a) | set(b))

if __name__ == "__main__": 
    a = [0,1,2,0,1,2,3,4,5,6,7,8,9]
    b = [5,6,7,8,9,10,11,12,13,14]
    print (unique(a))
    print (intersect(a, b))
    print (union(a, b))
