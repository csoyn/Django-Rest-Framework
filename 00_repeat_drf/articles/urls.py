from django.urls import path
from . import views

urlpatterns = [
    # GET ~/articles/ : articles을 전부 조회
    # POST ~/articles/ : article을 작성
    path('articles/', views.article_list_create),

    # GET ~/articles/1 : 1번 article을 조회
    # DELETE ~/articles/1 : 1번 article을 삭제
    # UPDATE ~/articles/1 : 1번 article을 수정
    path('articles/<int:article_pk>/', views.article_detail_delete_update),
]
