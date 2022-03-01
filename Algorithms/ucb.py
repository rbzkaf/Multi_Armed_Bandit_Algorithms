import math
import random

class UCB():

    def __init__(self, confidence, n_arms):

        self.confidence = confidence
        self.n_arms = n_arms
        self.name = "UCB"
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


    def pull_arm(self):
        """
        Function to decide which arm to pull
        :return:
        """

        #To ensure it tries all arms before UCB
        for arm in range(self.n_arms):
            if self.counts[arm] == 0:
                return(arm)

        ucb = [0.0 for _ in range(self.n_arms)]

        #t: Number of total steps taken (i.e) number of total arm pulls
        t = sum(self.counts)

        for arm in range(self.n_arms):

            """
            N_t: Number of times particular arms pulled
            Intuition - The lower number of times it has been pulled
                        The higher its chance of being selected
                        This helps with exploration
                        
            Q_t: Learnt value of the current estimate of value of arm
            """
            N_t = self.counts[arm]
            Q_t = self.values[arm]

            ucb[arm] = Q_t + self.confidence * math.sqrt(math.log(t)/N_t)

        return self.idx_max(ucb)








    def update(self,chosen_arm,reward):
        """
        Function to update agent's estimate of value of particular arm

        :param chosen_arm:
        :param reward:
        :return:
        """

        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]

        val = self.values[chosen_arm]

        self.values[chosen_arm] = (((n - 1) / n) * val) + (1/n) * reward





