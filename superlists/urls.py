from django.conf.urls import url
from lists import views
from django.urls import path, include
from django.contrib import admin


#from superlists

urlpatterns = [
    path('', views.count_user_register, name='register'),
    path('calGrade', views.grade_calculator,name='calGrade'),
    path('admin/', admin.site.urls),
    path('signup', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'home', views.home_page, name='home'),
    url(r'flow', views.search_subjects_in_the_flow, name='flow'),
    url(r'help', views.help, name='help'),
    url(r'subject', views.list_of_subjects, name='listOfSubjects'),
    url(r'graph', views.graph, name='Graph'),
    url(r'picFlow', views.picture_of_flow, name='picFlow'),
    url(r'firstTerm', views.first_term, name='firstTerm'),
    url(r'secondTerm', views.second_term, name='secondTerm'),
    url(r'thirdTerm', views.third_term, name='thirdTerm'),
    url(r'fourthTerm', views.fourth_term, name='fourthTerm'),
    url(r'fifthTerm', views.fifth_term, name='fifthTerm'),
    url(r'sixthTerm', views.sixth_term, name='sixthTerm'),
    url(r'seventhTerm', views.seventh_term, name='seventhTerm'),
    url(r'eightTerm', views.eight_term, name='eightTerm'),
    url(r'about', views.about, name='about'),
    #url(r'home', views.home_page, name='calGrade'),
    #admin page
    #path('admin/', admin.site.urls),
    #url(r'^admin/', admin.site.urls),
    #register path
    #path("register/", v.register, name="register"),


]
