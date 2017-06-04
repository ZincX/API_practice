#coding: utf-8
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort-stars'
r = requests.get(url)
print("Status code:", r.status_code)

#将API响应存储到一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

#探索有关仓库的信息
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])

	if repo_dict['description'] == None:
		plot_dict = {
			'value': repo_dict['stargazers_count'], 
			'label': 'hahaha'
			}
	else:
		plot_dict = {
			'value': repo_dict['stargazers_count'], 
			'label': repo_dict['description']
			}

	plot_dicts.append(plot_dict)

print(plot_dicts)
print(len(plot_dicts))
print(len(names))
print(names)
#可视化
my_style = LS('#336699', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

#chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos_plot_dicts.svg')
#chart.add('', plot_dicts)
#chart.render_to_file('bar_descriptionss.svg')