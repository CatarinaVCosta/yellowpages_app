from django.urls import path
from .views import list_companies, new_company, edit_company, delete_company, search, admin_list_companies, \
    back_to_homepage, reset_form, back_to_adminpage, get_most_searched_categories

urlpatterns = [
    path('list/', list_companies, name="list_companies"),
    path('search/', search, name="search_companies"),
    path('', get_most_searched_categories, name="get_most_searched_categories"),
    path('adminpage/', back_to_adminpage, name="back_to_adminpage"),

    path('admin/', admin_list_companies, name="company_list"),
    path('admin/back', back_to_homepage, name="back_to_homepage"),
    # path('admin/new/', new_company, name="company_create"),
    path('admin/edit/<int:id>/', edit_company, name="company_update"),
    path('admin/reset', reset_form, name="reset_form"),
    path('admin/delete/<int:id>/', delete_company, name="company_delete"),
]
