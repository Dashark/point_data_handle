#############################################################
# 统计 + 过滤相似的点
# 序号：数量
# 序号：中心点
#############################################################

import math, sys, glob, os
from sympy import Point2D, Polygon


# 重叠面积
def overlap(rect1,rect2):
  xmin1,ymin1,xmax1,ymax1 = rect1;
  xmin2,ymin2,xmax2,ymax2 = rect2;
  xmin = max(xmin1,xmin2);
  ymin = max(ymin1, ymin2);
  xmax = min(xmax1, xmax2);
  ymax = min(ymax1, ymax2);
  if(xmin>=xmax or ymin >= ymax):
    return False;
  else:
    area1 = (xmax1-xmin1)*(ymax1-ymin1);
    area2 = (xmax2-xmin2)*(ymax2-ymin2);
    lap = (xmax-xmin)*(ymax-ymin);
    return lap/(area1+area2-lap);

def tag_region(line):
  regions = ((60,160,580,180),(560,160,580,470),(60,450,580,470),(60,160,80,470));
  index = 0;
  for reg in regions:
    ret = overlap(line[0:-2], reg);
    if(ret > 0.08):
      return index;
    index += 1;
  return -1;

def main():       
  dirs = ((3,1,1,1),(2,3,3,3),(2,3,3,3),(2,3,3,3));
  
  for file in glob.glob(sys.argv[1]+'/*.txt'):
    with open(file) as f:
      outfile,ext = os.path.splitext(file);
      f2 = open(outfile+'-region'+ext, 'w');
      while True:
        line = f.readline() # 按行读取数据
        if line:
          data = [round(x) for x in map(float, line.split())];
          reg = tag_region(data)
          if(reg != -1):
            f2.write(str(reg)+' '+line);
        else: break
      f2.close();
      f.close();

if __name__ == '__main__':
  main()