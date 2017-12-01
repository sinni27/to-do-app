from django.conf.urls import url

from to_do_list import views

app_name = 'to_do_list'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^add_task/$',views.add_task,name='add_task'),
    url(r'to_do_list/(?P<pk>[0-9]+)/delete/$',views.TaskDelete.as_view(),name='task_delete'),

]
