a = int(input())
tub = 1
for i in range(2, a//2+1):
    if a %  i == 0:
	tub = 0
	break
    else:
	tub = 1
if tub == 1:
    print("tub son")
else:
    print("tub son emas")
