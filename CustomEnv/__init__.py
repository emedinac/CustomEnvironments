from gym.envs.registration import register

register(
    id='valves-v0',
    entry_point='CustomEnv.envs:MachineryEnv',
)
