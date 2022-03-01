
from scipy.stats import beta

class Thompson():

    def __init__(self, n_arms):

        self.n_arms = n_arms
        self.name = "Thompson"
        self.counts = [0 for _ in range(n_arms)]
        self.values = [0 for _ in range(n_arms)]
        self.a = []
        self.b = []
        self.reset(n_arms)

    def reset(self, n_arms):
        self.n_arms = n_arms
        self.counts = [0 for _ in range(self.n_arms)]
        self.values = [0 for _ in range(self.n_arms)]

        # Counts of Reward
        self.a = [1 for _ in range(self.n_arms)]
        # Counts of No Reward
        self.b = [1 for _ in range(self.n_arms)]

    def idx_max(self,draws):
        """
        Returns Index of Arm to Exploit

        :return: Index of Max
        """
        return draws.index(max(draws))




    def pull_arm(self):
        """
        Function to decide which arm to pull
        :return:
        """

        # Pairs up a and b for each arm
        parameters = zip(self.a, self.b)

        rand_draws = []
        for param in parameters:

            # Generates a random number using Beta distribution with parameters a and b
            draw = beta.rvs(param[0], param[1], size=1)
            rand_draws.append(draw)

        return self.idx_max(rand_draws)






    def update(self, chosen_arm, reward):
        """
        Function to update agent's estimate of value of particular arm
        Note: Update is called in Test Algorithm after reward is calculated

        :param chosen_arm:
        :param reward:
        :return:
        """


        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]

        val = self.values[chosen_arm]

        self.values[chosen_arm] = (((n - 1) / n) * val) + (1 / n) * reward





