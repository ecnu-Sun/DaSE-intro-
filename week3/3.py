import re
def retest(Id):
    pattern=r'(^\d{15}$)|(^\d{17}([0-9]|X)$)'
    if(re.match(pattern,Id)):
        return True
    else: return False
