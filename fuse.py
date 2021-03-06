#############################################################
# 统计 + 过滤相似的点
# 序号：数量
# 序号：中心点
#############################################################

import math, sys, glob, os
from sympy import Point2D, Polygon

class Tracking:
  __regions = ((60,160,580,180),(560,160,580,470),(60,450,580,470),(60,160,80,470));
  __region0 = [];
  __region1 = ();
  __region2 = ();
  __region3 = ();
  
  def fuse(self,rect):
    if(len(self.__region0)==0):
      self.__region0.append(rect);
    else:
      tmp = [rect if self.overlap(rect,reg)>0.4 else reg for reg in self.__region0];
      if rect not in tmp:
        tmp.append(rect)
      #print(tmp)
      self.__region0 = list(tmp);
      #for pre in self.__region0:
       # lap = self.overlap(rect, pre);
        #if(lap > 0.7):
         # self.__region0[self.__region0.index(pre)] = rect;
          #break;
    return self.__region0;
      
  def clear(self):
    self.__region0.clear();
  
  # 重叠面积
  def overlap(self, rect1,rect2):
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

  # 中心点距离
  def distance(self, rect1, rect2):
    xmin1,ymin1,xmax1,ymax1 = rect1;
    xmin2,ymin2,xmax2,ymax2 = rect2;
    xcenter1 = xmin1 + (xmax1 - xmin1) / 2
    ycenter1 = ymin1 + (ymax1 - ymin1) / 2
    xcenter2 = xmin2 + (xmax2 - xmin2) / 2
    ycenter2 = ymin2 + (ymax2 - ymin2) / 2
    return math.sqrt((xcenter1-xcenter2)**2+(ycenter1-ycenter2)**2)

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

  track = Tracking();
  for file in glob.glob(sys.argv[1]+'/*region.txt'):
    with open(file) as f:
      outfile,ext = os.path.splitext(file);
      f2 = open(outfile+'-fuse'+ext, 'w');
      pre_region = -1;
      #region = [];
      for line in f.readlines(): # 按行读取数据
        data = [round(x) for x in map(float, line.split())];
        if pre_region == -1:
          pre_region = data[0]
          region = track.fuse(data[1:-2]);
        elif data[0] == pre_region :
          region = track.fuse(data[1:-2])
        else:
          f2.write(str(pre_region) + ' ' + str(region)+'\n');
          track.clear();
          region = track.fuse(data[1:-2]);
          pre_region = data[0];
      f2.write(str(pre_region) + ' ' + str(region)+'\n');
      track.clear();
      f2.close();
    f.close();

if __name__ == '__main__':
  main()