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


if __name__ == '__main__':

    prob = [0.2,0.2,0.2,0.9]
    n_arms = len(prob)

    random.shuffle(prob)
    arms = []
    for i in prob:
        arm = BernoulliArm(i)
        arms.append(arm)

    print(arms[0].draw())


