import numpy as np
import matplotlib.pyplot as plt

n_actions = 4
gride_size = 5

n_states = gride_size * gride_size

Q_table = np.zeros((n_states, n_actions))

rewards = np.full(n_states, -1)
rewards[24] = 10
rewards[12] = -10

alpha = 0.1
gamma = 0.9
epsilon = 0.1

def epsilon_greedy_action(Q_table, state, epsilon):
    if np.random.rand < epsilon:
        return np.random.randint(0, n_actions)
    else:
        return np.argmax(Q_table[state])

for episode in range(1000):
    state = np.random.randint(0, n_states)
    done = False
    while not done:
        action = epsilon_greedy_action(Q_table, state, epsilon)
        next_state = np.random.randint(0, n_states)
        reward = rewards[state]
        Q_table[state, action] += alpha * (
            reward + gamma *np.max(Q_table[next_state]) - Q_table[state, action]
        )
        state = next_state
        if next_state in [12, 24]:
            done = True

culmelative_rewards = []
for episode in range(1000):
    state = np.random.randint(0, n_states)
    done = False
    total_rewards = 0
    while not done:
        action = epsilon_greedy_action(Q_table, state, epsilon)
        next_state = np.random.randint(0, n_states)
        reward = rewards[state]
        Q_table[state, action] += alpha * (
            reward + gamma * np.max(Q_table[next_state]) - Q_table[state, action]
        )
        state = next_state
        total_rewards += reward
        if next_state in [12, 24]:
            done = True
        
    culmelative_rewards.append(total_rewards)

plt.plot(culmelative_rewards)
plt.title("Learning Curve")
plt.xlabel("Episode")
plt.ylabel("Cumulative Rewards")
plt.show()