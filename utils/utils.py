import gym
import numpy as np
import pandas as pd
from customtkinter import *
from tksheet import Sheet
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import defaultdict
import seaborn as sns
from time import time


def import_agent_knowledge_from_file(source):
    """
    Imports agent knowledge from a file in CSV format.

    Parameters:
        source (str): File path or URL of the CSV file.

    Returns:
        pandas.DataFrame: DataFrame containing the imported agent knowledge.
    """
    return pd.read_csv(source)

def initiate_agent_profile(Q, save_profile, profile_name: str):
    """
    Initiates the agent profile based on the provided Q values.

    Parameters:
        Q (dict): A dictionary representing the Q values.
        save_profile (bool): Flag indicating whether to save the agent profile as a CSV file. Default is True.
        profile_name (str): Name of the profile if save_profile is True.

    Returns:
        pandas.DataFrame: DataFrame containing the agent profile with calculated scores and other columns.
    """
    Scores = pd.DataFrame(Q.values(), columns=['Stick', 'Hit'])
    States = pd.DataFrame(Q.keys(), columns=['My','Thy','Ace'])
    df = pd.concat([States, Scores], axis=1)
    df['Greedy Choice'] = np.int8(df.Hit>df.Stick)
    df['Greedy Value'] = df[['Hit','Stick']].apply(max, axis=1)
    if save_profile:
        df.to_csv(f'./data/{profile_name}.csv')
    return df

def return_agent_policy_data(df):
    """
    Returns policy data for the agent based on the provided DataFrame.

    Parameters:
        df (pandas.DataFrame): DataFrame containing the agent profile.

    Returns:
        pandas.DataFrame: Heatmap of the greedy choices for states where Ace is present.
        pandas.DataFrame: Heatmap of the greedy choices for states where Ace is not present.
    """
    ace = df[df.Ace]
    n_ace = df[~df.Ace]

    hm = ace.pivot_table('Greedy Choice','My','Thy')
    nhm = n_ace.pivot_table('Greedy Choice','My','Thy')
    return hm,nhm

def return_agent_state_value_heatmap(df):
    """
    Returns the state value heatmaps for the agent based on the provided DataFrame.

    Parameters:
        df (pandas.DataFrame): DataFrame containing the agent profile.

    Returns:
        pandas.DataFrame: Heatmap of the greedy values for states where Ace is present.
        pandas.DataFrame: Heatmap of the greedy values for states where Ace is not present.
    """
    ace = df[df.Ace]
    n_ace = df[~df.Ace]
    hc = ace.pivot_table('Greedy Value','My','Thy')
    nhc = n_ace.pivot_table('Greedy Value','My','Thy')
    return hc, nhc

def eps_greedy(Q, state, epsilon):
    """
    Epsilon-greedy policy for action selection based on Q values and state.

    Parameters:
        Q (dict): A dictionary representing the Q values.
        state (tuple): Current state of the agent.
        epsilon (float): Epsilon value for exploration vs. exploitation.

    Returns:
        int: Selected action based on epsilon-greedy policy.
    """
    if state[0]<12:
        return 1
    elif np.random.random() < epsilon:
        return np.random.choice([0,1])  # Choose a random action
    else:
        return np.argmax(Q[state])
    
def generate_episode(env, Q, eps):
    """
    Generates an episode using the epsilon-greedy policy.

    Parameters:
        env (gym.Env): The RL environment to interact with.
        Q (dict): A dictionary representing the Q values.
        eps (float): Epsilon value for exploration vs. exploitation.

    Returns:
        list: List of tuples representing (state, action, reward) for each step in the episode.
    """
    state = env.reset()[0]
    episode = []

    done = False
    while not done:
        action = eps_greedy(Q, state, eps)
        next_state, reward, done, _, _ = env.step(action)
        episode.append((state, action, reward))
        state = next_state 
    return episode 