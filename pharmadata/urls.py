from django.urls import path
from .views import index, all_faculties, add_user, add_faculty, faculty_edit, faculty_delete, login_page, logout_page


urlpatterns = [
    path('', index, name='main-page'),
    path('login/', login_page, name='login-page'),
    path('logout/', logout_page, name='logout-page'),
    path('all-faculties', all_faculties, name='all-faculties'),
    path('add-user', add_user, name='add-user'),

    path('add-faculty', add_faculty, name='add-faculty'),
    path("faculty/<int:pk>/edit/", faculty_edit, name="faculty_edit"),
    path("faculty/<int:pk>/delete/", faculty_delete, name="faculty_delete"),
]
