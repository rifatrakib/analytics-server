from server.config.environments import BaseConfig


class DevelopmentConfig(BaseConfig):
    DEBUG: bool = True
    MODE: str = "development"
