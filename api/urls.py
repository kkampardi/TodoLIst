from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView

urlpatterns = {
    url(r'^todolist/$', CreateView.as_view(), name="create")
}

# the format_suffix_pattern allows us to specify the data format
# when we use the urls. It appends the format to be used to every URL in the pattern

urlpatterns = format_suffix_patterns(urlpatterns)

