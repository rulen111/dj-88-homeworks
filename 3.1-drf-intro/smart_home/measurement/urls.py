from django.urls import path

from measurement.views import ListSensorsView, SensorDetailView, AddMeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path("sensors/", ListSensorsView.as_view()),
    path("sensors/<pk>/", SensorDetailView.as_view()),
    path("measurements/", AddMeasurementView.as_view()),
]
