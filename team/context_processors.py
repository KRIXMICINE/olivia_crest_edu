from django.shortcuts import get_object_or_404
from .models import Team

def team_single(request):
    team = None
    if 'team_pk' in request.session:
        try: team = Team.objects.get(request.session['team_pk'])
        except Team.DoesNotExist:
            pass
        
    return {'team': team}