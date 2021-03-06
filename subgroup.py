#############################################################
# 统计 + 过滤相似的点
# 序号：数量
# 序号：中心点
#############################################################

import math, sys, os

def main():       
  file = sys.argv[1];#input('Please input inputFile name:') # 要处理的文件
  dir,filename = os.path.split(file);""#input('Please input outputFile1 name:') # 输出中心点  
  subdir = dir + '/subgroup';
  if( not os.path.exists(subdir)):
    os.mkdir(subdir);
  with open(file) as f:
    subfile = "";
    groupid = 0;
    pretime = 0;
    prenum = 0;
    subfile = subdir + '/groups' + str(groupid) + '.txt';
    while True:
      line = f.readline() # 按行读取数据

      if line:
        group = line.split();
        num = int(group[-2]) # 序号，int类型
        ctime = int(group[-3]);
        if num - prenum > 30:
          prenum = num;
          subfile = subdir + '/groups' + str(groupid) + '.txt';
          groupid += 1;
          with open(subfile,'a') as sf:
            sf.write(line);
            sf.close();
        else:
          with open(subfile,'a') as sf:
            sf.write(line);
            sf.close();
        pretime = ctime;
        prenum = num
      else:
        break

    f.close();

if __name__ == '__main__':
  main()