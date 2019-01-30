from pyecharts import WordCloud

name1 = [
    'java', 'python', 'shell', 'junit', 'testng', 'selenium', 'appium', 'jmeter', 'sql', 'hadoop', 'jenkins'
 ]
value1 = [
    20, 10, 10, 5, 5, 10, 5, 10, 10, 10, 5
 ]
wordcloud1 = WordCloud(width=1300, height=620)
wordcloud1.add("", name1, value1, word_size_range=[50, 150])
wordcloud1.render("word_cloud1.html")

name2 = [
    '功能测试', '接口测试', '性能测试', '标签测试', '文档编写', '过程改进', '技术研究', '知识分享', '工具应用', '环境维护'
]
value2 = [
    10, 10, 5, 30, 10, 5, 10, 10, 5, 5
]
wordcloud2 = WordCloud(width=1300, height=620)
wordcloud2.add("", name2, value2, word_size_range=[50, 150])
wordcloud2.render("word_cloud2.html")