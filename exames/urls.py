from django.urls import path
from . import views

urlpatterns = [
    path('solicitar_exames/', views.solicitar_exames, name="solicitar_exames"), # type: ignore
    path('fechar_pedidos/', views.fechar_pedidos, name="fechar_pedidos"),
    path('gerenciar_pedidos/', views.gerenciar_pedidos, name="gerenciar_pedidos"),
    path('cancelar_pedido/<int:pedido_id>', views.cancelar_pedido, name="cancelar_pedido"),
    path('gerenciar_exames/', views.gerenciar_exames, name="gerenciar_exames"), # type: ignore
    path('permitir_abrir_exame/<int:exame_id>', views.permitir_abrir_exame, name="permitir_abrir_exame"), # type: ignore
    path('solicitar_senha_exame/<int:exame_id>', views.solicitar_senha_exame, name="solicitar_senha_exame"), # type: ignore
    path('gerar_acesso_medico/', views.gerar_acesso_medico, name="gerar_acesso_medico"), # type: ignore
    path('acesso_medico/<str:token>', views.acesso_medico, name="acesso_medico"),
]
