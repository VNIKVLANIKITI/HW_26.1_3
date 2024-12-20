from rest_framework import serializers
from education.models import lesson, course
from education.validators import ContentValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = lesson
        fields = ('name', 'description',)
        #validators = [ContentValidator(field='description')]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.IntegerField(source='lessons.count')
    lessons_count = serializers.SerializerMethodField()
    lessons_all = LessonSerializer(source='lessons', many=True)

    class Meta:
        model = course
        #fields = '__all__'
        fields = ('name', 'description', 'lessons', 'lesson_count', 'lessons_count', 'lessons_all' , )
        validators = [ContentValidator(field='description')]

    def get_lessons_count(self, obj):
        return obj.lessons.count()  # Подсчет связанных треков
