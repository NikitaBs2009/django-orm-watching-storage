from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404
from security_info_helper import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
    
    passcard = get_object_or_404(Passcard,passcode=passcode)

    passcard_visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for visit in passcard_visits:   
        duration =get_duration(visit)
        entry_local_time = localtime(visit.entered_at)
        visit_time =format_duration(duration)
        long_visit_flag =is_visit_long(duration)

        this_passcard_visits.append(
            {
                'entered_at': entry_local_time,
                'duration': visit_time,
                'is_strange': long_visit_flag
            }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
