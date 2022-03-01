
from bernoulliArm import BernoulliArm
from egreedy import EpsilonGreedy


class Tester():

    def __init__(self,arms,num_sims,allowed_pulls):

        self.arms = arms
        self.num_sims = num_sims
        self.allowed_pulls = allowed_pulls



    def test_algo(self,algorithm):

        tot_pulls = self.num_sims * self.allowed_pulls

        chosen_arms = [0 for _ in range(tot_pulls)]
        rewards = [0 for _ in range(tot_pulls)]
        cumulative_rewards = [0 for _ in range(tot_pulls)]
        sim_nums = [0 for _ in range(tot_pulls)]
        times = [0 for _ in range(tot_pulls)]

        sim = t = 0

        for sims in range(self.num_sims):

            sim += 1
            algorithm.reset(n_arms=self.arms)
            t = 0
            for t in range(self.allowed_pulls):

                t += 1



