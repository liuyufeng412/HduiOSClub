if __name__=="__main__":
    data = [1]
    for i in range(10):
        print(data)
        data = [1] + [data[i]+data[i+1] for i in range(i)]+[1]


