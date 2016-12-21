#############################################################
# 统计 + 过滤相似的点
# 序号：数量
# 序号：中心点
#############################################################

import math, sys, getopt

dict1 = {} # {序号：中心点}

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

# 过滤相似的点，如果相似，返回None
def filt(center, num):
  global dict1
  count = 0 # 统计比较了多少次
  # 两点之间的距离
  for tup in dict1[num]:
    leng = math.sqrt((center[0]-tup[0])**2 + (center[1]-tup[1])**2)
    if leng < 50:
      break
    else:
      count += 1
  if count == len(dict1[num]):
    return center
  return []

def main():       
  global dict1
  opts,args = getopt.getopt(sys.argv[1:], "hi:o:c:")
  file = ""#input('Please input inputFile name:') # 要处理的文件
  file2 = ""#input('Please input outputFile1 name:') # 输出中心点  
  file3 = ""#input('Please input outputFile2 name:') # 输出数量
  for op, value in opts:
    if op == "-i":
      file = value
    elif op == "-o":
      file2 = value
    elif op == "-c":
      file3 = value
    elif op == "-h":
      usage()
      sys.exit()
  with open(file) as f:
    while True:
      line = f.readline() # 按行读取数据

      if line:
        num = int(line.split()[-1]) # 序号，int类型
        center = getCenter(line) # 中心点，tuple类型
        if num not in dict1.keys():
          dict1[num] = [center]
        else:
          center = filt(center, num) #过滤
          if center != []:
            dict1[num].append(center)
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

if __name__ == '__main__':
  main()