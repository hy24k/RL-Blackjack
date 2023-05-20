from utils.utils import *


def plot_policies(hm,nhm):
    """
    Plots the optimal policies based on the provided heatmaps.

    Parameters:
        hm (pandas.DataFrame): Heatmap of the optimal policy with a usable ace.
        nhm (pandas.DataFrame): Heatmap of the optimal policy without a usable ace.

    Returns:
        None
    """
    fig, axs = plt.subplots(1, 2)
    sns.heatmap(hm, cmap='gray', ax=axs[0] )
    axs[0].invert_yaxis()
    axs[0].set_title('Optimal policy with usable ace')
    axs[0].set_xlabel('Dealers Up card')
    axs[0].set_ylabel('Players Sum')
    axs[0].set_xticklabels(['A']+list(range(2,11)))

    sns.heatmap(nhm.loc[11:,:], cmap='gray')
    axs[1].invert_yaxis()
    axs[1].set_title('Optimal policy, NO usable ace')
    axs[1].set_xlabel('Dealer\'s Up card')
    axs[1].set_ylabel('Player\'s Sum')
    axs[1].set_xticklabels(['A']+list(range(2,11)))

    plt.subplots_adjust(wspace=0.4)
    plt.savefig('./media/Visualisations/policy.png')
    plt.show()

def plot_state_values(hc,nhc):
    """
    Plots the score heatmaps based on the provided heatmaps.

    Parameters:
        hc (pandas.DataFrame): Heatmap of the scores with a usable ace.
        nhc (pandas.DataFrame): Heatmap of the scores without a usable ace.

    Returns:
        None
    """
    fig, axs = plt.subplots(1, 2)
    sns.heatmap(hc, cmap='gray', ax=axs[0])
    axs[0].invert_yaxis()
    axs[0].set_title('Score heatmap with usable ace')
    axs[0].set_xlabel('Dealer\'s Up card')
    axs[0].set_ylabel('Player\'s Sum')
    axs[0].set_xticklabels(['A']+list(range(2,11)))

    sns.heatmap(nhc, cmap='gray', ax=axs[1])
    axs[1].invert_yaxis()
    axs[1].set_title('Score heatmap, NO usable ace')
    axs[1].set_xlabel('Dealers Up card')
    axs[1].set_ylabel('Players Sum')
    axs[1].set_xticklabels(['A']+list(range(2,11)))

    plt.subplots_adjust(wspace=0.4)
    plt.savefig('./media/Visualisations/score_matrices.png')
    plt.show()