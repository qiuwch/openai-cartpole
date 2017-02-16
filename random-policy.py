import gym, time
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    time.sleep(0.1)
    env.step(env.action_space.sample()) # take a random action
