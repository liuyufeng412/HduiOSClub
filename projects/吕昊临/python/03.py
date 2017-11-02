# 输出前20项裴波纳契数列
if __name__=="__main__": 
    x,y=1,1
    for _ in range(20):
        print(x)
        x,y=y,x+y


