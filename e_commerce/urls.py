from django.urls import path
from .views import *

urlpatterns=[
    path('',IndexView, name='index'),
    path('cart/',CartView, name='cart' ),
    path('checkout/',CheckoutView,name='checkout'),
    path('blog-single-sidebar/',BlogSingleSidebar, name='blog-single-sidebar'),
    path('signup/', signup_view, name='signup'),
    path('logout/', log_out, name='logout'),
    path('login/', log_in, name='login'),
    path('addtocart/', addToCart, name='addtocart'),
    path('minusproduct/', minusproduct, name='minusproduct'),
    
    
    

    

]