#############################################################
# 统计 + 过滤相似的点
# 序号：数量
# 序号：中心点
#############################################################

import math, sys, getopt

def main():       
  opts,args = getopt.getopt(sys.argv[1:], "hi:o:")
  file = ""#input('Please input inputFile name:') # 要处理的文件
  file2 = ""#input('Please input outputFile1 name:') # 输出中心点  
  for op, value in opts:
    if op == "-i":
      file = value
    elif op == "-o":
      file2 = value
    elif op == "-h":
      usage()
      sys.exit()
  with open(file) as f:
    subfile = "";
    groupid = 0;
    pretime = 0;
    prenum = 0;
    while True:
      line = f.readline() # 按行读取数据

      if line:
        group = line.split();
        num = int(group[-1]) # 序号，int类型
        ctime = int(group[-2]);
        if(num != prenum and ctime - pretime > 100000):
          prenum = num;
          subfile = file2 + str(groupid) + '.txt';
          groupid += 1;
          with open(subfile,'a') as sf:
            sf.write(line);
            sf.close();
        else:
          with open(subfile,'a') as sf:
            sf.write(line);
            sf.close();
        pretime = ctime;
      else:
        break

    f.close();

if __name__ == '__main__':
  main()