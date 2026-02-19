from typing import Literal


class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        resultant_sword_type = None

        if (self.sword_type != other.sword_type) or self.sword_type == "steel":
            raise Exception("cannot craft")
        
        elif self.sword_type == "bronze":
            resultant_sword_type = "iron"

        elif self.sword_type == "iron":
            resultant_sword_type = "steel"

        return Sword(resultant_sword_type)