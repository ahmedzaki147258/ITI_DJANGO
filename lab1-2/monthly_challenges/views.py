from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

months_challenges = {
    "january": "run 20 mins every day.",
    "february": "eat 5 fruits every day.",
    "march": "do 30 pushups every day.",
    "april": "drink 3 liters of water every day.",
    "may": "read 10 pages of a book every day.",
    "june": "meditate for 10 minutes every day.",
    "july": "write a journal entry every day.",
    "august": "learn a new word every day.",
    "september": "practice a new skill for 30 minutes every day.",
    "october": "do yoga for 20 minutes every day.",
    "november": "volunteer for an hour every week.",
    "december": "spend time with family every day."
}

# Create your views here.
def index(request):
    months = list(months_challenges.keys())
    return render(request,"monthly_challenges/all.html", context={
        'all_month':months,
    })


def monthly_challenge_by_name(request, month):
        return render(request,"monthly_challenges/index.html", context={
        'text':months_challenges[month],
        'month': month,
    })

    # return HttpResponse(f"challenge for {months_challenges[month]}")


def monthly_challenge_by_number(request, month):
    months = list(months_challenges.keys())
    url = reverse("month_challenge_by_name", args=[months[month -1]])
    return HttpResponseRedirect(url)


def monthly_challenge(request):
    return render(request,"monthly_challenges/index.html", context={
        'text':"Hello",
        'number': 5,
    })


