# this is a test python file

def test(a1, a2):
    c = [ i for i in a1 if i not in a2 ]
    if len(c):
        return True
    else:
        return False
