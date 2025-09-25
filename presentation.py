#"""
#    >>> slope(5, 3, 4, 2)
#    1.0
#    >>> slope(1, 2, 3, 2)
#    0.0
#    >>> slope(1, 2, 3, 3)
#    0.5
#    >>> slope(2, 4, 1, 2)
#    2.0
#"""
# Docstring. Expects the function to return a float representing the slope of the line between two points (x1,y1) and (x2,y2).
#def slope(x1,y1,x2,y2):
#    dx = x2 - x1
#    dy = y2 - y1
#    slope = dy / dx
#    return slope
    # This function is the basic slope formula. It generates variables for the change in x and y (Delta X and Delta Y), then divides them to get the slope.
    # It does not account for undefined, zero, or fractional slopes.
    # My second example does account for these, but is more complex.

#if __name__ == "__main__":
#    import doctest
#    doctest.testmod()
# Doctest Function


#Secondary, more complex example:
"""
    >>> advslope(5,3,4,2,"none")
    1.0
    >>> advslope(1,2,3,2,"none")
    'Zero'
    >>> advslope(1,2,3,3,"none")
    0.5
    >>> advslope(2,4,1,2,"none")
    2.0
    >>> advslope(5,4,5,1,"none")
    'Undefined'
    >>> advslope(3,2,1,4,"fr")
    '2/-2'
"""
def advslope(x1,y1,x2,y2,option):
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0:
        return 'Undefined'
    elif dy == 0:
        return 'Zero'
    elif option == "fr":
        fraction = str(dy) + '/' + str(dx)
        return str(fraction)
    else:
        slope = dy / dx
        return slope

if __name__ == "__main__":
    import doctest
    doctest.testmod()
# Doctest Function