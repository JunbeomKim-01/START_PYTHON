import os

path = "C:/Users/estju/OneDrive/바탕 화면/ping"
start = 101
end = 200
for i in range(start, end+1):
    os.mkdir(path + '/'+str(i))
