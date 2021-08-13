import threading
import time

# def func():
# 	print("Ran")
# 	time.sleep(1)
# 	print("Done")
# 	time.sleep(0.85)
# 	print("Now done")

# x = threading.Thread(target=func)
# x.start()
# print(threading.activeCount())
# time.sleep(1.2)
# print("Finally")

# def count(n):
# 	for i in range(1, n+1):
# 		print(i)
# 		time.sleep(0.01)

# for _ in range(2):
# 	x = threading.Thread(target=count, args=(10,))
# 	x.start()

# print("Done")

ls = []

def count(n):
	for i in range(1, n+1):
		ls.append(i)
		time.sleep(0.5)

def count2(n):
	for i in range(1, n+1):
		ls.append(i)
		time.sleep(0.5)

x = threading.Thread(target=count, args=(5,))
x.start()

x.join()

y = threading.Thread(target=count, args=(5,))
y.start()

y.join()

print(ls)

