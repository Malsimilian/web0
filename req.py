from requests import get, post, delete


def one():
    for i in get('http://localhost:8080/api/news').json()['news']:
        print(i)


def two():
    print(get('http://localhost:8080/api/news/1').json())

    print(get('http://localhost:8080/api/news/999').json())

    print(get('http://localhost:8080/api/news/q').json())


def tri():
    print(post('http://localhost:8080/api/news',
               json={'title': 'Заголовок',
                     'content': 'Текст новости',
                     'user_id': 1,
                     'is_private': False}).json())


def ch():
    print(delete('http://localhost:8080/api/news/3').json())
    # новости с id = 999 нет в базе

    print(delete('http://localhost:8080/api/news/2').json())


tri()
