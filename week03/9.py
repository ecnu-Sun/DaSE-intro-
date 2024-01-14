def multi(LIST):
    result=[]
    LEN=len(LIST)
    for i in range(0,LEN):
        NEW=1
        for j in range(0,LEN):
            if j!=i:
                NEW=NEW*LIST[j]
        result.append(NEW)
    return result
