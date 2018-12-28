from bs4 import BeautifulSoup
import re

html = ''' 
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4> 
</div> 
<div class="panel-body"> 
<ul class="list" id="list-1" name='elements'>
<li class="element">Foo</li> 
<li class="element">Bar</li> 
<li class="element">Jay</li> 
</ul> 
<ul class="list list-small" id ＝"list-2">
<li class="element">Foo2</li> 
<li class="element">Bar</li> 
</ul> 
</div> 
</div>
'''


soup = BeautifulSoup(html,'lxml')
print(soup.find_all(name='ul'))
print(type(soup.find_all(name='ul')[0]))
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)


print('*' * 50)

print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))

print(soup.find_all(id='list-1'))
print(soup.find_all(class_='element'))


html1 = '''
<div class="panel"> <div class="panel-body">
<a>Hello, this is a link</a> 
<a>Hello, this is a link, too</a> 
</div> 
</div> 
'''
soup1 = BeautifulSoup(html1,'lxml')
print(soup1.find_all(text=re.compile('link')))

print('*'*80)

print(soup.find(name='ul'))
#print(type(soup.find(name='ul')))
#print(soup.find(class_='list'))
print('*'*80)
html2 = '''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4> 
</div> 
<div class="panel-body">
<ul class="list" id="list-1"> 
<li class="element">Foo<lli> 
<li class="element">Bar</li> 
<li class="element">]ay</li>
</ul> 
<ul class="list1 list-small" id="list-2"> 
<li class="element">Foo1</li> 
<li class="element">Bar</li> 
</ul> 
</div> 
</div> 
'''

soup2 = BeautifulSoup(html2,'lxml')
print(soup2.select('.panel .panel-heading'))
print(soup2.select('ul li'))
print(soup2.select('#list-2 .element'))
print(soup2.select('#list-2 .element'))
print(soup2.select('ul')[0])
print('*'*50)

for ul in soup2.select('ul'):
    print(ul.select('li'))
    print(ul['id'])
    print(ul.attrs['id'])
print('*'*50)
for li in soup2.select('li'):
    print('Get Text:',li.get_text())
    print("String:",li.string)