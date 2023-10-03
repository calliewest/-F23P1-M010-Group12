char_list = ["a", "b", "c", "d", "e", "f", "ab", "cdef"]
bin_list = ["0", "10", "110", "1110", "11110", "111110", "1111110", "111111110"]


def convert_s_to_b(p1: str):
    # loops through the characters of the param dropping 1 character from the end with each loop
    for index in range(len(p1)):
        # loop through the character list and determine if the parameter(or part of it) is in the character list
        for item in char_list:
            if p1[0:len(p1) - index] == item:
                return str(bin_list[char_list.index(item)]) + p1.replace(item, "")
    return p1
    pass
