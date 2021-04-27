# render : HTML 렌더하는 함수 => 사용 X
from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article, Comment
from .serializers import (
    ArticleListSerializer,
    ArticleSeriailizer,
    CommentListSerializer,
    CommentSerializer
)

# swagger
from drf_yasg.utils import swagger_auto_schema


# DRF : method를 구분하는 데코레이터 필수!!!
@swagger_auto_schema(methods=['POST'], request_body=ArticleSeriailizer)
@api_view(['GET', 'POST'])
def article_list_create(request):
    if request.method == 'GET':
        # articles = Article.objects.all()

        # 보내줄 데이터에 해당하는 인스턴스 정보
        articles = get_list_or_404(Article)
        
        # 시리얼라이저 인스턴스 생성 과정
        # 보내줄 데이터에 해당하는 인스턴스 정보가 필요 => 생성할때 넘겨줌
        # 넘겨주는 데이터가 여러개! : many=True
        serializer = ArticleListSerializer(articles, many=True)

        # HTML 랜더가 아니라, JSON을 응답으로 보내준다!
        return Response(serializer.data)
    elif request.method == 'POST':
        # DRF : request data 위치!
        serializer = ArticleSeriailizer(data=request.data)
        # is valid(raise_exception=True) : validation 통과하지 못하면 status code 400
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # status code 201 -> create data
            # status code 204 -> delete
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 아래 코드가 없으면 500 error => raise_exception=True 사용하면 생략 가능
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['PUT'], request_body=ArticleSeriailizer)
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail_delete_update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'GET':
        serializer = ArticleSeriailizer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'message': f'{article_pk}번 데이터가 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ArticleSeriailizer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # default 200
            return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)
    # elif request.method == 'POST':
    #     article = get_object_or_404(Article, pk=request.data.get('article_pk'))
    #     serializer = CommentSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         # article과 연결해주기!
    #         serializer.save(article=article)
    #         return Response(serializer.data)


@swagger_auto_schema(methods=['PUT'], request_body=CommentSerializer)
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail_delete_update(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'message': f'{comment_pk}번 댓글이 삭제되었습니다.'
        }
        return Response(data, status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    
@swagger_auto_schema(methods=['POST'], request_body=CommentSerializer)
@api_view(['POST'])
def comment_create(request, article_pk):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # article과 연결해주기!
            serializer.save(article=article)
            return Response(serializer.data)