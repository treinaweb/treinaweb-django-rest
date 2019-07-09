from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PaginacaoCustomizada(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'tamanho_pagina'
    max_page_size = 5

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'results': data
        })