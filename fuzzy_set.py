import math
import matplotlib.pyplot as plt

class FuzzySet:

    ######################
    # this creates a fuzzy set like ("Tall",175,200) which belongs to a fuzzy variable
    #######################

    def __init__(self, name, min_val, max_val):

        self.name = name
        self.min_val = min_val
        self.max_val = max_val
        self.domain = list(range(min_val,max_val+1))
        self.image = []

    def __getitem__(self, x_val):
        index = self.domain.index(x_val)
        return self.image[index]

    def get_domain(self):
        return self.domain

    def get_image(self):
        return self.image

    ###########################
    # gives the set the membership function desired whether is triangular or trapezoidal
    ###########################

    def create_triangular(self,a,m,b):

        #discretize te passed values
        a = math.trunc(a)
        b = math.trunc(b)
        m = math.trunc(m)

        for x in self.domain:
            if ((x<=a) or (x>=b)):
                self.image.append(0)
            elif (a<x<=m):
                self.image.append((x-a)/(m-a))
            elif (m<x<b):
                self.image.append((b-x)/(b-m))

    def create_gaussian(self,k,m):

        for x in self.domain:
            self.image.append(math.pow(math.e,-(((x-m)**2)/(2*(k**2)))))

    def create_trapezoidal(self,a,b,c,d):

        #discretize te passed values
        a = math.trunc(a)
        b = math.trunc(b)
        c = math.trunc(c)
        d = math.trunc(d)

        for x in self.domain:
            if ((x<a) or (x>d)):
                self.image.append(0)
            elif(a<=x<b):
                self.image.append((x-a)/(b-a))
            elif(b<=x<=c):
                self.image.append(1)
            elif(c<x<=d):
                self.image.append((d-x)/(d-c))

    ######################
    #   make some methods used by fuzzy set.... union, cut set, and mutiply
    ######################

    def union(self,other_set):
        united_set = FuzzySet(f'({self.name} union {other_set.name})',self.min_val,self.max_val)

        join_image = zip(self.image,other_set.image)
        for si,oi in join_image:
            united_set.image.append(max(si,oi))
        
        return united_set

    def multiply(self,value):
        mult_set = FuzzySet(f'{self.name} multiplied',self.min_val,self.max_val)

        for item in self.image:
            mult_set.image.append(item*value) 
        
        return mult_set

    def cutter(self,value):
        cut_set = FuzzySet(f'{self.name} cutted',self.min_val,self.max_val)

        for item in self.image:
            cut_set.image.append(min(item,value))

        return cut_set
  
  #################
  # defuzzification methods
  #################

    def bisector(self):
        area = 0
        _join = zip(self.domain,self.image)
        for x,y in _join:
            area += x*y
        half_area = area/2

        area, index = 0,0

        while half_area > area:
            area += (self.domain[index])*(self.image[index])
            index+=1
            
        return self.domain[index-1]

    def maxims(self):
        maxims = []
        maxim = max(self.image)
        for index in range(len(self.image)):
            if self.image[index] == maxim:
                maxims.append(self.domain[index])
        return maxims
        
    def som(self):
        m_set = self.maxims()
        return(min(m_set))

    def lom(self):
        m_set = self.maxims()
        return(max(m_set))

    def mom(self):
        m_set = self.maxims()
        return(round(sum(m_set)/len(m_set)))

    def centroid(self):
        numerator = 0
        _join = zip(self.domain,self.image)
        for x,y in _join:
            numerator += x*y

        denominator = sum(self.image)

        return round(numerator/denominator,3)


