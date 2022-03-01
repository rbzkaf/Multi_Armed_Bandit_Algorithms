import random

class EpsilonGreedy():

    def __init__(self, epsilon, n_arms):

        self.epsilon = epsilon
        self.n_arms = n_arms
        self.name = "Epsilon_Greedy"
        self.counts = [0 for _ in range(n_arms)]
        self.values = [0 for _ in range(n_arms)]


    def reset(self, n_arms):
        self.n_arms = n_arms
        self.counts = [0 for _ in range(self.n_arms)]
        self.values = [0 for _ in range(self.n_arms)]

    def idx_max(self,ucb):
        """
        Returns Index of Arm to Exploit

        :return: Index of Max
        """
        return ucb.index(max(ucb))

    def get_avg(self):
        """
        Returns average of values
        Can change depending on weighing scheme

        :return:
        """
        return sum(self.values) / len(self.values)


    def pull_arm(self):
        """
        Function to flip Epsilon coin between exploit and explore
        :return:
        """
        if random.random() > self.epsilon:
            return self.idx_max(self.values)

        else:
            return random.randrange(len(self.values))


    def update(self,chosen_arm,reward):
        """
        Function to update value of particular arm
        Note: Update is called in Test Algorithm after reward is calculated

        :param chosen_arm:
        :param reward:
        :return:
        """

        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]

        val = self.values[chosen_arm]

        self.values[chosen_arm] = (((n - 1) / n) * val) + (1/n) * reward





