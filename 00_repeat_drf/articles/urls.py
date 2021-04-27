from django.urls import path
from . import views

urlpatterns = [
    # GET ~/articles/ : articles을 전부 조회
    # POST ~/articles/ : article을 작성
    path('articles/', views.article_list_create),

    # GET ~/articles/1 : 1번 article을 조회
    # DELETE ~/articles/1 : 1번 article을 삭제
    # PUT ~/articles/1 : 1번 article을 수정
    path('articles/<int:article_pk>/', views.article_detail_delete_update),
    
    # GET ~/articles/1/comments/ : 1번 게시물의 모든 comment 조회
    # POST ~/articles/1/comments/ : 1번 게시물 comment 생성 (article_pk)
    path('articles/<int:article_pk>/comments/', views.comment_create),
    
    # GET ~/comments/ : comments를 전부 조회
    # POST ~/comments/ : comment 생성 => 할수있음! (여기에선 X)
    path('comments/', views.comment_list),

    # GET ~/comments/1/ : 1번 comment를 조회
    # DELETE ~/comment/1/ : 1번 comment를 삭제
    # PUT ~/comment/1/ : 1번 comment를 수정
    path('comments/<int:comment_pk>/', views.comment_detail_delete_update)
]
