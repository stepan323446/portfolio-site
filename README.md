# My portfolio site

The site works in conjunction with Django + Vue 3 (Option API).

* [Docker setup](#docker-setup)
* [Manually website setup](#manually-website-setup)
    * [Backend (Django)](#backend-django)
    * [Frontend (Vue)](#frontend-vue)
* [Telegram bot setup](#telegram-bot-setup)

## Docker setup
soon

## Manually website setup

### Backend (Django)
1. Install all packages in the folder `backend_dj/`
```
pip install -r requirements.txt
```
2. Set new secret key for django using django library or generate [on this website](https://djecrety.ir/)
```
python3 manage.py shell
```
```py
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```
and copy new secret key in the new file `.env`
```
SECRET_KEY={Your secret key}
```

3. Setup your database in the `settings.py`. Default is `db.sqlite3`:
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

4. Make all migrations for db
```
python3 manage.py makemigrations
python3 manage.py migrate
```

5. Set all allowed origins for frontend in the `settings.py`:
Default:
```py
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8080',
    'http://127.0.0.1:8080'
]
```

6. Start server
```
python3 manage.py runserver
```

### Frontend (Vue)

1. Install all packages in the folder `frontend_vue/`
```
npm install
```

2. Set axios default address for backend in the `src/main.js`
```js
axios.defaults.baseURL = 'http://127.0.0.1:8000';
```

3. Start dev mode
```
npm run serve
```
or Build frontend part of website
```
npm run build
```
## Telegram bot setup

The website supports sending messages to the Telegram messenger as a notification of a message. Go to the django admin panel and create a new object in the `Telegram bots` tab.

for a bot, you need to:

* Telegram bot token
* Your chat id with bot (you can get it using api `https://api.telegram.org/bot<token>/getUpdates`)