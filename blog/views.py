from datetime import date
from django.shortcuts import render


all_posts = [
    {
        "slug": "1",
        "image": "2.jpg",
        "author": "Michał1",
        "date": date(2021, 7, 25),
        "title": "Wizyta w Stolicy Czech",
        "excerpt": "W Pradze było nam fantastyczne, chodziliśmy sobie i zwiedzaliśmy wśród tłumów ludzi przed pandemią",
        "content": """Drogi Marszałku, Wysoka Izbo. PKB rośnie. Różnorakie i realizacji nowych propozycji. Wyższe założenie ideowe, a także usprawnienie systemu szkolenia kadr spełnia ważne z dotychczasowymi zasadami dalszych poczynań. Różnorakie i unowocześniania modelu rozwoju. Tak samo istotne jest ważne z powodu modelu.
        """
    },
    {
        "slug": "2",
        "image": "2.jpg",
        "author": "Michał2",
        "date": date(2021, 7, 29),
        "title": "Wizyta w Stolicy Polski",
        "excerpt": "W Pradze było nam fantastyczne, chodziliśmy sobie i zwiedzaliśmy wśród tłumów ludzi przed pandemią",
        "content": "Drogi Marszałku, Wysoka Izbo. PKB rośnie. Różnorakie i znaczenia tych problemów nie trzeba udowadniać, ponieważ rozpoczęcie powszechnej akcji kształtowania podstaw zmusza nas do tej decyzji skłonił mnie fakt, że konsultacja z powodu postaw uczestników wobec zadań stanowionych przez organizację. Troska."
    },
    {
        "slug": "3",
        "image": "2.jpg",
        "author": "Michał3",
        "date": date(2021, 7, 28),
        "title": "Wizyta w Stolicy Niemiec",
        "excerpt": "W Pradze było nam fantastyczne, chodziliśmy sobie i zwiedzaliśmy wśród tłumów ludzi przed pandemią",
        "content": "Drogi Marszałku, Wysoka Izbo. PKB rośnie. Nie muszę państwa przekonywać, że inwestowanie w tym zakresie koliduje z powodu form oddziaływania. Podobnie, zakończenie tego projektu umożliwia w określaniu obecnej sytuacji. Prawdą jest, iż inwestowanie w wypracowaniu nowych propozycji. Proszę państwa, nowy."
    }
]


def get_date(post):
    return post['date']


def start_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/posts.html", {
        "all_posts": all_posts
    })


def single_post(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/single-post.html", {
        "post": identified_post
    })
