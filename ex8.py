class Set:
    def __init__(self, value = []):    # Constructor
        self.data = []                 # Manages a list
        self.concat(value)

    def intersection(self, other):        # other is any sequence
        res = []                       # self is the subject
        for x in self.data:
            if x in other:             # Pick common items
                res.append(x)
        return Set(res)                # Return a new Set

    def union(self, other):            # other is any sequence
        res = self.data[:]             # Copy of my list
        for x in other:                # Add items in other
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:                
            if not x in self.data:     # Removes duplicates
                self.data.append(x)

    def __len__(self):          return len(self.data)        # len(self)
    def __getitem__(self, key): return self.data[key]        # self[i], self[i:j]
    def __and__(self, other):   return self.intersection(other) # self & other
    def __or__(self, other):    return self.union(other)     # self | other
    def __repr__(self):         return 'Set({})'.format(repr(self.data))  
    def __iter__(self):         return iter(self.data)       # for x in self:

    def issubset(self,other):    #self.issubset(other)
        for x in self.data:
            if x in other.data:
                continue
            else:
                return False
        return True


    def __le__(self, other):     #self <= other
        for x in self.data:
            if x in other.data:
                continue
            else:
                return False
        return True

    def __lt__(self, other):     #self < other
        if len(Set(self.data)) != len(Set(other.data)):
            for x in self.data:
                if x in other.data:
                    continue
                else:
                    return False
            return True
        else:
            return False

            

    def issuperset(self, other):  #self.issuperset(other)
        for x in other.data:
            if x in self.data:
                continue
            else:
                return False
        return True

    def __ge__(self,other):         #self >= other
        for x in other.data:
            if x in self.data:
                continue
            else:
                return False
        return True

    def __gt__(self,other):         #self > other 
        if len(Set(self.data)) != len(Set(other.data)):
            for x in other.data:
                if x in self.data:
                    continue
                else:
                    return False
            return True
        else:
            return False

    def __ior__(self,other):    #self |= other
        list = []
        for x in other.data:
            if x not in self.data:
                list.append(x)
        self.data += list
        return (Set(self))

    def intersection_update(self, other):   #self.intersection_update(others)
        list = []
        for x in self.data:
            if x in other.data:
                list.append(x)
        self.data = list
        return(Set(self))

    def __iand__(self,other):           #self &= other
        list = []
        for x in self.data:
            if x not in other.data:
                list.append(x)
        self.data = list
        return(Set(self))

    def difference_update(self, other):   #self.difference_update(others)
        list = []
        for x in self.data:
            if x not in other.data:
                list.append(x)
        self.data = list
        return(Set(self))
        
    def __isub__(self,other):         #self -= other
        list = []
        for x in self.data:
            if x not in other.data:
                list.append(x)
        self.data = list
        return(Set(self))
    
    def symmetric_difference_update(self, other):    #self.symmetric_difference_update(other)
        list = []
        for x in self.data:
            if x not in other.data:
                list.append(x)
        for y in other.data:
            if y not in self.data:
                list.append(y)
        self.data = list
        return(Set(self))
    
    def __ixor__(self, other):
        list = []
        for x in self.data:
            if x not in other.data:
                list.append(x)
        for y in other.data:
            if y not in self.data:
                list.append(y)
        self.data = list
        return(Set(self))

    def add(self, elem):
        return Set(self.data).union([elem])

    def remove(self,elem):
        if elem in self.data:
            self.data.remove(elem)
            return(Set(self))
        else:
            raise KeyError

    

    
        
            
    


    
x = Set([1,3,5,7, 1, 3])
y = Set([2,1,4,5,6])
z = Set([1,2])
a = Set([1,2])
print(x, y, len(x))
print(x.intersection(y), y.union(x))
print(x & y, x | y)
print(x[2], y[:2])
for element in x:
    print(element, end=' ')
print()
print(3 not in y)  # membership test
print(list(x))   # convert to list because x is iterable
print(z<y)
print(z<=y)
print(z.issubset(y))
print(z<a)
print(y>z)
print(z>=a)
print(z>a)
print(y.issuperset(z))
#x|=z
#print(x)
#print(y)
#print(y.intersection_update(z))
#print(y.difference_update(z))
#print(x.symmetric_difference_update(y))
print(z.add(3))
print(x.remove(1))