from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'userProfiles', views.UserProfileSet)
router.register(r'healthAgreements', views.HealthAgreementProfileSet)
router.register(r'clinics', views.ClinicProfileSet)
router.register(r'agreements', views.AgreementProfileSet)
router.register(r'doctors', views.DoctorProfileSet)
router.register(r'franchises', views.ClinicsFranchiseProfileSet)
router.register(r'analysis', views.AnalysisProfileSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('vk/', include('social_django.urls')),
]