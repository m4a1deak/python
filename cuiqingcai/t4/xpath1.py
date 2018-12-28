from lxml import etree


text = ''' 
<div> 
<ul>
<li class="item-3"><a href="link5.html">fifth item</a>
<li class="item-1">< a href="link2.html">second item</a></li> 
<li class="item-inactive"><a href="link3.html">third item</a></li> 
<li class="item-1"><a href="link4.html">fourth item</a></li> 
<li class="item-2"><a href="link5.html">fifth item</a> 
</ul> 
</div>
'''

html = etree.HTML(text)
result = etree.tostring(html)
print(type(html))
print(type(result))
#print(result.decode('utf-8'))
print('*' * 50)

html = etree.parse('test.html',etree.HTMLParser())
#result = etree.tostring(html)
#print(result.decode('utf-8'))
result = html.xpath('//*')
print(result)
result = html.xpath('//li')
print(result)
print(result[0])

result = html.xpath('//ul//a')
print(result)
print('*' * 50)

result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)

result = html.xpath('//li[@class="item-0"]')
print(result)


result = html.xpath('//li[@class="item-0"]/text()')
print(result)

result = html.xpath('//li[@class="item-0"]//text()')
print(result)

result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)

result = html.xpath('//li/a/@href')
print(result)


text = '''
<li class="li li-first"><a href="link2.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[@class="li"]/a/text()')
print(result)
result = html.xpath('//li[contains(@class,"li")]/a/text()')
#print(etree.tostring(html))
print(result)



text = '''
<li class="li li-first" name="item"><a href="link2.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
print(result)



text = '''                                                           
<div>                                                                
<ul>                                                                 
<li class="item-3"><a href="link5.html">first item</a>               
<li class="item-1">< a href="link2.html">second item</a></li>        
<li class="item-inactive"><a href="link3.html">third item</a></li>   
<li class="item-1"><a href="link4.html">fourth item</a></li>         
<li class="item-2"><a href="link5.html">fifth item</a>               
</ul>                                                                
</div>                                                               
'''
print(text)
html = etree.HTML(text)
result = etree.tostring(html)
print(type(result))
print(result.decode('utf-8'))

result = html.xpath('//li[1]/a/text()');
print(result)
result = html.xpath('//li[last()]/a/text()');
print(result)
result = html.xpath('//li[position()>3]/a/text()');
print(result)
result = html.xpath('//li[last()-2]/a/text()');
print(result)




text = '''                                                           
<div>                                                                
<ul>                                                                 
<li class="item-0"><a href="link1.html"><span>first item</span></a>               
<li class="item-1"><a href="link2.html">second item</a></li>        
<li class="item-inactive"><a href="link3.html">third item</a></li>   
<li class="item-1"><a href="link4.html">fourth item</a></li>         
<li class="item-0"><a href="link5.html">fifth item</a>               
</ul>                                                                
</div>                                                               
'''
html = etree.HTML(text)
result = html.xpath("//li[1]/ancestor::*")
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print(result)
result = html.xpath('//li[1]/following::*')
print(result)
result = html.xpath('//li[1]/following-sibling::*')
print(result)