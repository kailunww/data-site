from django.shortcuts import render
from django.http.response import JsonResponse
from .task import add, mul, xsum


def test(request):
    ret = "hi"
    res = add.delay(2, 3)
    ret = res.get()
    return JsonResponse(dict(ret=ret))
