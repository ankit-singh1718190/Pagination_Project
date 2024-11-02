from rest_framework.pagination import PageNumberPagination
class MyPagePagination(PageNumberPagination):
    page_size=5
    page_query_param='p'