import sys

def main():
	n,k = map(int, input().split())
	tasks = [int(x) for x in input().split()]
	#tasks = list(map(int, input().split()))
	dic = set(tasks)
	cntcst = list(dic)

	if len(dic) < k:
		for task in tasks:
			if task in dic:
				dic.remove(task)
			else:
				cntcst.append(task)

	print(*cntcst[:k])
if __name__ == '__main__':
    main()