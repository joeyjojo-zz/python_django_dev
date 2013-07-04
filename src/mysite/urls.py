import fnmatch
import os
import os.path
import re


from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


def handlebarsfilelist():
    """
    Get all the handlebar templates in the directory tree
    """
    includes = ['*.handlebars',] # for files only
    excludes = [] # for dirs and files

    # transform glob patterns to regular expressions
    includes = r'|'.join([fnmatch.translate(x) for x in includes])
    excludes = r'|'.join([fnmatch.translate(x) for x in excludes]) or r'$.'

    path = os.path.dirname(os.path.abspath(__file__))
    handlebarsdirectory = os.path.join(path, 'templates')

    files = []

    for root, dirs, files in os.walk(handlebarsdirectory):

        # exclude dirs
        dirs[:] = [os.path.join(root, d) for d in dirs]
        dirs[:] = [d for d in dirs if not re.match(excludes, d)]

        # exclude/include files
        files = [os.path.join(root, f) for f in files]
        files = [f for f in files if not re.match(excludes, f)]
        files = [f for f in files if re.match(includes, f)]

    print "Files", files
    return files


class MainAppView(TemplateView):
    filelist = None

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MainAppView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['filelist'] = self.filelist
        return context

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', MainAppView.as_view(
        template_name='index.html',
        filelist = handlebarsfilelist(),
    )),
)