import itertools
import operator
import nump


class Capacity:
#Class representing a capacity, i.e. a monotone set function vanishing at the empty set (also called
#fuzzy measure, non-additive measure, monotone measure).
 
    def __init__(self, capacity_set):  #création d'un objet Capacity
        #Cardinalité de l'ensemble, S, sur le quel est définie la capacité
        self.N = log(len(capacity_set),2)
        
        #liste de toutes les parties de S
        self.subsets = [{}]
           for x in list(range(1:N)):
            # for every additional element in our set
            # the power set consists of the subsets that don't
           # contain this element (just take the previous power set)
            # plus the subsets that do contain the element (use list
            # comprehension to add [x] onto everything in the
            # previous power set)
            self.subsets.extend({subset + {x} for subset in result})


        #Capacité elle même
        self.mu = capacity_set

    def get_criteres_trie_par_valeur(self):
        self.criteres_keys_trie_par_valeur = []

        # on les trie
        criteres_trie_par_valeur = sorted(self.criteres.items(), key=operator.itemgetter(1))

        # make a list of the criteria keys in the
        for critere in criteres_trie_par_valeur:
            self.criteres_keys_trie_par_valeur.append(critere[0])

        return self.criteres_keys_trie_par_valeur


    def calculate(self):
        '''Calculate the Choquet Integral and return just that value'''

        # initialize variables for loop
        self.utility=0
        x_n_minus_1 = 0
        self.get_criteres_trie_par_valeur()
        my_keys = self.criteres_keys_trie_par_valeur[:]
        set_of_criteria = frozenset(my_keys)

        for criterum in self.criteres_keys_trie_par_valeur:
            self.utility += (self.criteres[criterum] - x_n_minus_1) * self.mu[set_of_criteria]
            # set up for next loop
            x_n_minus_1 = self.criteres[criterum]
            my_keys.pop(0)
            set_of_criteria = frozenset(my_keys)

        return self.utility
