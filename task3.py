import task2

# TEST CODE
char_list = ["a", "b", "c", "d", "e", "f", "ab", "cdef"]
bin_list = ["000000", "000001", "000010", "000011", "1000000", "1000001", "1000010", "1000011"]


def string_to_bin(p1: str):
    # while there are still unconverted characters
    #   convert whatever possible from p1 and if everything is converted end the loop and return the binary list
    #   else split the outcome of running task2, and add the binary to a list,
    #   then redo the loop with the remaining characters
    # return the result list
    result = []
    done = False
    while not done:
        p2 = task2.convert_s_to_b(p1)
        if "," not in p2:
            done = True
        else:
            split = p2.split(",")
            result.append(split[0])
            p1 = split[1]
    return result


def bin_to_string(p1: str):
    # while p1 length is greater than 0
    #   check if it's a short or long character
    #       find the short/long character in binary list
    #       take index of binary character and add to result corresponding  character
    # return result
    result = ""
    while len(p1) > 0:
        if p1[0] == "1":
            # long char 7 bits
            index = bin_list.index(p1[0:7])
            result = result + char_list[index]
            p1 = p1[7:]
        else:
            # short char 6 bits
            index = bin_list.index(p1[0:6])
            result = result + char_list[index]
            p1 = p1[6:]
    return result
