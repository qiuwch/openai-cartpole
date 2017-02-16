import pickle, gym, time
import numpy as np
params = pickle.load(open('random.bin'))

def run_episode(env, parameters):
    observation = env.reset()
    totalreward = 0
    for _ in xrange(1000):
        action = 0 if np.matmul(parameters,observation) < 0 else 1
        env.render()
        time.sleep(0.1)
        observation, reward, done, info = env.step(action)
        totalreward += reward
        if done:
            break
    return totalreward

if __name__ == '__main__':
    env = gym.make('CartPole-v0')
    run_episode(env, params)
