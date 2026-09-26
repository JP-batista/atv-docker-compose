from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ArquivoForm
from .models import Arquivo


def index(request):
    if request.method == "POST":
        form = ArquivoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Arquivo enviado com sucesso!")
            return redirect("index")
    else:
        form = ArquivoForm()

    return render(
        request,
        "arquivos/index.html",
        {"form": form, "arquivos": Arquivo.objects.all()},
    )


@require_POST
def excluir(request, pk):
    arquivo = get_object_or_404(Arquivo, pk=pk)
    arquivo.arquivo.delete(save=False)
    arquivo.delete()
    messages.info(request, "Arquivo excluído.")
    return redirect("index")
