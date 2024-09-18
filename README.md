# My portfolio site

The site works in conjunction with Django + Vue 3 (Option API).

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

3. Setup your database in the `settings.py`. Default is `db.sqlite`:
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