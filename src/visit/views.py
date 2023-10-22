from django.shortcuts import render, redirect

from .forms import VisitForm


def visit_create_view(request):
    context = {}
    form = VisitForm(request.POST or None)
    if form.is_valid():
        visit_obj = form.save(commit=False)
        visit_obj.patient = request.patient
        visit_obj.save()
        return redirect('visit/create/')
    return render(request, 'visit/create.html', context)
