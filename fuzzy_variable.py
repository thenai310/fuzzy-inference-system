from fuzzy_set import *

class FuzzyVariable():

    def __init__(self, name, min_val, max_val):

        self.name = name
        self._sets={}
        self.max_val = max_val
        self.min_val = min_val

    def __eq__(self,other_var):
        return self.name==other_var.name

    def add_gaussian(self,name,exp,mean):
        '''
        Crea una conjunto difuso con una distribucion gaussiana
        Params:
        --------
            name: string, nombre del conjunto
            exp: exponente de la distribucion
            mean: medida de la distribucion
        '''
        new_set = FuzzySet(name,self.min_val,self.max_val)
        new_set.create_gaussian(exp,mean)
        self._sets[name] = new_set

    def add_triangular(self, name, low, mid, high):
        '''
        Crea una conjunto difuso con una distribucion triangular
        Params:
        --------
            name: string, nombre del conjunto
            low: valor de inicio
            mid: pico de la distribucion
            high: ultimo valor de la distribucion
        '''
        new_set = FuzzySet(name,self.min_val,self.max_val)
        new_set.create_triangular(low, mid, high)
        self._sets[name] = new_set

    def add_trapezoidal(self, name, a, b, c, d):
        '''
        Crea una conjunto difuso con una distribucion trapezoidal
        Params:
        --------
            name: string, nombre del conjunto
            a: valor de inicio de la distribucion
            b,c: valores medios de la distribucion
            d: ultimo valor de la distribucion
        '''
        new_set = FuzzySet(name,self.min_val,self.max_val)
        new_set.create_trapezoidal(a, b, c, d)
        self._sets[name] = new_set

    def fuzzify_larsen(self, value, set_name):
        return self._sets[set_name].multiply(value)

    def fuzzify(self, value, set_name, former = True):
        if former:
            return self._sets[set_name][value]
        else:
            return self._sets[set_name].cutter(value)
    
    def plot_variable(self, ax = None, show = True):
        if ax == None:
            ax = plt.subplot(111)

        for n ,s in self._sets.items():
            ax.plot(s.get_domain(), s.get_image(), label=n)

        ax.set_title(self.name)
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        
        if show:
            plt.show()
