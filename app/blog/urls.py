from django.urls import path

from . import views

urlpatterns = [
    path("", views.pagina_inicial, name="pagina_inicial"),
    path(
        "postagens/<int:postagem_id>/",
        views.detalhar_postagem,
        name="detalhar_postagem",
    ),
    path(
        "postagens/<int:ano>/<int:mes>/",
        views.postagens_por_data,
        name="postagens_por_data",
    ),
    path(
        "categorias/<int:categoria_id>/",
        views.postagens_por_categoria,
        name="postagens_por_categoria",
    ),
    path("pesquisar/", views.pesquisar_postagens, name="pesquisar_postagens"),
    path("postagens/criar/", views.criar_postagem, name="criar_postagem"),
]
