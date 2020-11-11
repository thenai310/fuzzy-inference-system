from fuzzy_rule import *
class FuzzySystem:

    def __init__(self):

        self.rules = []

    def add_rule(self,ant,cons, op = 'None'):
        """
        Agrega un regla al sistema 
        de inferencia:

        Params:
        -----------
            ant: lista de antecedentes( Una lista de tuplas con la variable,
            la funcion de membresia y un bool que indica si es antecedente)

            cons: consecuencia, tupla con la variable, la funcion de membresia 
            y el bool(former = False) que indica si es antecedente

            op: string opcional que indica el operador entre los antecedentes'or' 
            o 'and'

        """
        rule = FuzzyRule(ant,cons,op)
        self.rules.append(rule)

    def run_sid(self,input_values,method,add_m):
        """
        Correr el sistema de inferencia difusa

        Params:
        --------
            input_values: lista de valores de entrada (tupla , variable-valor)

            method: string, nombre del metodo de desfusificacion:
                    * centroid * bisector * lom * mom * som
            add_m: string nombre del metodo de agregacion:
                    * mamdani * larsen

        Returns:
        ---------
            value: evaluacion del metodo en el conjunto
                   resultante de la agregacion  
        """
        set_list = []
        for rule in self.rules:
            if add_m.lower == 'mamdani':
                set_list.append(rule.evaluate_rule(input_values))
            else:
                set_list.append(rule.evaluate_rule(input_values,False))

        initial_set = set_list.pop(0)
        for _set in set_list:
            initial_set = initial_set.union(_set)

        return eval(f'initial_set.{method.lower()}()')

    