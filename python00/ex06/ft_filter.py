
def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    #document string of filter() method
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))



# my_list = [0, 1, "98989898", "Hello", None, True, False, [], "", 42]
# def is_int(num):
#     if type(num) == int:
#         return True
#     return False
# yyy = filter(is_int, my_list)
# zzz = ft_filter(is_int, my_list)

# print(f"yyy (original): {list(yyy)}")
# print(f"zzz (dyalk):    {list(zzz)}")