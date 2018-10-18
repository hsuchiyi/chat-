lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:   #讀一發檔案
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    time = s[0][:5]    #字串可以視為清單 #我們取時間的部分
    name = s[0][5:]
    print(name)