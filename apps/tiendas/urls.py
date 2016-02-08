from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('', 
	url(r'^admin/', include(admin.site.urls)),
	url(r'^datos/$', 'apps.tiendas.views.reclama_datos', name="reclama_datos"),
	url(r'^mostrartiendas/(?P<zona_name_slug>[\w\-]+)/$', 'apps.tiendas.views.mostrar_tiendas', name='tienda'),
	url(r'^add_zona/$', 'apps.tiendas.views.add_zona', name='add_zona'), # NEW MAPPING!
	url(r'^add_tienda/(?P<zona_name_slug>[\w\-]+)/$', 'apps.tiendas.views.add_tienda', name='add_tienda'), 
	url(r'^register/$', 'apps.tiendas.views.register', name='register'), # ADD NEW PATTERN!# NEW MAPPING!
	url(r'^login/$', 'apps.tiendas.views.user_login', name='login'),
	url(r'^restricted/', 'apps.tiendas.views.restricted', name='restricted'),
	url(r'^logout/$', 'apps.tiendas.views.user_logout', name='logout'),
	url(r'^aumentarvisitastienda/(?P<tienda_name_slug>[\w\-]+)/$' , 'apps.tiendas.views.aumentar_visitas_tienda', name="au_v_tienda"),
	url(r'^' , 'apps.tiendas.views.inicio', name="index"),
)
