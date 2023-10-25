from django.shortcuts import get_object_or_404, render
from .models import Team

# Create your views here.
def team(request):
    teams = None
    
    teams = Team.objects.all()
    context = {'teams': teams}
    
    return render(request, 'team.html', context)


def team_single(request, pk):
    team = get_object_or_404(Team, pk=pk)
    context = {'team': team}
    return render(request, 'team_single.html', context)