from gym.envs.registration import register

register(
    id='CrowdSim_rl-v0',
    entry_point='crowd_sim_rl.envs:CrowdSim',
)
