
from math import nan

def NULL_not_found(object: any) -> int:
    type_ = type(object)
    if object is None:
        print(f"Nothing: {object} {type_}")
# print(x == x) # True
# print(nan == nan) # False
    elif isinstance(object, float) and object != object:
        print(f"Garlic: {object} {type_}")
    elif object == 0 and type(object) is int:
        print(f"Zero: {object} {type(object)}")
    elif object == "" and type(object) is str:
        print(f"Empty: {type(object)}")
    elif object is False:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not found")
    return 1
