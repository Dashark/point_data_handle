#############################################################
# 统计 + 过滤相似的点
# 序号：数量
# 序号：中心点
#############################################################

import math, sys, glob, os

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
  timespan = {} # 2帧之间的时间差
  pretime = 0;
  for file in glob.glob(sys.argv[1]+'/*.txt'):
    with open(file) as f:
      outfile,ext = os.path.splitext(file);
      while True:
        line = f.readline() # 按行读取数据

        if line:
          group = line.split();
          num = int(group[-1]) # 序号，int类型
          ctime = int(group[-2]);
          center = getCenter(line) # 中心点，tuple类型
          if num not in dict1.keys():
            dict1[num] = [center]
            timespan[num] = [ctime-pretime];
            pretime = ctime;
          else:
            center = filt(center, num) #过滤
            if center != []:
              dict1[num].append(center)
        else:
          break

      with open(outfile+'-filt'+ext, 'w') as f2:
        keys = sorted(dict1) # 排序
        for key in keys:
          f2.write(str(key) + ':' + str(dict1[key]) + '\n') 
        f2.close();

      with open(outfile+'-count'+ext, 'w') as f3:
        keys = sorted(dict1)
        for key in keys:
          len1 = len(dict1[key]);
          if len1 > 1:
            f3.write(str(key) + ':' + str(len1) + ':' + str(timespan[key]) + '\n')
        f3.close();
      f.close();
      dict1.clear();

if __name__ == '__main__':
  main()