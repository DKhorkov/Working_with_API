import requests
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# Обработка результатов:
response_dict = r.json()
# print(response_dict.keys())  # Обработка результатов.
repo_dicts = response_dict['items']
repo_links, stars, descriptions = [], [], []
for repo_dict in repo_dicts:
    # for key in sorted(repo_dict.keys()):
    #     print(key)

    # Plotly позволяет использовать разметку HTML: "<br />" - (break) разрыв строки.
    # <a href="URL">текст ссылки</a> - Создает гиперссылку на проект.
    repo_links.append(f'<a href="{repo_dict["html_url"]}">{repo_dict["name"]}</a>')
    descriptions.append(f'{repo_dict["owner"]["login"]}<br />{repo_dict["description"]}')
    stars.append(repo_dict['stargazers_count'])


# Построение визуализации:
data = [{'type': 'bar',
         'x': repo_links,
         'y': stars,
         'hovertext': descriptions,  # Подсказка пользователю при наведении на столбец (будет описание проекта). Если
         # использовать "text" вместо "hovertext", то описание будет также выведено внутри столбца.
         'opacity': 0.8,
         'marker': {'color': 'rgb(120, 120, 255)',  # Настройка цвета столбца.
                    'line': {'width': 4, 'color': 'rgb(100, 50, 50)'}}  # Настройки линии-контура около столбца.
         }]
my_layout = {'title': 'Most-Starred python projects on GitHub',
             'titlefont': {'size': 28, 'color': 'blue'},  # Установка цвета и размера заголовка диаграммы.
             'xaxis': {'title': 'Repo names',
                       'titlefont': {'size': 24,  # Установка размера и цвета наименования осей диаграммы.
                                     'color': 'red'}
                       },
             'yaxis': {'title': 'Stars',
                       'titlefont': {'size': 24,  # Установка размера и цвета наименования осей диаграммы.
                                     'color': 'red'}
                       },
             }
offline.plot({'data': data, 'layout': my_layout})
