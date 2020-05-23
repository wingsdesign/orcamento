# -*- Mode: Python; coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from core.base.models import Fornecedor, Compra, Produto, Material



@login_required(redirect_field_name='redirect_to')
def orcamento(request, id=None, *args, **kwargs):
	contexto = {}
	contexto['orcamento'] = Compra.objects.get(id=id)

	return render(request, "orcamento.html", contexto)

