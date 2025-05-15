from rest_framework.pagination import PageNumberPagination

# Criamos a class para o 'básico' que vai personalizar quantas páginas que devemos criar: Professor, Disciplinar, Ambiente
class BaseCustomPagination(PageNumberPagination):
    page_size = 5

# O nosso padrão para o parâmetro de consulta da página é letra: 'p'
# O parâmetro de consulta de página padrão é 'page'
# Ele vai direcionar qual página que devemos seguir
    page_query_param = 'p'

# Defina o tamanho de página pelo cliente
# Aqui, a variável 'records' seria o ideial para digitar na URL
    page_size_query_param = 'records'

# Aqui, descreveremos o final da página
    max_page_size = 5

# Descrevemos a variável 'end' para dizer que é essa variável correta para escrever na URL se quiser, ir no final da página
    last_page_strings = ['end']


# Isso, vai definir as três classes que vai pegar a classe como 'básico' e vai colocar dentro dessas três classes que permite criar a página
class MyPageNumberPaginationProfessor(BaseCustomPagination):
    pass

class MyPageNumberPaginationDisciplinar(BaseCustomPagination):
    pass

class MyPageNumberPaginationAmbiente(BaseCustomPagination):
    pass

class MyPageNumberPaginationReserva(BaseCustomPagination):
    pass