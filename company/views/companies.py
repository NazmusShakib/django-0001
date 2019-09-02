from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from company.models import Companies


@method_decorator(login_required, name='dispatch')
class CompanyList(ListView):
    model = Companies
    template_name = 'company-list.html'
    context_object_name = 'companies'
    paginate_by = 10
    # queryset = Companies.objects.all()


@method_decorator(login_required, name='dispatch')
class CompanyCreate(CreateView):
    model = Companies
    template_name = 'company-create.html'
    fields = (
        'name',
        'email',
        'phone',
        'web_site',
        'address'
    )
    success_url = '/companies'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


# @login_required
# def companyCreate(request):
#     return render(request, 'company-form.html')

@method_decorator(login_required, name='dispatch')
class CompanyUpdate(UpdateView):
    model = Companies
    template_name = 'company-update.html'
    fields = (
        'name',
        'email',
        'phone',
        'web_site',
        'address'
    )
    success_url = '/companies'


@method_decorator(login_required, name='dispatch')
class CompanyDelete(DeleteView):
    model = Companies
    template_name = 'company-delete.html'
    context_object_name = 'company'
    success_url = '/companies'
