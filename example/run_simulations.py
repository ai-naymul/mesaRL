import gym
import mesa_gym_env  # Make sure this is accessible in your Python environment

# Assuming you've registered your custom environment with Gym, otherwise directly use MesaGymEnv
env = gym.make('MesaGymEnv-v0')

observation = env.reset()
for _ in range(1000):  # Run for 1000 steps or adjust as needed
    action = env.action_space.sample()  # Select a random action
    observation, reward, done, info = env.step(action)
    if done:
        observation = env.reset()
env.close()