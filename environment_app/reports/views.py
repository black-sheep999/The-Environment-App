from django.shortcuts import render, redirect

from .forms import ReportForm

def report_issue(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            return redirect('report_success')
    else:
        form = ReportForm()
        return render(request, 'reports/report_form.html', {'form': form})


# Create your views here.
def report_success(request):
    return render(request, 'reports/report_success.html')

