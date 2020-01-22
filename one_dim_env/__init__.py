from gym import register


register(
    id='OneDim-v0',
    entry_point='one_dim_env.envs:OneDimEnv',
)

register(
    id='TwoDim-v0',
    entry_point='two_dim_env.envs:TwoDimEnv',
)