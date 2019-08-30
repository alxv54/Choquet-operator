import itertools
import operator


class Capacity:

    def __init__(self, capacity_set):
        #création'un objet intégrale de Choquet
        self.criteres = capacity_set.criteres
        self.mu = capacity_set.mu

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
