from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
    "december": "Ahoj Żabciu"
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Ahoj Inny zwierzaczku!")
    redirect = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("Ahoj Inny zwierzaczku!")
    return HttpResponse(challenge_text)
