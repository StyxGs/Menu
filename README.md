<h1>Menu app</h2>

<h3>Инструкция по установке</h3>
<ol>
<li>Установить зависимости: pip install -r requirements.txt</li>
<li>Сохранить миграции: python manage.py makemigrations</li>
<li>Выполнить миграции: python manage.py migrate</li>
<li>Создать суперпользователя: python manage.py createsuperuser</li>
<li>Создать своё меню в админке</li>
<li>Зайти в menu/templates/menu/home.html в теге draw_menu поменять переменную 'main_menu' на название своего меню, в точности как вы его назвали в админке</li>
</ol>
