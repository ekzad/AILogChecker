from django.shortcuts import render
from . import pipeline as pp

SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}

# Create your views here.
def Main(request):
#main dashboard view, it calls the analyze logs and gets a list of info that is then processed and it is then sent to our .html file
    events = pp.analyze_logs()

    events.sort(key=lambda e: SEVERITY_ORDER.get(e.get("severity", "info"), 5))
 
    context = {
        "events": events,
        "total_count": len(events),
        "critical_count": sum(1 for e in events if e.get("severity") == "critical"),
        "high_count": sum(1 for e in events if e.get("severity") == "high"),
        "medium_count": sum(1 for e in events if e.get("severity") == "medium"),
    }
    return render(request, "dashboard.html", context)
