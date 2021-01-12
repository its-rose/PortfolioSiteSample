from django.urls import path


from . import views



urlpatterns = [
    path('', views.home_page, name='home'),
    path('contact', views.contact_page, name='contact'),
    path('about', views.about_page, name='about'),
    path('blog', views.blog_page, name='blog'),
    path('portfolio', views.portfolio_page, name='portfolio'),
    path('get_in_touch', views.get_in_touch, name='get_in_touch'),
    path('<slug:post>', views.post_detail, name='post_detail'),
]