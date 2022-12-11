from .geoip import ip_to_coordinates
from .ids_rules import IDSRules
from .check_tor import CheckTor


def str_to_int(s: str):
    try:
        return int(s)
    except ValueError:
        return None
