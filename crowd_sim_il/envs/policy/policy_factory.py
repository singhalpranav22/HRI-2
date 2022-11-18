from crowd_sim_il.envs.policy.linear import Linear
from crowd_sim_il.envs.policy.orca import ORCA


def none_policy():
    return None


policy_factory = dict()
policy_factory['linear'] = Linear
policy_factory['orca'] = ORCA
policy_factory['none'] = none_policy
