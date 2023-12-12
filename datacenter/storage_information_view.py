from datacenter.models import Visit
from django.shortcuts import render

from django.utils.timezone import localtime
from security_info_helper import get_duration, format_duration, is_visit_long


def storage_information_view(request):
    
    not_leaved_visits=Visit.objects.filter(leaved_at=None)

    not_closed_visits = []
    for visit in not_leaved_visits:
        duration =get_duration(visit)
        entry_local_time = localtime(visit.entered_at)
        visit_time =format_duration(duration)
        lon_visit_flag =is_visit_long(duration)
        pearson = visit.passcard

        not_closed_visits.append(
            {
                'who_entered': pearson,
                'entered_at': entry_local_time,
                'duration': visit_time,
                'is_strange': lon_visit_flag
            }
        )

    context = {
        'non_closed_visits': not_closed_visits, 
    }
    return render(request, 'storage_information.html', context)
