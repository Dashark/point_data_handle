##############################################################
# 切分数据，再把切分好的数据分别做排列组合
##############################################################

from itertools import product 

# 求中心点，返回中心点坐标
def getCenter(line):
	li = line.split()
	xmin = float(li[0])
	ymin = float(li[1])
	xmax = float(li[2])
	ymax = float(li[3])
	xcenter = xmin + (xmax - xmin) / 2
	ycenter = ymin + (ymax - ymin) / 2
	return (xcenter, ycenter)

file = input('Please input file name:') # 待处理的文件
dict1 = {} # {序号：中心点}

with open(file) as f:
	while True:
		line = f.readline() # 按行读取数据
		if line:
			num = int(line.split()[-1]) # 序号，int类型
			center = getCenter(line) # 中心点，tuple类型
			if num not in dict1.keys():
				dict1[num] = [] + [center]
			else:
				dict1[num] += [center]
		else:
			break

# 分片处理所有数据
def handle_all():
	# 数据分片，给定每组数据的行数
	data_rows = int(input('Please input each group\'s data rows:'))
	# 数据可以分为多少组
	groups = len(dict1) // data_rows

	num = 0 # 文件名后面的数字	
	key = 0 # 字典dict1的关键字
	for i in range(groups):
		li = [] # 把从字典中取出的每组数据放入列表中
		num += 1
		filename = 'output' + str(num) + '.txt' # 输出文件的文件名
		with open(filename, 'a') as f2:
			for j in range(data_rows):
				key += 1
				li.append(dict1[key])

			center = product(*li)	
			I = iter(center) # center坐标迭代器
			while True:
				try:
					x = next(I)
					f2.write(str(x) + '\n')
				except:
					break

# 选择指定的行数处理数据
def handle():
	li = []
	filename = input('Please input output file name:')
	start = int(input('Please input start:'))
	end = int(input('Please input end:'))
	with open(filename, 'a') as f:
		for key in range(start, end + 1):
			li.append(dict1[key])

		center = product(*li)	
		I = iter(center) # center坐标迭代器
		while True:
			try:
				x = next(I)
				f.write(str(x) + '\n')
			except:
				break

# 选择指定的行数处理数据,把每行数据写入一个文件
def handle2():
	li = []
	start = int(input('Please input start:'))
	end = int(input('Please input end:'))
	num = 0
	
	for key in range(start, end + 1):
		li.append(dict1[key])

		center = product(*li)	
		I = iter(center) # center坐标迭代器
		while True:
			try:
				num += 1
				filename = 'output' + str(num) + '.txt'
				with open(filename, 'a') as f:
					x = next(I)
					f.write(str(x) + '\n')
			except:
				break

if __name__ == '__main__':
	# handle_all()
	handle()