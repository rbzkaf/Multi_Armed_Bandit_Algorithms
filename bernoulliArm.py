import random

class BernoulliArm():

    def __init__(self, prob):

        self.prob = prob

    def draw(self):
        """
        Rewards if within Probability p
        :return:
        """
        if random.random() > self.prob:
            return 0

        else:
            return 1

