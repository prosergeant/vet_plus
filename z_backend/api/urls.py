from django.urls import path
from rest_framework import routers
#from .views import TeacherViewSet, GetUserInfo, TeacherCurr, MedCenterViewSet, GetCurrDoc, BidViewSet, CreateUser, CreateReview
#from .views import CreateBid, ReviewViewSet, GetBidsForCurrDoc, MedReviewViewSet, CreateMedReview, Search, CreateCompletedTask
#from .views import 
from .views import *
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

router = routers.SimpleRouter()
router.register('doc', TeacherViewSet, basename='doc')
router.register('med', MedCenterViewSet, basename='med')
router.register('services', ServicesViewSet, basename='med')
router.register('bid', BidViewSet, basename='bid')
router.register('partner-bid', PartnerBidViewSet, basename='partner-bid')
router.register('review', ReviewViewSet, basename='review')
router.register('medreview', MedReviewViewSet, basename='medreview')
router.register('completed-tasks', CompletedTaskViewSet, basename='completed-tasks')
router.register('partner-messages', MessagesViewSet, basename='partner-messages')
router.register('med-images', MedicalImageViewSet, basename='med-images')
router.register('med-services', MedicalServicesViewSet, basename='med-services')

urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
    path('user-info/', GetUserInfo.as_view()),
    path('get-curr-doc/<int:pk>/', GetCurrDoc),
    path('get-bid-curr-doc/<int:pk>/', GetBidsForCurrDoc),
    path('create-user/', CreateUser.as_view()),
    path('create-review/', CreateReview.as_view()),
    path('create-review-med/', CreateMedReview.as_view()),
    path('create-bid/', CreateBid.as_view()),
    path('complete-task/', CreateCompletedTask.as_view()),
    path('review-last/', LastReviewAPIView.as_view()),
    path('search/', Search.as_view()),
    path('change-password/', ChangePassword.as_view()),
    path('doc-without-med/', DocWithoutMed.as_view()),
    path('bids-curr-med/', BidsForCurrMed.as_view()), 
    path('change-doc-bid/', ChangeDocForCurrBid.as_view()),
    path('add-doc-med/', AddDocForCurrMed.as_view()),
    path('delete-doc-med/', DeleteDocFromMed.as_view()),
    path('get-docs-service/', GetDocsForServices.as_view()),
    path('set-new-image-med/', SetNewImageMed.as_view()),
    path('set-new-image-user/', SetNewImageUser.as_view()),
    path('add-new-image-med/', AddNewImageMed.as_view()), 
    path('get-med-images/<int:pk>/', GetMedImages),
    path('get-med-services/<int:pk>/', GetMedServices),
    path('add-new-med-service/', AddNewMedService.as_view()),
    path('update-bid-data/', UpdateBidData.as_view()),
    path('get-bid-data/<int:pk>/', GetBidDataForCalendar )
]
urlpatterns += router.urls