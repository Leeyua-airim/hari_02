from django.urls import path
from . import views

app_name = "leader_llm"

urlpatterns = [
    path("", views.leader_page, name="leader_page"),  # /llm_hub/leader/
]
