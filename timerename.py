import os,time
# 定位需要重命名的文件目录，获取文件列表信息
fileList = os.listdir("C:\\Users\\lijinrong\\Desktop\\nsfc")
# 将文件列表按系统修改时间排序
fileList.sort(key=lambda x: os.path.getmtime(os.path.join( "C:\\Users\\lijinrong\\Desktop\\nsfc", x)))
# 定义工作路径，即文件重命名后的保存路径
os.chdir("C:\\Users\\lijinrong\\Desktop\\nsfc")
# 名称变量
num = 0
# 遍历文件夹中所有文件
for filename in fileList:
    new_name = str(num+1)+filename[-5:]
    # 重命名文件,如果是需要进行复杂的重命名,则需要利用re与正则表达式.
    os.rename(filename, new_name)
    num = num+1
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'*'*5+'mission complete！！！')
# for fileName in fileList:
    # 匹配文件名正则表达式
    # pat = ".+\.(jpg)"
    # 进行匹配
    # pattern = re.findall(pat, fileName)
    # 文件重新命名
    # os.rename(fileName, ('picture '+ str(num + 1) + '.' + pattern[0]))
    # 改变编号，继续下一项
    # num = num + 1