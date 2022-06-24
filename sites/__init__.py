
# для каждого сайта импортируем свой класс
from .site_jazzesse import SiteJazzesseClass

# класс каждого сайта добавляем в списов, что бы его то-же спарсели
cl_sites_with_posters = [
    SiteJazzesseClass
]

__all__ = [cl_sites_with_posters]