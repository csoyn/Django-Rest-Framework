from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title', )


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        # is valid 통과!
        read_only_fields = ('article', )


class ArticleSeriailizer(serializers.ModelSerializer):
    # 1. 게시글의 댓글이 pk 형태로 표현됨.
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    # 2. 게시글의 댓글들의 정보가 모두(시리얼라이저에서 설정된 fields값) 표현됨.
    comment_set = CommentSerializer(many=True, read_only=True)

    # 추가
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Article
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

