data = []
count = 0
with open ('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
        count += 1
        if count % 1000 == 0: # 如果是1000的倍數就, % 是用來求於數 EX: 7 % 3 = 1, 10 % 6 = 4
            print(len(data)) # 讀取過程中印出進度
print(len(data)) # 印出 data 計算清單的總數
print('------------------')
print(data[0]) # 印出 data 第一筆留言
print(len(data[0])) # 印出 data 計算第一筆留言的總數
print('------------------')
print(data[1]) # 印出 data 第二筆留言