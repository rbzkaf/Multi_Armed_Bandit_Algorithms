import math
import random

from scipy import beta

class Thompson():

    def __init__(self, n_arms,a,b):

        self.a = a
        self.b = b
        self.n_arms = n_arms
        self.name = "Thompson"
        self.counts = [0 for _ in range(n_arms)]
        self.values = [0 for _ in range(n_arms)]

    def reset(self, n_arms):
        self.n_arms = n_arms
        self.counts = [0 for _ in range(self.n_arms)]
        self.values = [0 for _ in range(self.n_arms)]





    def pull_arm(self):
        """
        Function to decide which arm to pull
        :return:
        """



    def update(self, chosen_arm, reward):
        """
        Function to update agent's estimate of value of particular arm

        :param chosen_arm:
        :param reward:
        :return:
        """

        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]

        val = self.values[chosen_arm]

        self.values[chosen_arm] = (((n - 1) / n) * val) + (1 / n) * reward





