import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

# 执行API调用并储存响应
url = "https://api.github.com/search/repositories?q=language:python&sort=starts"
r = requests.get(url)
print("Status code:", r.status_code)  # 状态码200表示响应成功

# 这个API返回JSON格式的信息，因此使用方法json()将这些信息转换为一个python字典
response_dict = r.json()
print("Total repositories returned:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
# print("Repositories returned:", len(repo_dicts))

#添加自定义工具提示
names,plot_dicts=[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict={
        'value':repo_dict['stargazers_count'],
        'label':repo_dict['description'],
        'xlink':repo_dict['html_url'], #将每个条形转为链接，点击任意条形，会打开一个新的页面，跳转到这个url上去
    }
    plot_dicts.append(plot_dict)

#显示醒目名称和stars数量
# names,stars=[],[]
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])
#可视化
#设置图表属性
my_style=LS('#333366',base_style=LCS)
my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False #隐藏图列
my_config.title_font_size=24 #图表标题字体大小
my_config.label_font_size=14 #副标签字体大小，x轴上的项目名和y轴上的大部分数字
my_config.major_label_font_size=18 #主标签字体大小，y轴上5000整数倍的刻度
my_config.truncate_label=15 #将项目名字较长的缩短为15个字符，鼠标指向项目名将会显示完整的名字
my_config.show_y_guides=False #隐藏水平线
my_config.width=1000

chart=pygal.Bar(my_config,style=my_style) #将实例my_config作为实参传递，从而通过一个实参传递所有配置设置
chart.title='Most-Starred Python Projects on Github'
chart.x_labels=names

chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')

# 研究第一个仓库，打印返回信息
# 要准确的直到API将返回哪些信息，要么阅读文档，要么像这样使用代码查看
# repo_dict=repo_dicts[0]
# print("\nKeys:",len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

#打印返回中仓库的某些关键信息
# print("\nSelected information about first repository:")
# for repo_dict in repo_dicts:
#     print('\nName:', repo_dict['name'])
#     print('Owner:', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Description:', repo_dict['description'])




