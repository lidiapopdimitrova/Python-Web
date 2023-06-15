from random import choice

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def show_departments(request, *args, **kwargs):
    print(request.method)
    print(request.GET)  # query params /?param1=value1&param2=value2
    print(request.POST)  # BODY OF http REQUEST

    order_by = request.GET.get('order_by', 'name')
    body = f'path: {request.path}, args={args}, kwargs={kwargs}, order_by:{order_by}'
    return HttpResponse(body)


def show_department_details(request, department_id):
    body = f'path: {request.path}, id: {department_id}'
    return HttpResponse(body)


def redirect_to_first_department(request):
    possible_order_by = ['name', 'age', 'id']
    order_by = choice(possible_order_by)

    # to='https://softuni.bg'
    # to= f'/departments/?order_by={order_by}'
    return redirect('show department details', department_id=13)


def show_not_found(request):
    # return HttpResponseNotFound('This is not found')
    # return HttpResponse('Error', status=status_code)
    raise Http404('Not found!')