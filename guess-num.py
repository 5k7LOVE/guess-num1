#standard library 標準函式庫
#light-weighted 輕
#module 模組
#產生一個隨機整數１～１００
# 讓使用者重複輸入數字去猜
# 猜錯的話要告訴他比搭按大／小

import random

fristNum = input('請輸入起始數字：')
fristNum = int(fristNum)

nextNum = input('請輸入最終數字')
nextNum = int(nextNum)

r = random.randint(fristNum, nextNum)
n = 0
while True:
	n += 1

	num = input('請輸入關鍵密碼:')
	num = int(num)
	print('你猜了，', n, '次')
	if r > num:
		print('過小了')
	elif r < num:
		print('過大了')
	elif r == num:
		print('中出')
		break


