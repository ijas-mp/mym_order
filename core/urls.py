from core.apis import router
from django.urls import path, include

app_name = "core"

urlpatterns = [path("", include(router.urls))]
