from scrapy.selector import  Selector
from scrapy.http import HtmlResponse

body='''
<html>
    <head>
        <base href='http://example.com/'/>
        <title>Example website</title>
    </head>
    <body>
        <div id='images'>
            <a href='image1.html'>Name:Image1<br/><img src='image1.jpg'/></a>
            <a href='image2.html'>Name:Image2<br/><img src='image2.jpg'/></a>
            <a href='image3.html'>Name:Image3<br/><img src='image3.jpg'/></a>
            <a href='image4.html'>Name:Image4<br/><img src='image4.jpg'/></a>
            <a href='image5.html'>Name:Image5<br/><img src='image5.jpg'/></a>
        </div>
    </body>
</html>
'''

response=HtmlResponse(url='http://www.example.com',body=body,encoding='utf8')

print(response.xpath('/html'))#描述从根节点开始绝对路径
print(response.xpath('/html/head'))#描述从根节点开始绝对路径
print(response.xpath('/html/body/div/a'))#选中双亲节点中的所有子节点
print(response.xpath('//a'))#选中所有a节点
print(response.xpath('/html//img'))#选中后代中的所有img节点
res=response.xpath('//a/text()')#选中文本子节点
print(res.extract())
print(response.xpath('/html/*'))#选中所有子节点
print(response.xpath('/html/body/div//*'))#选中所有后代节点
print(response.xpath('//div/*/img'))#选中所有孙节点中的img节点
print(response.xpath('//img/@src'))#选中所有img的src属性节点
print(response.xpath('//@href'))#选中所有href属性节点
print(response.xpath('//div/@*'))#选中所有孙节点中所有属性
