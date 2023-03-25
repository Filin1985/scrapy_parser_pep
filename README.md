# Проект парсинга документации Python

[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/-Scrapy-464646?style=flat&logo=Scrapy&logoColor=ffffff&color=043A6B)](https://www.djangoproject.com/)

## Описание проекта

Асинхронный парсер собирающий информацию данные с сайтов https://docs.python.org/3/ и https://peps.python.org/ и формирующий статистику по статусам всех PEP

**Используемые технологии**

- Python
- Scrapy

### Запуск проекта

1. Клонируем репозиторий

```
git clone https://github.com/Filin1985/scrapy_parser_pep
```

2. Устанавливаем виртуальное окружение

```
python3 -m venv venv
```

3. Активируем виртуальное окружение

```
source venv/bin/activate
```

4. Устанавливаем зависимости

```
pip install -r requirements.txt
```

5. Заходим в папку pep_parse

```
cd pep_parse
```

### Запуск парсеров

```
scrapy crawl pep
```

**Авторы: [ЯндексПрактикум](https://github.com/yandex-praktikum), [Марат Ихсанов](https://github.com/Filin1985)**
