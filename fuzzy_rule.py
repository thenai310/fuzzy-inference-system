from fuzzy_variable import *

# # # # # # # #
#   
#  formar una tupla (variable, set_name ,former = Bool)
#  y formar dos listas de estas para antecedentes y consecuencias
#

class FuzzyRule:

    def __init__(self, antecedents, consequent, op ):

        self.r_antecedents = antecedents
        
        if op.lower() == 'and': 
            self.op = 'min' 
        else: 
            self.op = 'max'

        self.r_consequent = consequent

    def evaluate_rule(self,input_values):
        eval_value = []

        for var , set_name in self.r_antecedents:
            for in_var, value in input_values:
                if in_var==var:
                    eval_value.append(var.fuzzify(value,set_name))

        image_val =  eval(f'{self.op}({eval_value})')

        return self.r_consequent[0].fuzzify(image_val,self.r_consequent[1],self.r_consequent[2])


    def evaluate_larsen(self,input_values):
        eval_value = []

        for var , set_name in self.r_antecedents:
            for in_var, value in input_values:
                if in_var==var:
                    eval_value.append(var.fuzzify(value,set_name))

        image_val =  eval(f'{self.op}({eval_value})')

        return self.r_consequent[0].fuzzify_larsen(image_val,self.r_consequent[1])
