list = []
#读取A文件（txt）
with open(r'c:\Users\Admin\Desktop\1.txt',encoding='utf-8') as file:
    s = file.readlines()
    list.extend(s)
list.sort()
print(list)
#写入B文件（txt）
fp = open(r'c:\Users\Admin\Desktop\2.txt','w',encoding='utf-8')
fp.writelines(list)
fp.close()
