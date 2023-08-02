import numpy as np

# example of result representer file
def represent(result):
    print(result)
    return f"{np.argmax(result)}"
