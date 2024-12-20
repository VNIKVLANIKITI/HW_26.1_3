from rest_framework import viewsets, generics
from education.serializers import LessonSerializer, CourseSerializer
from education.models import lesson, course
from rest_framework.permissions import IsAuthenticated
from education.permissions import IsCurator
from education.paginators import lessonPaginator, courcePaginator
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt


# CRUD на вьюсетах
class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = lesson.objects.all()


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = course.objects.all()
    pagination_class = courcePaginator
    

# CRUD на дженериках
class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    #permission_classes = [IsAuthenticated]

    '''
    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()
    '''


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = lesson.objects.all()
    pagination_class = lessonPaginator


class LessonRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = lesson.objects.all()
    permission_classes = [IsCurator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = lesson.objects.all()


def CourceProductCreate(request, pk):
    product = course.objects.get(id=pk)
    product_name = product.name
    print(product_name)
    if request.method == 'GET':
        url = 'https://api.stripe.com/v1/products'
        headers = {
            'Authorization': 'Bearer sk_test_4eC39HqLyjWDarjtT1zdp7dc',
        }
        data = {
            'name': product_name,
        }
        response = requests.post(url, headers=headers, data=data)
        return JsonResponse(response.json(), status=response.status_code)
    return JsonResponse({'error': 'Invalid request method'}, status=400)  # Обработка GET-запросов


@csrf_exempt
def CourcePriceCreate(request, product_key):
    if request.method == 'GET':
        url = 'https://api.stripe.com/v1/prices'
        headers = {
            'Authorization': 'Bearer sk_test_4eC39HqLyjWDarjtT1zdp7dc',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = {
            'currency': 'rub',
            'unit_amount': 5000,
            'recurring[interval]': 'month',
            'product': product_key,
        }
        response = requests.post(url, headers=headers, data=data)
        return JsonResponse(response.json(), status=response.status_code)
    return JsonResponse({'error': 'Invalid request method'}, status=405)  # Обработка других методов


@csrf_exempt
def CourceCheckoutCreate(request, price_key):
    if request.method == 'GET':
        url = 'https://api.stripe.com/v1/checkout/sessions'
        headers = {
            'Authorization': 'Bearer sk_test_4eC39HqLyjWDarjtT1zdp7dc',
        }
        data = {
            'success_url': 'https://example.com/success',
            'line_items[0][price]': price_key,
            'line_items[0][quantity]': 2,
            'mode': 'subscription',
        }
        response = requests.post(url, headers=headers, data=data)
        return JsonResponse({'URL': response.json().get('url')}, status=response.status_code)
    return JsonResponse({'error': 'Invalid request method'}, status=405)  # Обработка других методов
