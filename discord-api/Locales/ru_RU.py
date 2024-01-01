#   Tinelix Microbot
#   -------------------------------------------------------------------------------------------
#   Copyright © 2023 Dmitry Tretyakov (aka. Tinelix)
#
#   This program is free software: you can redistribute it and/or modify it under the terms of
#   the GNU Affero General Public License 3 (or any later version) and/or Apache License 2
#   See the following files in repository directory for the precise terms and conditions of
#   either license:
#
#       LICENSE.APACHE
#       LICENSE.AGPL
#
#   Please see each file in the implementation for copyright and licensing
#   information, (in the opening comment of each file).

def _tr(where, str):
    locale = {}
    if where == "message":
        locale = {
            'prefix': '**Префикс:** `{0}`\r\nПоддерживаются также слэш-команды.'
        }
    elif where == "embed_title":
        locale = {
            'error': '❎ Ошибка',
            'help': '❔ Справка',
            'cmd_help': 'Команда `{0}`',
            'fatalerr_reporter': '🛠 У нас что-то сломалось!',
            'about': '🤖 О боте',
            'user': '👤 {0} / {1}',
            'user2': '👤 {0}',
            'user_bot': '🤖 {0} / {1}',
            'user_bot2': '🤖 {0}',
            'user_owner': '👑 {0} / {1}',
            'user_owner2': '👑 {0}',
            'avatar': '🖼 Аватар пользователя {0}',
            'forbidden': '🚫 Доступ запрещен',
            'eval': '⌨ Интерпретатор',
            '8ball': '🎱 Генератор случайных ответов',
            'rngen': '🎱 Генератор случайных чисел',
            'calc': '🔢 Калькулятор',
            'settings': '⚙ Настройки',
            'msg_author': '📣 Публикация от {0} / @{1}',
            'ping': '🏓 Понг!',
            'weather': '⛅ Погода',
            'weather2': '⛅ {0}, {1}',
            'wikipedia': '🌐 Википедия',
            'codec': '🔡 Кодек',
            'timers': '⏲️ Таймеры',
        }
    elif where == "embed_description":
        locale = {
            'help': '**{0}** - простейший и компактный бот для Discord.\r\nХотите узнать, для чего нужны команды? Вбейте `{1}help [имя команды]`.\r\n[Пригласить]({2})',
            'error_unf': '😔 Пользователь не найден. Попробуйте найти другого пользователя.',
            'fatalerr_reporter': '🪲 Да, у нас и такое случается. Но ничего страшного, скоро мы это отремонтируем.',
            'forbidden': '🚫 Вы не имеете права пользоваться этой командой!',
            'please_wait': '⌛ Подождите...',
            'settings_done': '✅ Готово!',
            'publish_isntcomm': '❌ Сервер не обладает функциями сообщества. Включите в настройках сервера.',
            'publish_isntnewsch': '❌ Канал не является новостным каналом или каналом с объявлениями. Включите в настройках канала.',
            'weather_conditions_200': '**⛈ Гроза с умеренным дождем**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
            'weather_conditions_201': '**⛈ Гроза с дождем**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
            'weather_conditions_202': '**⛈ Гроза с ливнем**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
            'weather_conditions_300-321': '**🌨 Гололедица**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
            'weather_conditions_500-501': '**🌧 Умеренный дождь**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
            'weather_conditions_502': '**🌧 Дождь**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/) на_',
            'weather_conditions_503-504': '**🌧 Ливень**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
            'weather_conditions_511': '**🌧 Дождь**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
            'weather_conditions_600-601': '**🌨 Снег**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
            'weather_conditions_602': '**🌨 Метель**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
            'weather_conditions_615-616': '**🌨 Дождь со снегом**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
            'weather_conditions_800': '**☀ Солнечно**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
            'weather_conditions_801': '**🌤 Малооблачно**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
            'weather_conditions_802-803': '**⛅ Облачно**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
            'weather_conditions_804': '**☁ Пасмурно**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
            'weather_sconditions_200': '⛈ Гроза с умеренным дождем',
            'weather_sconditions_201': '⛈ Гроза с дождем',
            'weather_sconditions_202': '⛈ Гроза с ливнем',
            'weather_sconditions_300-321': '🌨 Гололедица',
            'weather_sconditions_500-501': '🌧 Умеренный дождь',
            'weather_sconditions_502': '🌧 Дождь',
            'weather_sconditions_503-504': '🌧 Ливень',
            'weather_sconditions_511': '🌧 Дождь',
            'weather_sconditions_600-601': '🌨 Снег',
            'weather_sconditions_602': '🌨 Метель',
            'weather_sconditions_615-616': '🌨 Дождь со снегом',
            'weather_sconditions_800': '☀ Солнечно',
            'weather_sconditions_801': '🌤 Малооблачно',
            'weather_sconditions_802-803': '⛅ Облачно',
            'weather_sconditions_804': '☁ Пасмурно',
            'query_notfound': '😔 К сожалению, мы ничего не нашли. Может, попробуете другой запрос?',
            'wikipedia': '{0}\r\n[Подробнее...]({1})',
            'timers': '⏲️ Тут ничего нет, но вы можете создать хоть один таймер.',
            'timers_created': '✅ Таймер создан.',
            'timers_deleted': '✅ Таймер удален.',
            'timers_invelapsdt': '❌ Указанная дата должна быть не позднее сегодняшней!',
            'timers_invupcomdt': '❌ Указанная дата должна быть не раньше сегодняшней!',
            'tz_invalidabbr': '❌ Вы ввели неверное обозначение часового пояса. Смотрите [по ссылке](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) (столбец Notes) для подробной информации.',
            'invalid_cmd_usage': 'Вы используете эту команду неправильно или не указали одно из требуемых параметров. Смотрите её синтаксис и пример.',
            'cmd_not_found': '❌ Запрашиваемая вами команда не предусмотрена. Возможно, [вы что-то предложите разработчику]({0})?',
            'cmd_not_found2': '❌ Запрашиваемая вами команда не предусмотрена. Возможно, вы что-то предложите разработчику?'
        }
    elif where == "embed_fields":
        locale = {
            'help_preff': 'Префиксы',
            'help_prefv': '{0} или `/`',
            'help_cmdsf': 'Команды',
            'help_cmdsv': '{0}',
            'help_exampf': 'Пример',
            'help_aliasf': 'Аналогичные названия',
            'eval_codelf': 'Листинг',
            'eval_resulf': 'Результат',
            'about_versf': 'Версия',
            'about_versf2': 'На основе {0}',
            'about_versv': '{0} ({1})',
            'about_devsf': 'Разработчик',
            'about_devsv': '{0} / _`{1}`_',
            'about_regdf': 'Дата регистрации',
            'about_regdv': '{0}',
            'about_statsf': 'Статистика',
            'about_statsv': '{0} серверов\r\n{1} пользователей',
            'about_uptimef': 'Активен',
            'about_uptimev': '{0}',
            'about_basedf': 'Работает на базе',
            'about_basedv': 'Python {0}\r\nDisnake {1}\r\nSQLite {2}',
            'about_hardwf': 'Оборудование',
            'about_hardwv': '**ЦП:** {0} ({1} МГц)\r\n**ОЗУ:** {2}\r\n**Платформа:** {3}',
            'about_linksf': 'Ссылки',
            'about_linksv': '[Пригласить]({0})',
            'about_linksv2': '[Сайт]({0})',
            'about_linksv3': '[Исходный код]({0})',
            'about_linksv4': '[Сервер поддержки]({0})',
            'about_linksv5': '[Донат]({0})',
            'about_licensesf': 'О лицензиях',
            'about_licensesv': 'Это свободное программное обеспечение с открытым исходным кодом, предназначенное для работы с сетевыми API и распространяемое в соответствии с условиями [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) и/или [GNU Affero GPL 3.0 (или выше)](https://www.gnu.org/licenses/agpl-3.0.html).',
            'user_nickf': 'Псевдоним',
            'user_nickv': '{0}',
            'user_nickvn': '*Отсутствует*',
            'user_regdf': 'Дата регистрации',
            'user_regdv': '{0}',
            'user_joinf': 'Дата входа на сервер',
            'user_joinv': '{0}',
            'user_statusf': 'Статус',
            'user_statusv': '<:online:1012294415731146765> Онлайн',
            'user_statusv2': '<:idle:1012294411020947457> Отошел',
            'user_statusv3': '<:dnd:1012294408412082186> Не беспокоить',
            'user_statusv4': '<:offline:1012294452246753300> Оффлайн',
            'user_rolesf': 'Роли ({0})',
            'user_rolesv': '{0}',
            'guild_ownerf': 'Владелец',
            'guild_ownerv': '{0}\r\n({1} / _`{2}`_)',
            'guild_crtf': 'Дата создания',
            'guild_crtv': '{0}',
            'guild_blvlf': 'Уровень бустов',
            'guild_blvlv': '_Пока еще нет бустов_',
            'guild_blvlv2': 'Уровень {0} / {1} бустов',
            'guild_mlvlf': 'Уровень модерации',
            'guild_mlvlv': 'Нет ограничений',
            'guild_mlvlv2': 'Только подтвержденный e-mail',
            'guild_mlvlv3': 'Регистрация более 5 минут',
            'guild_mlvlv4': 'Присутствие более 10 минут',
            'guild_mlvlv5': 'Только подтвержденный телефон',
            'guild_statsf': 'Статистика',
            'guild_statsv': '**Всего {0} участников**\r\n<:users:1014484889732653066> {1} ({2}%)\r\n<:bots:1014484886515630080> {3} ({4}%)\r\n<:online:1012294415731146765> {5} ({6}%)\r\n<:channels:1012296573364998196> {7}',
            'guild_rulesf': 'Правила',
            'guild_rulesv': '{0}',
            'guild_featurf': 'Функции',
            'guild_featurv': 'Автомодерация',
            'guild_featurv2': 'Сообщество',
            'guild_featurv3': 'Новости',
            'guild_featurv4': 'Чаты в голосовых каналах',
            'guild_featurv5': 'Экран приветствия',
            '8ball_answf': 'Ответ',
            '8ball_answv': ['Да.', 'Нет.', 'Возможно.', 'Может быть.', 'Время покажет.', 'Поживем - увидим.', 'Навряд ли.', 'Конечно.', 'Да-да.', 'Неа.', 'Так и есть.', 'Понятия не имею.', 'Я не знаю.', 'Я хз.', 'Без понятия.', 'Наверное, да...', 'Наверное, нет...', 'Да фиг знает!', 'Я не понял ваш вопрос, можете повторить?', 'Попробуйте задать другой вопрос. Может быть, я что-то не понимаю?', 'Вероятно.', 'Ничего подобного.'],
            'rngen_numbf': 'Число',
            'rngen_numbv': '{0}',
            'calc_resulf': 'Результат',
            'calc_rlerrv': 'ОШИБКА: Попытка деления на ноль',
            'calc_rlerrv2': 'ОШИБКА: Слишком большое число',
            'calc_rlerrv3': 'ОШИБКА: Принимаются только числа',
            'calc_rlerrv4': 'ОШИБКА: {0}',
            'calc_asignf': 'Доступные знаки',
            'calc_asignv': '[`+`] - сложение\r\n[`-`] - удаление\r\n[`/`], [`:`] - деление\r\n[`*`] - умножение',
            'settings_gsettf': 'Настройки сервера',
            'settings_gsettv': 'Язык: 🇷🇺 Русский\r\nПрефикс: {0}',
            'settings_usettf': 'Настройки пользователя',
            'settings_usettv': 'Часовой пояс: {0}',
            'settings_availoptf': 'Доступные параметры',
            'settings_availoptv': '🚩 Язык (Language)\r\n🪄 Префикс\r\n🕒 Часовой пояс',
            'ping_statisticsf': 'Статистика',
            'ping_statisticsv': '**Задержка:** {0} мсек\r\n**Задержка веб-сокета:** {1} мсек\r\n',
            'ping_statisticsv2': '**Задержка:** {0} мсек\r\n**Задержка веб-сокета:** {1} мсек\r\n**Время выполнения:** {2} мсек',
            'weather_resultf': 'Результаты поиска ({0})',
            'weather_resultv': '```{0}```',
            'weather_tempf': 'Температура воздуха',
            'weather_tempv': '**{0}°C**\r\nмин. {1}°C\r\nмакс. {2}°C',
            'weather_pressuref': 'Давление',
            'weather_pressurev': '{0} мм. рт. ст.',
            'weather_humidityf': 'Влажность',
            'weather_humidityv': '{0}%',
            'weather_windspeedf': 'Скорость ветра',
            'weather_windspeedv': '{0} м/сек',
            'weather_selyc': 'Выберите город или населенный пункт',
            'weather_upforecastsf': 'Ближайшие прогнозы',
            'weather_upforecastsv': '```{0}```',
            'codec_resulf': 'Результат',
            'codec_resulv': '```{0}```',
            'codec_algf': 'Алгоритм',
            'codec_algv': '{0}',
            'codec_algv2': 'Двоичный код',
            'codec_derrv': 'Ошибка декодирования',
            'codec_eerrv': 'Ошибка кодирования',
            'timers_dcr': 'Осталось {0} дн. {1} ч. {2} мин. {3} сек.',
            'timers_dce': 'Прошло {0} дн. {1} ч. {2} мин. {3} сек.',
            'timers_dco': 'Время закончилось',
        }
    elif where == "embed_footer":
        locale = {
            '8ball': 'Все совпадения случайны!',
            'help': 'Версия {0}',
            'help2': 'На основе Microbot версии {0}',
        }
    elif where == "command_categories":
        locale = {
            'main': '🤖 Главное',
            'fun': '🎭 Развлечения',
            'interactivity': '🌐 Интерактивность',
            'personalization': '🎨 Персонализация',
            'other': '*️⃣ Другое'
        }
    elif where == "command_description":
        locale = {
            'help': 'Показывает справочную информацию, включая список доступных команд.',
            'about': 'Показывает описание бота, а также служебную информацию.',
            'user': 'Показывает информацию о пользователе.',
            'avatar': 'Показывает аватарки пользователя.',
            '8ball': 'Генерирует для любого вопроса случайный ответ. Все совпадения случайны!',
            'rngen': 'Генерирует случайное число в указанном диапазоне.',
            'guild': 'Показывает информацию о гильдии (сервере)',
            'calc': 'Простейший калькулятор.',
            'settings': 'Настройки бота.',
            'settings_lang': 'Смена языка.',
            'publish': 'Публикует сообщения с новостного канала без лишнего клика по кнопке мыши.',
            'ping': 'Пни меня.',
            'weather': 'Отображает прогноз погоды на ближайшие 24 часа. Для этого используется сервис [OpenWeatherMap](https://openweathermap.org).',
            'wiki': 'Показывает статью в Википедии в краткой форме.',
            'codec': 'Расшифровка и зашифровка текста',
            'timers': 'Создание и управление таймерами в прошедшее и оставшиеся времени.',
        }
    elif where == "command_examples":
        locale = {
            'help': '```{0}help```',
            'about': '```{0}about```',
            'user': '```{0}user [@упоминание | ID участника | юзернейм]```',
            'avatar': '```{0}avatar [@упоминание | ID участника | юзернейм]```',
            '8ball': '```{0}8ball [вопрос]```',
            'rngen': '```{0}rngen [начало диапазона]-[конец диапазона]```',
            'guild': '```{0}guild```',
            'settings': '```{0}settings [-L] [значение]\r\n{0}settings -L en_US```',
            'settings_lang': '```{0}settings -L [en_US / ru_RU]\r\n{0}settings -L en_US```',
            'settings_lang2': '```{0}settings language [en_US / ru_RU]\r\n{0}settings language en_US```',
            'settings_prefix': '```{0}settings -P [префикс]\r\n{0}settings -P m!```',
            'settings_pref2': '```{0}settings prefix [префикс]\r\n{0}settings prefix m!```',
            'settings_tz': '```{0}settings -tz [обозначение часового пояса]\r\n{0}settings -tz Europe/Moscow\r\n{0}settings -tz Asia/Barnaul```',
            'settings_tz2': '```{0}settings timezone [обозначение часового пояса]\r\n{0}settings timezone Europe/Moscow\r\n{0}settings timezone Asia/Barnaul```',
            'publish': '```{0}publish [текст]\r\n{0}publish Вот так выглядит публикация!```',
            'ping': '```{0}ping```',
            'weather': '```{0}weather [город или населенный пункт]\r\n{0}weather Париж\r\n{0}weather Лондон\r\n{0}weather Санкт-Петербург\r\n{0}weather Барнаул```',
            'wiki': '```{0}wiki [полное название страницы]\r\n{0}wiki Синус\r\n{0}wiki Android (операционная система)\r\n{0}wiki Кунсткамера\r\n{0}wiki Прокси-сервер\r\n{0}wiki Эмодзи```',
            'codec': '```{0}codec [-d / -e] [алгоритм] [содержимое]\r\n{0}codec -e base64 Base64 text encoding.\r\n{0}codec -e binary Это перевод текста в двоичный код.\r\n{0}codec -d base64 QmFzZTY0IHRleHQgZGVjb2RpbmcgZXhhbXBsZS4=```',
            'calc': '```{0}calc [выражение]```',
            'timers': '```{0}timers```',
            'timers_create': '```{0}timers [-Cr / -Ce] [имя таймера] -t [ГГГГ-ММ-ДД ЧЧ:ММ:СС] -e [эмодзи]\r\n{0}timers -Cr Новый год -t 2025-01-01 00:00:00 -e 🎄\r\n{0}timers -Ce Начало карьеры -t 2016-03-27 00:00:00 -e 📹```',
            'timers_delete': '```{0}timers -D [имя таймера]\r\n{0}timers -D Начало карьеры```',
        }
    elif where == "button":
        locale = {
            'user_avatar': 'Показать аватар',
            'rngen_retry': 'Повторить',
            'timers_create': 'Создать',
            'timers_delete': 'Удалить',
        }
    elif where == "numb_with_unit":
        locale = {
            'bytes': '{0} байт',
            'bytes2': '{0} / {1} байт',
            'kilobytes': '{0} кБ',
            'kilobytes2': '{0} / {1} кБ',
            'megabytes': '{0} МБ',
            'megabytes2': '{0} / {1} МБ',
            'gigabytes': '{0} ГБ',
            'gigabytes2': '{0} / {1} ГБ',
        }
    else:
        locale = {}
    if len(locale) == 0: # if string not found (variant #1)
        return "[{0}|{1}]".format(str, where)
    else:
        return locale[str]

def _dt_fmt(datetime, size):
    if(size == 'full'):
        days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        months = ['', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
        return f'{days_of_week[datetime.weekday()]}, {datetime.day} {months[datetime.month]} {datetime.year} г. в {datetime.hour:02d}:{datetime.minute:02d}:{datetime.second:02d}'
    elif(size == 'normal'):
        days_of_week = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
        months = ['', 'янв.', 'фев.', 'мар.', 'апр.', 'мая', 'июн.', 'июл.', 'авг.', 'сен.', 'окт.', 'ноя.', 'дек.']
        return f'{days_of_week[datetime.weekday()]}, {datetime.day} {months[datetime.month]} {datetime.year} г. в {datetime.hour:02d}:{datetime.minute:02d}:{datetime.second:02d}'
    elif(size == 'compact'):
        days_of_week = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
        months = ['', 'янв.', 'фев.', 'мар.', 'апр.', 'мая', 'июн.', 'июл.', 'авг.', 'сен.', 'окт.', 'ноя.', 'дек.']
        return f'{days_of_week[datetime.weekday()]}, {datetime.day} {months[datetime.month]} {datetime.year} г.'
