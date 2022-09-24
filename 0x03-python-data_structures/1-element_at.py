#!/usr/bin/python3

 def element_at(my_list, idx):
        """
        retrieves an element from a list like in C.
        """
        return(my_list[idx] if 0 <= idx < len(my_list) else None)
