from setuptools import setup


setup(
    name='crowdnav',
    version='0.0.1',
    packages=[
        'crowd_nav',
        'crowd_nav.configs',
        'crowd_nav.policy',
        'crowd_nav.utils',
        'crowd_sim_il',
        'crowd_sim_il.envs',
        'crowd_sim_il.envs.policy',
        'crowd_sim_il.envs.utils',
        'crowd_sim_rl',
        'crowd_sim_rl.envs',
        'crowd_sim_rl.envs.policy',
        'crowd_sim_rl.envs.utils',
    ],
    install_requires=[
        'gitpython',
        'gym',
        'matplotlib',
        'numpy',
        'scipy',
        'torch',
        'torchvision',
    ],
    extras_require={
        'test': [
            'pylint',
            'pytest',
        ],
    },
)
