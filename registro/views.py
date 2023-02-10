from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from registro.models import Employee, Register
from .forms import LoanForm
# from django.template import loader


def index(request):
    employee_list = Employee.objects.all()
    # template = loader.get_template('registro/index.html')
    context = {
        'employee_list': employee_list
    }
    return render(request, 'registro/index.html', context)
    # return HttpResponse(template.render(context, request))

def new_loan(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    form = LoanForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'registro/new_loan.html', {'form': form, 'employee': employee})

def detail_by_employee(request, employee_id):
    # try:
    #     employee = Employee.objects.get(pk=employee_id)
    # except Employee.DoesNotExist:
    #     raise Http404('Funcionário não existe!')
    # return render(request, 'registro/detail.html', {'employee': employee})
    employee = get_object_or_404(Employee, pk=employee_id)
    register = Register.objects.filter(employee=employee_id)
    total = [value.amount for value in register]
    months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    infos = [f'{reg.pub_date.day} de {months[reg.pub_date.month - 1]} -> R$ {reg.amount}' for reg in register]
    return render(request, 'registro/detail.html', {'employee': employee, 'infos': infos, 'total':sum(total)})

def detail_by_month(request, month):
    ...

