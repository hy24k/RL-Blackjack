# Exploring Monte Carlo Control on Blackjack RL environment

Author: Hayk Hovhannisyan<br>
Date: 16 May 2023<br>
BS in Data Science 2024, American University of Armenia

---

**Abstract:**<br>

This notebook explores the application of Monte Carlo Control in a Reinforcement Learning (RL) environment for the game of Blackjack. 

**The goal:** <br>
Improve the policy function through an iterative process of simulation and evaluation.
 The implementation follows the methodology outlined by Sutton et al. in their book ["Reinforcement Learning: An Introduction"](http://incompleteideas.net/book/RLbook2020.pdf). 
 
 **RL Algorythm** <br>
 Monte Carlo Control is employed to estimate the state-action values, and an epsilon-greedy policy is used to balance exploration and exploitation. The study provides insights into the effectiveness of Monte Carlo Control in learning optimal policies for playing Blackjack and contributes to the field of RL and decision-making in uncertain environments.

 **Environment**
 The OpenAI Gym environment is utilized in this study. The Blackjack environment from the OpenAI Gym library is employed to simulate the game and interact with the RL agent.

 ---

**Repo structure**
- `data` - this folder contains some profiles of agents generated during MC simulation phaze
- `utils` - contains `plot_utils.py` and `utils.py` files for utilization functions
- `media` - Contains visualisations and any other media used in `mc_control.ipynb`

- `Exploring_MC_control.pdf` - slideshow, showcasing the Blackjack environment and Monte Carlo - Policy Control algorythm 
- `gui.py` - GUI interface for showcasing the agent
- `mc_control.ipynb` - implementation of MC COntrol algorythm

---

**Clonning repo**
```sh
git clone https://github.com/hy24k/RL-Blackjack

cd RL_Blackjack
python -m venv venv
source ./venv/activate
pip install -r ./requirements.txt
```

---

**GUI**

To run gui, type following in a terminal:

```sh
python ./gui.py
```

---

Python  version `3.11.3`

---

# EOD