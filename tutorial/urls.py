# -*- coding:utf8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from DjangoUeditor import urls as djud_urls
import blog.urls as blog_url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include(djud_urls)),
    url(r'^blog/', include(blog_url)),
]

# 此段代码暂时未知作用
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

