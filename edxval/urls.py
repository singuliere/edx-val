"""
Url file for django app edxval.
"""

from django.conf.urls import patterns, url
from django.conf import settings

from edxval import views

urlpatterns = patterns(
    '',
    url(
        r'^videos/$',
        views.VideoList.as_view(),
        name="video-list"
    ),
    url(
        r'^videos/(?P<edx_video_id>[-\w]+)$',
        views.VideoDetail.as_view(),
        name="video-detail"
    ),
    url(
        r'^videos/(?P<video__edx_video_id>[-\w]+)/(?P<language>[-_\w]+)$',
        views.SubtitleDetail.as_view(),
        name="subtitle-detail"
    ),
    url(
        r'^videos/(?P<edx_video_id>[-\w]+)/(?P<language>[-_\w]+)/subtitle$',
        views.get_subtitle,
        name="subtitle-content"
    ),
    url(
        r'^courses/{}$'.format(settings.COURSE_ID_PATTERN),
        views.CourseVideoList.as_view(),
        name="course-video-list"
    ),
    url(
        r'^youtube/(?P<youtube_id>[-_\w]+)$',
        views.YoutubeVideoList.as_view(),
        name="youtube-video-list"
    ),

)
