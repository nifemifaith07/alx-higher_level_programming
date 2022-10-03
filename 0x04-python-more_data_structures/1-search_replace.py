#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def s_replace(elm):
        return (elm if elm != search else replace)
    return list(map(s_replace, my_list))
