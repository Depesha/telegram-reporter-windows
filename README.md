# Telegram channel reporter for Windows
## Перший запуск
Даний репозиторій містить скрипти, які зроблять все за вас. Підготовлять ваш Windows для роботи і відправки репортів. 

З вашої сторони потрібно зробити наступне:
1. Отримати від телеграму **appId** і **appHash**. Посилання для отримання: https://my.telegram.org/auth
При створенні додатку, введіть назву додатку, айді додатку і url додатку. P.S. url додатку може бути будь який url. Наприклад: www.google.com

2. Далі вставити отримані **appId** і **appHash** в файл **settings.json**

```
{
    "appId": ваш_appId,
    "apiHash": "ваш_appHash"
}
```

**Навіщо це потрібно?** Тому що ви запускаєте додаток, який має працювати від імені когось. 
І вот саме від імені створеного додатку телеграма, який міститиме appId і appHash буде виконуватись дія

3. Добавте канали для репортінгу в файл **#repoted_channels.txt**. Один канал на в одній стрічні. 

Підтримуються наступні формати:
```
https://t.me/nameofchannel
@nameofchannel
nameofchannel
```

4. Відкрити папку зі скачаними файлами і запустити **1_first_run.bat**, клацнувши правою кнопкою миші і вибрати "Запустити від імені адміністратора".

**Чому від імені адміністратора?** На ваш ПК буде встановлений python і модулі python для виконання репортингу.

Перший запуск рахуєтсья успішним, коли вас запитують ваш номер телефону!


## Подальші запуски репортування
Надалі, щоб зарепортувати знову, вам лише потрібно буде оновити список каналів в файлі **#repoted_channels.txt** і запустити **2_post_run.bat**. 

В даному випадку не потрібно запускати від імені адміністратора.
