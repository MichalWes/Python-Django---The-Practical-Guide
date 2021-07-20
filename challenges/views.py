from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Ahoj Muminku",
    "february": "Ahoj Kreciku!",
    "march": "Ahoj Kitku!",
    "april": "Ahoj Myszko!",
    "may": "Ahoj Hipopotamku",
    "june": "Ahoj Słodziaku",
    "july": "Ahoj Netoperku",
    "august": "Ahoj Wężyku",
    "september": "Ahoj Topinamburku!",
    "october": "Ahoj Słońciu!",
    "november": "Ahoj Kangurku!",
    "december": None
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Ahoj Inny zwierzaczku!<h1>")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": f"Greeting in {month}"
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
