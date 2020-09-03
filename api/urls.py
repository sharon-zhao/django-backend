from django.urls import path, include
from .views.mango_views import Mangos, MangoDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.post_views import Posts, PostDetail
from .views.comment_views import Comments, CommentDetail
from django.conf.urls import url
from .views.upload_views import MyView

urlpatterns = [
	# Restful routing
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
    path('post', Posts.as_view(), name='post-create'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('comment', Comments.as_view(), name='comment-create'),
    path('comment/<int:pk>', CommentDetail.as_view(), name='comment_detail'),
    url('', MyView.as_view(), name='form'),

]
