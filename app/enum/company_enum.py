from enum import Enum

class CompanyType(str, Enum):
    SOFTWARE = "software house"
    HARDWARE = "hardware"
    MEDICAL = "medical"
    TEXTILE = "textile"
    EDUCATION = "education"
