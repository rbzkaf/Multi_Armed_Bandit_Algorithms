
from bernoulliArm import BernoulliArm
from Algorithms.thompson import Thompson

import pandas as pd
import numpy as np


class Tester():

    def __init__(self, arms,num_sims,allowed_pulls):

        self.arms = arms
        self.num_sims = num_sims
        self.allowed_pulls = allowed_pulls


    def test_algo(self,algo,arms):
        """

        Run simulations and store data in CSV


        :param algo:
        :param arms:
        :return:
        """
        tot_pulls = self.num_sims * self.allowed_pulls
        chosen_arms = [0 for _ in range(tot_pulls)]
        rewards = [0 for _ in range(tot_pulls)]
        cumulative_rewards = [0 for _ in range(tot_pulls)]
        sim_num = [0 for _ in range(tot_pulls)]
        pull_no = [0 for _ in range(tot_pulls)]

        sim = 0
        t = 0

        for sims in range(self.num_sims):

            sim += 1
            algo.reset(n_arms=self.arms)
            t = 0
            for t in range(self.allowed_pulls):

                t += 1

                index = (sim - 1) * self.allowed_pulls + t - 1
                sim_num[index] = sim
                pull_no[index] = t

                chosen_arm = algo.pull_arm()
                chosen_arms[index] = chosen_arm

                reward = arms[chosen_arms[index]].draw()
                rewards[index] = reward

                if t == 1:
                    cumulative_rewards[index] = reward
                else:
                    cumulative_rewards[index] = cumulative_rewards[index-1] + reward

                algo.update(chosen_arm,reward)




        return [sim_num, pull_no, chosen_arms, rewards, cumulative_rewards]








if __name__ == '__main__':

    """
    Initialization rules of arms, make changes to explore how it affects E-Greedy
    """


    prob_of_arms = [0.1, 0.12, 0.08, 0.14, 0.15]
    n_arms = len(prob_of_arms)
    arms = []
    for i in prob_of_arms:
        arm = BernoulliArm(i)
        arms.append(arm)

    print("Probability of arms: ", prob_of_arms)

    """
    Set how long sim should run 
    """
    num_sims = 100
    allowed_pulls = 400


    tester = Tester(arms=n_arms, num_sims= num_sims, allowed_pulls= allowed_pulls)

    agent_num = [1,2,3,4,5]
    """
    Running Simulations 
    """
    fin = np.zeros((1,5))
    for conf in agent_num:

        alg = Thompson(n_arms=n_arms)
        res = tester.test_algo(algo=alg, arms=arms)

        res = np.array(res)
        res = res.T
        fin = np.concatenate((fin,res),axis=0)

    print(alg.values)
    fin = fin[1:]
    df = pd.DataFrame(fin, columns=["Simulation", "Pull_no", "Chosen_arm", "Reward", "Cumul_Reward"])

    df.to_csv("./SimulationData/"+alg.name+"_"+str(num_sims)+"_sim_"+str(allowed_pulls)+"_pulls")











