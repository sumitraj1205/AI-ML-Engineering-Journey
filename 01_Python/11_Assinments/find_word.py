data = True
i = 1
with open("sample.txt","r") as f:
    while data:
        data = f.readline()
        if("python" in data):
            print("word found in line no.-", i)
            break
        i +=1
