from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
import logging

logger = logging.getLogger(__name__)


def main(request):
    logger.info('Visited main page')
    about_url = reverse('about')
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>How to Make an Application in Django</title>
        <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
        <style>
            body {{
                background-color: #3776AB;
                color: #F5F5F5;
                font-family: 'Roboto', sans-serif;
                font-size: 16px;
                line-height: 1.5;
                margin: 0;
                padding: 0;
            }}
            h1 {{
                color: #FFD43B;
                font-size: 48px;
                font-weight: bold;
                margin: 50px 0 20px;
                text-align: center;
                text-shadow: 2px 2px #306998;
            }}
            h2 {{
                color: #F5F5F5;
                font-size: 36px;
                font-weight: bold;
                margin: 30px 0 10px;
                text-shadow: 1px 1px #306998;
            }}
            p {{
                margin: 10px 0;
            }}
            code {{
                background-color: #F5F5F5;
                color: #306998;
                font-family: Consolas, monospace;
                font-size: 14px;
                padding: 2px 4px;
            }}
            button {{
                background-color: #FFD43B;
                border: none;
                border-radius: 4px;
                color: #306998;
                cursor: pointer;
                font-family: 'Roboto', sans-serif;
                font-size: 16px;
                font-weight: bold;
                margin-top: 20px;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                text-shadow: 1px 1px #F5F5F5;
                transition: background-color 0.3s ease;
            }}
            button:hover {{
                background-color: #F5F5F5;
                color: #306998;
            }}
        </style>
    </head>
    <body>
<h1>Как создать приложение в Django</h1>
        <h2>Шаг 1: Создание проекта Django</h2>
        <p>Для создания нового проекта Django откройте терминал и выполните следующую команду:</p>
        <code>django-admin startproject project_name</code>
        <p>Это создаст новый каталог с именем <code>project_name</code> с базовой структурой проекта Django.</p>
        <h2>Шаг 2: Создание приложения Django</h2>
        <p>Для создания нового приложения Django перейдите в каталог проекта и выполните следующую команду:</p>
        <code>python manage.py startapp app_name</code>
        <p>Это создаст новый каталог с именем <code>app_name</code> с базовой структурой приложения Django.</p>
        <h2>Шаг 3: Определение моделей</h2>
        <p>Определите модели данных для вашего приложения в файле <code>models.py</code> вашего приложения. 
        Используйте ORM Django для определения моделей и их отношений.</p>
        <h2>Шаг 4: Создание представлений</h2>
        <p>Создайте представления для вашего приложения в файле <code>views.py</code> вашего приложения. 
        Представления обрабатывают запросы и возвращают ответы, обычно в виде HTML-шаблонов.</p>
        <h2>Шаг 5: Определение URL-адресов</h2>
        <p>Определите URL-адреса для вашего приложения в файле <code>urls.py</code> вашего приложения. 
        Сопоставьте URL-адреса с представлениями, используя регулярные выражения.</p>
        <h2>Шаг 6: Создание шаблонов</h2>
        <p>Создайте HTML-шаблоны для вашего приложения в каталоге <code>templates</code> вашего приложения. 
        Используйте язык шаблонов Django для отображения динамического контента.</p>
        <a href="{about_url}"><button>Обо мне</button></a>
    </body>
    </html>
    """
    return HttpResponse(html)


def about(request):
    logger.info('Visited about page')
    html = """
    <style>
        body {
            background-color: #0F0F0F;
            color: #FFFFFF;
            font-family: 'Helvetica Neue', sans-serif;
            font-size: 16px;
        }
        h1 {
            color: #FFFFFF;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            margin-top: 50px;
        }
        p {
            margin-top: 30px;
            font-size: 20px;
            line-height: 1.5;
        }
        .logo {
            position: absolute;
            top: 20px;
            right: 20px;
            width: 100px;
        }
    </style>
    <h1>Ну не совсем обо мне)</h1>
    <p>Имя: Илон Маск<br>
    Дата рождения: 28 июня 1971 г.<br>
    Место рождения: Претория, Южно-Африканская Республика</p>

    <p><strong>Физическое описание:</strong><br>
    Рост: 188 см<br>
    Вес: неизвестен<br>
    Цвет волос: коричневый<br>
    Цвет глаз: голубой</p>

    <p><strong>Род деятельности:</strong><br>
    Предприниматель<br>
    Генеральный директор SpaceX<br>
    Генеральный директор Tesla, Inc.<br>
    Генеральный директор Neuralink<br>
    Сооснователь OpenAI</p>

    <p><strong>Известные партнеры:</strong><br>
    Сотрудники SpaceX<br>
    Сотрудники Tesla<br>
    Различные деловые партнеры и инвесторы<br>
    Знаменитости и общественные деятели</p>

    <p><strong>Судимости:</strong><br>
    Нет</p>

    <p><strong>Биография:</strong><br>
    Маск учился в Университете Претории, а затем переехал в США, чтобы поступить в Университет Пенсильвании.<br>
    Он соосновал Zip2, веб-компанию, которая позже была продана за почти $300 миллионов.<br>
    Маск затем соосновал PayPal, онлайн-платежную систему, которая была продана eBay за $1,5 миллиарда.<br>
    Он основал SpaceX в 2002 году с целью сделать космические полеты более доступными и доступными.<br>
    Маск также основал Tesla, Inc. в 2003 году с целью производства электромобилей, 
    которые являются практичными и желанными.<br>
    В дополнение к своей работе в SpaceX и Tesla, Маск основал Neuralink, компанию, занимающуюся разработкой 
    интерфейсов мозг-машин, и соосновал OpenAI, исследовательскую компанию, 
    специализирующуюся на искусственном интеллекте.</p>

    <p><strong>Примечания:</strong><br>
    Маск известен своими амбициозными целями и готовностью рисковать.<br>
    Он был замешан в нескольких скандалах, включая иск о клевете и критику своего стиля управления.<br>
    Маск имеет большую аудиторию в социальных сетях и известен своими откровенными и иногда 
    контроверзными заявлениями.<br>
    Он был назван одним из самых влиятельных людей в мире журналами Time и Forbes.</p>

    <p>Меня зовут Кобзев Алексей. Мне 35 лет. Я из Казани. Это мой первый сайт на Django.</p>
    <img class="logo" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeZn2T-0PNBGrSWhix1KzoyktyQHBWu3lYig&usqp=CAU" alt="GeekBrains Logo">
    """
    return HttpResponse(html)