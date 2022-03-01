import matplotlib.pyplot as plt
import pandas as pd



class Vizualizer():

    def __init__(self):
        self.df = pd.read_csv("./SimulationData/Epsilon_Greedy_1_sim_10000_pulls")


    def viz_cumul_rew(self):


        #Split Dataframes for each Epsilon rate

        eps = self.df.Epsilon.unique()
        gk = self.df.groupby("Epsilon")

        for ep in eps:
            data = gk.get_group(ep)
            label = "E="+str(float(ep))
            plt.plot(data["Pull_no"], data["Cumul_Reward"], label=label)


        plt.legend()
        plt.show()



if __name__ == '__main__':

    viz = Vizualizer()
    viz.viz_cumul_rew()

