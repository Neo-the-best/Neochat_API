from rest_framework import pagination

class UserPagination(pagination.PageNumberPagination):
    page_size = 5
    page_query_param = 'page'
    page_size_query_param = 'count'
    max_page_size = 100