from gym import register


register(
    id='OneDim-v0',
    entry_point='one_dim_env.envs:OneDimEnv',
)