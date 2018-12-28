from pyquery import PyQuery as pq

html = '''
<div> 
<ul> 
<li class="item-0">first item</li> 
<li class="item-1"><a href="link2.html">second item</a></li> 
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li> 
<li class="item-1 active"><a href="link4.html">fourth item</a></li> 
<li class="item-0"><a href="links.html">fifth item</a></li> 
</ul> 
</div> 
'''
doc = pq(html)
print(doc('li'))

doc = pq(url='https://cuiqingcai.com')
#print(doc)
print(doc('title'))


doc = pq(filename='demo.html')
print(doc('li'))



html = '''
<div class="wrap"> 
<div id="container"> 
<ul class="list"> 
<li class="item-0">first item</li> 
<li class="item-1"><a href="link2.html">second item</a></li> 
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li> 
<li class="item-1 active"><a href="link4.html">fourth item</a></li> 
<li class="item-0"><a href="link5.html">fifth item</a></li> 
</ul> 
</div>
</div>
'''

doc = pq(html)
print(doc('#container .list li'))
print(type(doc('#container .list li')))

item = doc('.list')
print(type(item))
print(item)
lis = item.find('li')
print(type(lis))
print(lis)
print('*'*10)
lis = item.children('.active')
print(lis)



# items = doc('.list')
# container = items.parent()
# print(type(container))
# print(container)
print('*'*80)
items = doc('.list')
parents = items.parents()
print(type(parents))
print(parents)


print('*'*80)
items = doc('.list')
parents = items.parents('.wrap')
print(parents)

print('*'*80)

li = doc('.list .item-0.active')
print(li.siblings())


print('*'*80)

li = doc('.list .item-0.active')
print(li.siblings('.active'))



print('*'*80)
li = doc('.item-0.active')
print(li)
print(type(li))
print(str(li))


print('*'*80)
lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li,type(li))



print('*'*80)
a = doc('.item-0.active a')
print(a,type(a))
print(a.attr('href'))
print(a.attr.href)


a = doc('a')
print(a)
print(a.attr.href)
for item in a.items():
    print(item.attr('href'))
    print(item.text())
print('*'*80)


a = doc('.item-0.active a')
print(a.text())
li = doc('.item-0.active')
print(li)
print(li.html())
print('*'*80)

li = doc('li')
print(li.html())
print(type(li.text()),li.text())

print('*'*80)
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('avtive')
print(li)


html01 = '''
<ul class="list">
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''
doc01 = pq(html01)
li = doc01('.item-0.active')
print(li)
li.attr('name','link')
print(li)
li.text('changed item')
print(li)
li.html('<span>changed item</span>')
print(li)

print('*'*80)
doc = pq(html)
wrap = doc('ul')
print(wrap.text())
print('*'*80)

html03 = '''
<div class="warp">
hello world
<p>This is a paragraph.</p>
</div>
'''
doc02 = pq(html03)
warp = doc02('.warp')
warp.find('p').remove()
print(type(warp.text()),warp.text())


print('*'*80)
doc = pq(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(second)')
print(li)


