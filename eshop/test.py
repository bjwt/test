# -*- coding: utf-8 -*-  
import time
import random
num = 0
names = ["吴可渝","吴可妮","吴涛","刘华利"]
for num in range(100):
	index = random.randint(0,3)
	print names[index]
	num += 1
	time.sleep(5)
