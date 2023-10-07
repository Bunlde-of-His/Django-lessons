from django.contrib import admin
from django.urls import path
from .views import show_about
from .views import show_home_page
from .views import show_article
from .views import add_comment
from .views import create_article
from .views import update_article
from .views import delete_article
from .views import list_topics
from .views import subscribe_to_topic
from .views import unsubscribe_from_topic
from .views import user_profile
from .views import set_password
from .views import set_userdata
from .views import deactivate_account
from .views import register_user
from .views import user_login
from .views import user_logout
from .views import show_date



urlpatterns = [
path('about/', show_about, name="about"),
    path('', show_home_page, name="home_page"),
    path('<int:article>/', show_article, name="article"),
    path('<int:article>/comment/', add_comment, name="add_comment"),
    path('create/', create_article, name="create_article"),
    path('<int:article>/update/', update_article, name="update_article"),
    path('<int:article>/delete/', delete_article, name="delete_article"),
    path('topics/', list_topics, name="list_topics"),
    path('topics/<int:topic>/subscribe/', subscribe_to_topic, name="subscribe_to_topic"),
    path('topics/<int:topic>/unsubscribe/', unsubscribe_from_topic, name="unsubscribe_from_topic"),
    path('profile/<str:username>/', user_profile, name="user_profile"),
    path('set-password/', set_password, name="set_password"),
    path('set-userdata/', set_userdata, name="set_userdata"),
    path('deactivate/', deactivate_account, name="deactivate_account"),
    path('register/', register_user, name="register_user"),
    path('login/', user_login, name="user_login"),
    path('logout/', user_logout, name="user_logout"),
    path('date/<int:year>/<int:month>/', show_date, name='show_date')
]
