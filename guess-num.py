#standard library 標準函式庫
#light-weighted 輕
#module 模組
#產生一個隨機整數１～１００
# 讓使用者重複輸入數字去猜
# 猜錯的話要告訴他比搭按大／小

import random

r = random.randint(1, 100)

while True:

	num = input('請輸入關鍵密碼:')
	num = int(num)

	if r > num:
		print('過小了')
	elif r < num:
		print('過大了')
	elif r == num:
		print('中出')
		break