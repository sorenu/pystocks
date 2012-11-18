from django.http import HttpResponse
from django.shortcuts import render
import d3generator

def diff(request, stock_symbol):
	data = d3generator.generate_d3(stock_symbol)
	return render(request, 'diff.html', {'data': data})

def diff_ajax(request):
	return render(request, 'diff_ajax.html')