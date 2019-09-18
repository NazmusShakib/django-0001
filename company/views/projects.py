from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from company.models import Projects, Companies


@method_decorator(login_required, name='dispatch')
class ProjectList(ListView):
    model = Projects
    template_name = 'projects/project-list.html'
    context_object_name = 'projects'
    paginate_by = 10
    # queryset = Companies.objects.all()


@method_decorator(login_required, name='dispatch')
class ProjectCreate(CreateView):
    model = Projects
    template_name = 'projects/project-create.html'
    fields = (
        'name',
        'deadline',
        'description',
        'company'
    )
    success_url = '/projects'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectCreate, self).get_context_data(**kwargs)
        context['companies'] = Companies.objects.values('id', 'name')
        return context


# @login_required
# def companyCreate(request):
#     return render(request, 'company-form.html')

# @method_decorator(login_required, name='dispatch')
# class CompanyUpdate(UpdateView):
#     model = Companies
#     template_name = 'company-update.html'
#     fields = (
#         'name',
#         'email',
#         'phone',
#         'web_site',
#         'address'
#     )
#     success_url = '/companies'
#
#
# @method_decorator(login_required, name='dispatch')
# class CompanyDelete(DeleteView):
#     model = Companies
#     template_name = 'company-delete.html'
#     context_object_name = 'company'
#     success_url = '/companies'
