#############################################################
# 统计 + 过滤相似的点
# 序号：数量
# 序号：中心点
#############################################################

import math, sys, glob, os

dict1 = {} # {序号：中心点}
dict2 = {} # 存放没有处理过的点xmin,ymin,xmax,ymax
timespan = {} # 2帧之间的时间差

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

# 按面积过滤
def filt_area(line):
  global dict1, dict2, timespan
  
  pretime = 0;
  group = line.split()
  num = int(group[-1]) # 序号，int类型
  ctime = int(group[-2])
  center = getCenter(line)
  if num not in dict1.keys():
    dict2[num] = [tuple(group[0:-2])]
    # 目前把第一个矩形作为对比
    dict1[num] = [center]
    timespan[num] = [ctime-pretime]
    pretime = ctime
  else:
    xmin2 = float(group[0])
    ymin2 = float(group[1])
    xmax2 = float(group[2])
    ymax2 = float(group[3])
    count = 0
    for tup in dict2[num]:
      xmin1 = float(tup[0])
      ymin1 = float(tup[1])
      xmax1 = float(tup[2])
      ymax1 = float(tup[3])
      xmin = max(xmin1, xmin2)
      ymin = max(ymin1, ymin2)
      xmax = min(xmax1, xmax2)
      ymax = min(ymax1, ymax2)
      if xmin >= xmax: # 两个矩形没有重叠
        count += 1
      elif (xmax-xmin)*(ymax-ymin) <= 50: # 重叠面积过小
        count += 1
    if count == len(dict2[num]):
      dict1[num].append(center)
      dict2[num].append((xmin2, ymin2, xmax2, ymax2))

def main():       
  global dict1
  
  for file in glob.glob(sys.argv[1]+'/*.txt'):
    with open(file) as f:
      outfile,ext = os.path.splitext(file);
      while True:
        line = f.readline() # 按行读取数据
        if line:
          filt_area(line)
        else: break

      with open(outfile+'-filt'+ext, 'w') as f2:
        keys = sorted(dict1) # 排序
        for key in keys:
          f2.write(str(key) + ':' + str(dict1[key]) + '\n') 
        f2.close();

      with open(outfile+'-count'+ext, 'w') as f3:
        keys = sorted(dict1)
        for key in keys:
          f3.write(str(key) + ':' + str(len(dict1[key])) + ':' + str(timespan[key]) + '\n')
        f3.close();
      f.close();
      dict1.clear();

if __name__ == '__main__':
  main()