# sistema_floricultura

Passo a passo rodar no terminal 
1.	Criar uma pasta e abrir no vs code.
2.	No vs code abrir o terminal
3.	Rodar os seguintes comandos:
```
python -m venv venv
```
```
source venv/Scripts/Activate
```
```
pip install -r requirements.txt
```
```
python manage.py runserver
```
```
python manage.py migrate
```
USE A ESTRUTURA ABAIXO PARA MEXER EM UM BANCO GENERICO:
floricultura_marinalva\settings.py 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
USE A ESTRUTURA A BAIXO PARA MEXER EM UM BANCO NA MAQUIN, USANDO MYSQL
floricultura_marinalva\settings.py
```
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'floricultura',
         'USER': 'root',
         'PASSWORD': 'SENHA',
         'HOST': '127.0.0.1',
         'PORT': '3306',
     }
}
```
