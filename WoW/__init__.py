from gym.envs.registration import register

register(
    id='WoW',
    entry_point='gym_game.envs:WoW_env',
    max_episode_steps=50000,
)