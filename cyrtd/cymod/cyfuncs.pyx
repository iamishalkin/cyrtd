cdef float cycube(float num):
    return num**3

cdef float cyroot(float num):
    return num**0.5

cdef float cycuberoot(float num):
    return num**(1/3)

def cube(num: float):
    """
    Argument to the power of 3

    Parameters
    ----------
    num: float
        Number to raise to the power of 3

    Returns
    -------
    float
        Cubic argument
    """
    return cycube(num)

def root(num: float):
    """
    Square root of argument

    Parameters
    ----------
    num: float
        Number to get square root

    Returns
    -------
    float
        Square root
    """
    return cyroot(num)

def cuberoot(num: float):
    """
    Cube root of argument

    Parameters
    ----------
    num: float
        Number to get cube root

    Returns
    -------
    float
        Cube root
    """
    return cycuberoot(num)
