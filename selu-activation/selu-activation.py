import math

def selu(x: list) -> list:
    """
    Returns SELU values rounded to four decimal places.
    """
    # Write code here
    value=1.0507
    alpha=1.6733
    result=[]
    for i in x:
        if i>0:
            result.append(value*i)
        else:
            result.append(value*alpha*(math.exp(i)-1))
    return result