
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('hotelapp.urls'))
]

# urlpatterns=[

#         path('hotel', include(HotelGuestView), include()),
#         path('room', RoomView, include()),
#         path('manager', ManagerView, include()),
# ]



