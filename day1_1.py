# -*- coding: utf-8 -*-  
import re
from urlparse import urlparse  
topHostPostfix = (
    '.com', '.cn','.info','.net','.org','.us','.com.cn','.net.cn',
    '.org.cn','.tw','.hk', ".com.hk")

regx = r'[^\.]+('+'|'.join([h.replace('.',r'\.') for h in topHostPostfix])+')$'
#regx = r'('+'|'.join([h.replace('.',r'\.') for h in topHostPostfix])+')$'
# 匹配的原则是 除了. 之外  然后以上述的字符串结尾。

pattern = re.compile(regx,re.IGNORECASE) #忽略大小写
print "--"*40

fd = file("url.list")
i = 1

for url in fd.readlines():
        
    parts = urlparse(url)  #将网址分成一个元祖。 如果这里没有发现Http://

    if parts.netloc is not '':
        host = parts.netloc
    else :
        host = parts.path

    m = pattern.search(host)   #对主域 www.baidu.com　　re.search函数会在字符串内查找模式匹配,
                                    #只到找到第一个匹配然后返回，如果字符串没有匹配，则返回None。
    res =  m.group() if m else host

    print i,':',
    i = i + 1
    
    print "unkonw!" if not res else res

fd.close()


 
