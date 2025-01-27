from django.forms import DateInput
from django_filters import FilterSet, CharFilter, NumberFilter, DateFilter, TimeFilter



class PostFilter(FilterSet): # класс фильтра для поиска новостей
    search_title = CharFilter(lookup_expr='iregex', label='Название', field_name= 'title') # название статьи/новости
    search_author = CharFilter(lookup_expr='iregex', label='Автор', field_name= 'author__user__username') # название статьи/новости
    search_date = DateFilter(field_name='create_time', lookup_expr='exact',
                             label='Дата публикации', widget=DateInput(attrs={'type': 'date'}, format='%d%m%Y'))




