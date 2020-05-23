from django.contrib import admin
from .models import Fornecedor, Material, Compra, Produto

class ProdutoAdmin(admin.TabularInline):

	model = Produto
	extra = 1

class FornecedorAdmin(admin.ModelAdmin):
	pass

class MaterialAdmin(admin.ModelAdmin):
	pass

class CompraAdmin(admin.ModelAdmin):

	date_hierarchy = 'data'
	list_filter = ['data', 'fornecedor']

	inlines = [ProdutoAdmin]
	list_display = ['data', 'nota_fiscal', 'fornecedor', 'valor_compra', 'imprimir']


admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(Material, MaterialAdmin)