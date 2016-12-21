#############################################################
#   统计
# 序号：数量
# 序号：中心点
#############################################################

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

file = input('Please input inputFile name:') # 要处理的文件
file2 = input('Please input outputFile1 name:') # 输出中心点
file3 = input('Please input outputFile2 name:') # 输出数量
with open(file) as f:
	dict1 = {} # {序号：中心点}

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

	with open(file2, 'a') as f2:
		keys = sorted(dict1) # 排序
		for key in keys:
			f2.write(str(key) + ':' + str(dict1[key]) + '\n') 

	with open(file3, 'a') as f3:
		keys = sorted(dict1)
		for key in keys:
			f3.write(str(key) + ':' + str(len(dict1[key])) + '\n')