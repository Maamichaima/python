def all_thing_is_obj(object: any) -> int:
    type_ = type(object)
    if type_ == list:
        print("List : ", type_)
    elif type_ == tuple:
        print("Tuple : ", type_)
    elif type_ == set:
        print("Set : ", type_)
    elif type_ == dict:
        print("Dict : ", type_)
    elif type_ == str:
        print(f"{object} is in the kitchen : {type_}")
    else:      
        print("Type not found")
    return 42
