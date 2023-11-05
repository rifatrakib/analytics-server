from enum import Enum


class Modes(str, Enum):
    development = "development"
    production = "production"
    staging = "staging"
