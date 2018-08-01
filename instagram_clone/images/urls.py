from django.urls import path
from . import views

app_name = "images"

urlpatterns = [
    # url has 3 param
    # regex, view, name
    path("", view=views.Feed.as_view(), name="feed"),
    path("<int:image_id>/like/", view=views.LikeImage.as_view(), name="like_image"),
    path("<int:image_id>/comment/", view=views.CreateComment.as_view(), name="create_comment")
    # test data
    # path("all/", view=views.ListAllImage.as_view(), name="all_images"),
    # path("comments/", view=views.ListAllComments.as_view(), name="all_comments"),
    # path("likes/", view=views.ListAllLikes.as_view(), name="all_likes"),
]
