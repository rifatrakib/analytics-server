from server.config.environments import BaseConfig


class ProductionConfig(BaseConfig):
    DEBUG: bool = False
    MODE: str = "production"
