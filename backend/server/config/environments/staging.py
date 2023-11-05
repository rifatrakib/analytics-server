from server.config.environments import BaseConfig


class StagingConfig(BaseConfig):
    DEBUG: bool = False
    MODE: str = "staging"
