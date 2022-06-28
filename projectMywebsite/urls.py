from django.urls import include 
from django.urls import path
		
urlpatterns = [
    path('', admin.site.urls),
    # Enter the app name in following syntax for this to work
    path('', include("appMywebsite.urls")),
]