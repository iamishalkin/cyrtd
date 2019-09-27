cdef float cycube(float num):
    return num**3

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
