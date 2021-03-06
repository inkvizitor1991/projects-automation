# Автоматизация командных проектов на [Devman](https://dvmn.org)

Делаем командный проект по автоматизации командных проектов. Заказчик – Илья Осипов, сотрудник онлайн-курсов Devman. Два раза в месяц он организует недельный проект для учеников курса, которые, в командах по 3 человека, разрабатывают какой-нибудь программный продукт. Разработка сопровождается созвонами по полчаса с продукт-менеджером каждый день, и эти созвоны приходится организовывать. Илья тратит по 4+ часов на опрос кому в какое время удобно заниматься, создает Discord-сервер, Trello-доски и т.д. Он хочет сократить время на организацию до часа максимум, желательно – свести организацию к запуску одного скрипта, идеально – сделать так, чтобы его участие вовсе более не требовалось.

## Как это работает

* `Телеграм бот` собирает от учеников их контактные данные и информацию о времени, когда им удобно работать над командным проектом.
* Собраная информация помещается во внутреннюю базу данных, доступ к которой имеет администратор, посредством `админки Django`.
* Внутренний алгоритм на `python` распределяет учеников, формируя команды.
* Автоматически генерируется `Trello-доска` по шаблону
* Автоматически генерируется `Discord-сервер` по шаблону

При создании нового trello по шаблону, происходят следующие действия:
- Создание рабочего пространства (workspace) trello.
- Ссылка на workspace сохраняется в бд. Доступ к объекту workspace можно получить через админку, перейдя в категорию `Trello workspaces` приложения `integrationapp`.
- Для каждой команды проекта, создается новая доска (board) внутри ранее созданого workspace.
- При наличии запроса на рассылку приглашений, каждому участнику проекта, на оставленный email отправляется ссылка приглашение к командному trello board.

## Как работает алгоритм распределения участников по группам и по ПМ

Все участники (новички, джуниоры, новички +3м) распределяются по командам из 3-ех человек, в команде джуниоров, присутствуют только джуниоры. Если участник проекта остался без группы,
он автоматически добавляется в одну из команд, состоящую из 3-ех человек, если же осталось 2 человека без группы, для них создается отдельная группа, состоящая из 2-ух человек.
Все команды распределены на 2 группы (участники первой недели и второй), у каждого ПМа максимально приблизительное число учеников(+-1), так же у каждого ПМа
максимально одинаковое число групп, как новичков, так и джуниоров.

### Для корректной работы алгоритма необходимо заполнить в админке

1) Названия проектов: week_1, week_2
2) Названия ПМов: Тим, Катя
3) Категории: Джуниор, Новичек, Новичек +3
4) Студенты (Обязательно заполнить поле `Категория`)

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Для реализации функции автоматической генерации trello по шаблону, заполните следующие переменные:
- `TRELLO_API_KEY` - получите [api ключ trello](https://trello.com/app-key) и установите его значение в текущее поле. Подробнее [здесь](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/).
- `TRELLO_SERVER_TOKEN` - на странице [api ключа trello](https://trello.com/app-key), по ссылке во фразе "generate a [Token]" получите серверный токен, после чего установите его значение в текущее поле.

## Запуск Django админки

- Для запуска сайта вам понадобится Python третьей версии.
- Скачайте репозиторий с кодом и прилегающими файлами.
- Установите зависимости командой `pip install -r requirements.txt`.
- Создайте базу данных SQLite командой `python3 manage.py migrate`.
- Создайте учетку администратора для админки Django командой `python3 manage.py createsuperuser`
- Запустите сервер разработчика командой `python3 manage.py runserver`.
- В браузере перейдите в админку по [адресу](http://127.0.0.1:8000/admin).

В случае успешного запуска, в консоль будет выведен ряд следующих уведомлений:
```
System check identified no issues (0 silenced).
September 29, 2021 - 12:00:38
Django version 3.2.7, using settings 'where_to_go.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

## Запуск автоматической генерации `Trello-доски` по шаблону

- Убедитесь что база данных корректно заполнена. Внутри содержится проект и команды с участниками проекта.
- В [админке](http://127.0.0.1:8000/admin) найдите нужный вам проект и перейдя в информацию о нем, скопируйте id.
- Для того, чтобы сгенерировать Trello шаблон для проекта, в браузере перейдите по ссылке `http://127.0.0.1:8000/integrations/trello/{project_id}`, где вместо `{project_id}` подставьте скопированный ранее id нужного проекта.
- Для того, чтобы разослать приглашения к доскам в трелло для участников проекта, в браузере перейдите по ссылке `http://127.0.0.1:8000/integrations/trello/{project_id}?send_email=True`, где вместо `{project_id}` подставьте скопированный ранее id нужного проекта, участникам которого требуется отправить приглашение.

## Запуск автоматической генерации `Discord-сервера` по шаблону

Полноценная версия генератора в разработке. Пока можно использовать файл `discord_lib.py` для просмотра текущих возможностей генератора. Для этого проделайте следующие действия:

- Создайте новое приложение discord (кнопка [New Application](https://discord.com/developers/applications)). Подробнее [здесь](https://discord.com/developers/docs/reference#authentication).
- Получите токен бота, пройдя [авторизацию](https://discord.com/developers/docs/reference#authentication)
- Добавьте полученный токен бота в переменные окружения файла `.env`, где `DISCORD_BOT_TOKEN=YOUR_TOKEN`.
- Запустите скрипт по работе с Discord командой `python3 integrationapp/utils/discord_lib.py`
- Клиент discord запустится, создаст сервер, приватную категорию, текстовый чат и ссылку приглашение, которую выведет в консоль. Созданная ссылка будет доступна в течение 30 секунд.
- Перейдите по ссылке и присоединитесь к созданному серверу в течение указанного выше времени.
- Если вы успели присоединиться, то по прошествии указанного времени у вас откроется доступ к созданному ранее приватному чату.

## Цели проекта

Код написан в рамках командного проекта учебной программы от [новичка до Middle](https://dvmn.org/t/middle-python-dev-before-you-finish-the-course/) на онлайн курсах обучению программирования python [Devman](https://dvmn.org/).
