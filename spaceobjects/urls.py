from django.contrib.sitemaps.views import sitemap
from django.conf.urls import url

import spaceobjects.views as views
from spaceobjects.sitemap import SpaceObjectSitemap, OrbitClassSitemap

sitemaps = {
    'spaceobjects': SpaceObjectSitemap,
    'orbitclass': OrbitClassSitemap,
}

urlpatterns = [
    url('^asteroid/random$', views.random, name='random'),
    url('^asteroid/(?P<slug>[^/]+)$', views.detail_asteroid, name='detail_asteroid'),
    url('^comet/(?P<slug>[^/]+)$', views.detail_comet, name='detail_comet'),
    url('^asteroid/(?P<slug>[^/]+)/shape$', views.detail_shape, name='detail_shape'),
    url('^category/(?P<category>[^/]+)$', views.category, name='category'),
    url('^solar-system$', views.solar_system, name='solar_system'),
    url('^api/objects$', views.api_objects, name='api_objects'),
    url('^api/objects/search$', views.api_objects_search, name='api_objects_search'),
    url('^api/category/(?P<category>[^/]+)/orbits$', views.api_category_orbits, name='api_category_orbits'),
    url('^api/category/(?P<category>[^/]+)$', views.api_category_objects, name='api_category_objects'),
    url('^compiled', views.index, name='compiled'),
    url('^classifications', views.classifications, name='classifications'),
        url('^categorylist', views.categorylist, name='categorylist'),
    url('^$', views.main, name='main'),

    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
            name='django.contrib.sitemaps.views.sitemap')
]
