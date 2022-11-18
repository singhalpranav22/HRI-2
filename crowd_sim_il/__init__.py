from gym.envs.registration import register

register(
    id='CrowdSim_il-v0',
    entry_point='crowd_sim_il.envs:CrowdSim',
)
