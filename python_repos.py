# Программа по вызову API для поиска на сайте "github" проектов на языке "python" с наибольшим кол-вом звезд.

# https://starkovden.github.io/course-overview.html - информация по API.

# https://api.github.com/rate_limit - сведения о количестве доступных запросов в определенный отрезок времени.

# https://api.github.com/search/repositories?q=language:python&sort=stars:
  # https://api.github.com/ - передача сайту запроса на вызов API;
  # search/repositories - приказ апи выдать инфу по всем репозиториям;
  # "?" - символ для передачи аргумента нашему запросу;
  # q=language:python - "q" - Query (запрос) равняется яызку программирования питон
  # &sort=stars - а также отсортировать по количеству звезд.

import requests

# Создание вызова API и сохранение ответа:
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}  # Определение заголовков.
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')  # Код 200 - признак успешного ответа.

response_dict = r.json()  # Сохранение ответа API в переменной. Поскольку данные в формате json, то и вызов json.
print(response_dict.keys())  # Обработка результатов.
print(f'Total number of repositories is {response_dict["total_count"]}.')

# Анализ информации о репозиториях:
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

# Анализ первого репозитория:
print('\nFSelected information about each repo:')
for repo_dict in repo_dicts:

    # Информация о ключах словаря:
    # print(f'Keys: {len(repo_dict)}.', end='\n\n')
    # for key in sorted(repo_dict.keys()):
    #     print(key)

    print(f'Name: {repo_dict["name"]}')
    print(f'Owner: {repo_dict["owner"]["login"]}')
    print(f'Stars: {repo_dict["stargazers_count"]}')
    print(f'Repo: {repo_dict["url"]}')
    print(f'Created: {repo_dict["created_at"]}')
    print(f'Description: {repo_dict["description"]}', end='\n\n')
