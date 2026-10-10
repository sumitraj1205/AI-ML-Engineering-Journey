# Q-Learning and SARSA in Reinforcement Learning

## About the Project

In this project, I have implemented two reinforcement learning algorithms: **Q-Learning and SARSA** using Python. I used the CliffWalking environment to understand how an agent learns to reach its goal by interacting with the environment and receiving rewards or penalties.

The main purpose of this project is to understand how these two algorithms work and how they update Q-values while learning.

## Files in This Project

* `Using_Q_Learning.ipynb` – Implementation of the Q-Learning algorithm.
* `using_sarsa.ipynb` – Implementation of the SARSA algorithm.

## 1. Q-Learning

Q-Learning is an off-policy reinforcement learning algorithm. It learns which action is best to take in a particular state by updating the Q-table based on the reward received and the maximum Q-value of the next state.

In this notebook, I trained an agent in the CliffWalking environment and used an epsilon-greedy strategy to balance exploration and exploitation.

## 2. SARSA

SARSA stands for State-Action-Reward-State-Action. It is an on-policy reinforcement learning algorithm.

Unlike Q-Learning, SARSA updates the Q-value using the next action actually selected by the agent. In this notebook, I implemented SARSA and trained the agent in the same CliffWalking environment.

## Difference Between Q-Learning and SARSA

* **Q-Learning:** Uses the maximum Q-value of the next state to update the current Q-value.
* **SARSA:** Uses the Q-value of the next action selected by the agent.

Both algorithms help the agent learn a policy to reach the goal, but their learning approaches are different.

## Technologies Used

* Python
* NumPy
* Gymnasium
* Jupyter Notebook

## How to Run the Project

1. Clone this repository.
2. Install the required libraries:

```bash
pip install numpy gymnasium jupyter
```

3. Open Jupyter Notebook:

```bash
jupyter notebook
```

4. Open either notebook and run the cells one by one.

## What I Learned

By working on this project, I learned:

* Basics of reinforcement learning.
* How Q-tables are used to store state-action values.
* The difference between exploration and exploitation.
* How Q-Learning and SARSA update Q-values.
* The difference between on-policy and off-policy learning.
* How an agent learns through interaction with an environment.

This project helped me build a better understanding of reinforcement learning through practical implementation.
