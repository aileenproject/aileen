from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf.urls.static import static

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(
        r"^favicon.ico$",
        RedirectView.as_view(  # the redirecting function
            url=staticfiles_storage.url(
                "aileen/images/aileen.ico"
            )  # converts the static directory + our favicon into a URL
        ),
        name="favicon",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.AILEEN_MODE in ("server", "both"):
    urlpatterns.extend((
                    url(r"^", include("server.urls", namespace="server")),
                    url(r"^", include("calibration.urls", namespace="calibration"))
                    ))
elif settings.AILEEN_MODE == "box":
    urlpatterns.append(url(r"^", include("box.urls", namespace="box")))
