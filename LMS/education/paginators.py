from rest_framework.pagination import PageNumberPagination


class lessonPaginator(PageNumberPagination):
    page_size = 2


class courcePaginator(PageNumberPagination):
    page_size = 10
