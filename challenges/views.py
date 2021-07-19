from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse

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
    for month in monthly_challenges.keys():
        month_path = reverse("month-challenge", args=[month])
        print(month_path)
        list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


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
            "header": f"Greeting in {month}"
        })
    except:
        return HttpResponseNotFound("<h1>Ahoj Inny zwierzaczku!<h1>")
