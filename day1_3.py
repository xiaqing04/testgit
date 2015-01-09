# -*- coding: utf-8 -*-  

def search(key):

        import urllib2
        from bs4 import BeautifulSoup as BS
                
        print '*'*80      
        #observe the pattern of search url

        search_url='http://www.baidu.com/s?wd=%s' % urllib2.quote(key)
        html=urllib2.urlopen(search_url).read()
        soup = BS(html)
        urls =soup.findAll("h3", attrs={"class": ["t c-gap-bottom-small",'t'] }) # 匹配了所有标题信息。

        if len(urls) < 10:
                print "length is not enough!!!"
        else:
                print len(urls)

        f=open('result.txt','a+')
        for i in urls:
                f.write(str(i))
        f.close()
        
        
if __name__=='__main__':
        fd = file("query_1k.txt")        
        for key in fd.readlines():
                search(key)
        fd.close()
