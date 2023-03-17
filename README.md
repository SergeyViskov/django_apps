# django_apps


### **Описание**
Сервис прохождения опросов пользователями на Django.

### **Запуск проекта**

1. Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone https://github.com/SergeyViskov/django_apps.git
```

2. Установите и активируйте виртуальное окружение
```
python -m venv venv
``` 
```
source venv/Scripts/activate
```

3. Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
```
cd quizapp
```

4. В папке с файлом manage.py выполните миграции:
```
python manage.py migrate
```

5. В папке с файлом manage.py запустите сервер, выполнив команду:
```
python manage.py runserver
```
