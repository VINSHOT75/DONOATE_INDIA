from django.urls import path
from . import views

urlpatterns = [
path("feed/",views.feed ,name="login"),
path("feed/donate/",views.donate ,name="donate"),
path("feed/donate/donateitem/",views.donateitem ,name="donateitem"),
path("feed/donate/viewdetails/<int:myid>",views.viewdetails ,name="viewdetails"),
path("feed/donate/donateitem/payment",views.payment ,name="payment"),
path("feed/donate/donateitem/stationary",views.stationary ,name="stationary"),
path("feed/donate/donateitem/food",views.food ,name="food"),
path("feed/donate/donateitem/clothes",views.clothes ,name="clothes"),
path("feed/donate/donateitem/time",views.time ,name="time"),
path("feed/donate/donateitem/blood",views.blood ,name="blood"),
path("feed/addpost/",views.add_post ,name="addpost"),
path("feed/checkout/",views.checkout ,name="checkout"),
]