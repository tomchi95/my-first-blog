# Prosty blog w Django #

Kod źródłowy do filmu na YT: https://youtu.be/1Z5--nDwRFU

Pokazujemy jak w 30 minut zrobić bardzo prostego bloga w Django.

### Jak uruchomić? ###

Należy stworzyć środowisko wirtualne przy użyciu virtualenv:

```
virtualenv --no-site-packages tutorial-django-blog
```

aktywować je:

```
source ./tutorial-django-blog/bin/activate
```

i założyć katalog app:

```
mkdir ./tutorial-django-blog/app
cd ./tutorial-django-blog/app
```

Następnie należy zainstalować opowiednie pakiety:

```
pip install django
pip install django-bootstrap
```

W kolejnym kroku trzeba sklonować repozytorium:

```
hg clone https://bitbucket.org/netstation/tutorial-django-blog
```

zmienić katalog na katalog repozytorium:

```
cd tutorial-django-blog
```

i uruchomić projekt:

```
python manage.py runserver
```



