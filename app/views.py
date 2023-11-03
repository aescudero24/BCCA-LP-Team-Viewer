from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from dataclasses import dataclass
from typing import List

# Create your views here.


@dataclass
class Team:
    name: str
    description: str
    members: List[str]


teams = {
    "management": Team(
        "Management",
        """Management team's job is to keep students on schedule during class,
      chores, and other activities. They build the schedules themselves and are
      supposed to guide us based on them.""",
        [
            "Matthew Hays",
            "Nicholas Gordon",
            "Owen Cotten",
            "Jeremiah Flowers",
            "Ab McCullough",
            "Abigail Usener",
        ],
    ),
    "procurement": Team(
        "Procurement",
        """Procurement team provides lunch and snacks based on a weekly budget. They
      also procure the necessary supplies for the building and ongoing events.""",
        [
            "Blaine Lambert",
            "Johnathon King",
            "Bryce Keel",
            "Wyatt Keenum",
            "Adrian Escudero",
        ],
    ),
    "documentation": Team(
        "Documentation",
        """Documentation team, as you can probably guess, document Base Camp Coding
      Academy. They do so by performing mock interviews with students, taking
      pictures of the events we participate in, and then posting them on the
      desired BCCA social media page.""",
        [
            "Mina Sanford",
            "Jay Williams",
            "Joshua Wadley",
            "Blair Johnson",
            "Kayleah Daniels",
            "Kaleigh Garcia",
            "Conner Cleland",
        ],
    ),
    "community": Team(
        "Community",
        """Community team delivers ideas for biweekly social events. They discuss to
      other teams about providing any supplies and effort in reaching the
      desired outcome of the event.""",
        [
            "Micah Gray",
            "Joby Foster",
            "Caleb Horn",
            "AJ Gilliland",
            "Jordan Donahue",
        ],
    ),
}


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def team_view(request: HttpRequest, name: str) -> HttpResponse:
    team = teams.get(name)
    if team is None:
        return HttpResponse("<h1><u>Team not found</u></h1>", status=404)
    context = {"team": team}
    return render(request, "team.html", context)
