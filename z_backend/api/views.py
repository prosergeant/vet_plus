from datetime import timedelta
from django.db.models.query import QuerySet
from django.urls.conf import path
from rest_framework import viewsets

from .serializers import *
from main.models import * 

from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.conf import settings

from itertools import groupby

class MedCenterViewSet(viewsets.ModelViewSet):
    allowed_methods = ('GET',)
    queryset = MedicalCenter.objects.all()
    serializer_class = MedSerializer


class ServicesViewSet(viewsets.ModelViewSet):
    allowed_methods = ('GET',)
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class BidViewSet(viewsets.ModelViewSet):
    allowed_methods = ('GET',)
    queryset = Bids.objects.order_by('-date')
    serializer_class = BidSerializer


class PartnerBidViewSet(viewsets.ModelViewSet):
    #allowed_methods = ('GET',)
    queryset = PartnerBid.objects.order_by('-date')
    serializer_class = PartnerBidSerializer


class CompletedTaskViewSet(viewsets.ModelViewSet):
    allowed_methods = ('GET',)
    queryset = CompletedTask.objects.all()
    serializer_class = CompletedTaskSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    allowed_methods = ('GET',)
    queryset = Review.objects.order_by('-id')
    serializer_class = ReviewSerializer


class LastReviewAPIView(APIView):
    def patch(self, request):
        last_item = Review.objects.last()
        serializer = ReviewSerializer(last_item)
        return Response(serializer.data)



class MedReviewViewSet(viewsets.ModelViewSet):
    allowed_methods = ('GET',)
    queryset = MedReview.objects.order_by('-id') #all()
    serializer_class = MedReviewSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    allowed_methods = ('GET',)
    #permission_classes = (IsAuthenticated,)
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer


class MedicalImageViewSet(viewsets.ModelViewSet):
    queryset = MedicalImage.objects.all()
    serializer_class = MedicalImageSerializer


class MedicalServicesViewSet(viewsets.ModelViewSet):
    queryset = MedicalServices.objects.all()
    serializer_class = MedicalServicesSerializer


"""
class UnauthenticatedPost(BasePermission):
    def has_permission(self, request, view):
        return request.method in ['POST']

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated|UnauthenticatedPost]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post']
"""

class GetUserInfo(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        email = request.user.email
        name = request.user.first_name
        phone = request.user.phone or ''
        is_med = False

        if request.user.is_med is not None:
            is_med = request.user.is_med.id

        data = {
            "email": email,
            "name": name,
            "id": request.user.id,
            'admin': request.user.is_superuser,
            'is_doctor': request.user.is_doctor,
            'is_admin': request.user.is_admin,
            'is_simpleuser': request.user.is_simpleuser,
            'is_med': is_med,
            'phone': phone
        }

        return Response(data)

from django.core import serializers
@api_view(['GET'])
def GetCurrDoc(request, pk):

    all_docs = Teacher.objects.all()
    currdocs = []
    is_prod = settings.PROD
    photo_url = 'http://127.0.0.1:8000/upload/'

    if is_prod:
        photo_url = 'https://vetplus.kz/upload/'

    for i in all_docs:
        if i.med is not None:
            if i.med.id == pk:
                i.photo = photo_url + str(i.photo)
                currdocs.append(i)

    
    res = {"result":"null"}
    
    serialized_qs = {"result": "null"}

    if currdocs != []:
        res = currdocs
        serialized_qs = serializers.serialize('json', res)

    return Response(serialized_qs)


@api_view(['GET'])
def GetBidsForCurrDoc(request, pk):

    curr_doc = Teacher.objects.get(pk=pk)
    all_bids = Bids.objects.filter(who=curr_doc)

    res = all_bids.values()

    return Response(res)


@api_view(['GET'])
def TeacherCurr(request, pk):
    instance = Teacher.objects.filter(pk=pk)
    serializer = TeacherSerializer(instance, many=True)
    return Response({ 'results': serializer.data })


class CreateUser(APIView):
    def post(self, request, *args, **kwargs):
        
        passw = request.data.get('password')

        new_user = Teacher(is_doctor=request.data.get('is_doctor'),
                              is_simpleuser=request.data.get('is_simpleuser'),
                              email=request.data.get('email'),
                              phone=request.data.get('phone'),
                              first_name=request.data.get('first_name') or "Пользователь",
                              last_name=request.data.get('last_name'),
                              text=request.data.get('text'),
                              #photo=request.data.get('photo'),
                              exp=request.data.get('exp'),
                              med=request.data.get('med'),
                              address=request.data.get('address'),
                              time_end=request.data.get('time_end'),
                              price=request.data.get('price'),
                              rating=request.data.get('rating'),
                              cashback=request.data.get('cashback'),
                              money=request.data.get('money') or 0
                              )
        new_user.set_password(passw)
        new_user.save()

        data = {
            'user has been': 'saved'
        }

        return Response(data)


class CreateReview(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        
        doc = Teacher.objects.get(id=request.data.get('id'))
        auth = Teacher.objects.get(id=request.user.id)
        new_review = Review(author=auth,
                            doctor=doc,
                            review=request.data.get('review'),
                            rating=request.data.get('rating'),
                            moderate=request.data.get('moderate') or False)

        new_review.save()

        reviews_of_this_doc = Review.objects.filter(doctor=doc, moderate=True)

        avg_rating = 0

        for i in reviews_of_this_doc:
            avg_rating += i.rating

        n = len(reviews_of_this_doc)

        if n == 0:
            n = 1

        avg_rating /= n

        doc.rating = avg_rating
        doc.save()

        data = {
            'newReview': 'created'
        }

        print("new review created")

        return Response(data)


class CreateMedReview(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        
        med = MedicalCenter.objects.get(id=request.data.get('id'))
        auth = Teacher.objects.get(id=request.user.id)
        new_review = MedReview(author=auth,
                            medcenter=med,
                            review=request.data.get('review'),
                            rating=request.data.get('rating'))

        new_review.save()

        reviews_of_this_med = MedReview.objects.filter(medcenter=med, moderate=True)

        avg_rating = 0

        for i in reviews_of_this_med:
            avg_rating += i.rating

        n = len(reviews_of_this_med)

        if n == 0:
            n = 1

        avg_rating /= n

        med.rating = avg_rating
        med.save()

        data = {
            'newMedReview': 'created'
        }

        print("new med review created")

        return Response(data)


class CreateBid(APIView):
    def post(self, request, *args, **kwargs):
        
        docID = request.data.get('id')
        doc = None

        if docID != -1:
            doc = Teacher.objects.get(id=request.data.get('id'))


        medID = request.data.get('medCenter')
        med = None
        
        if medID == -1 or medID == None:
            pass
        else:
            med = MedicalCenter.objects.get(id=medID)
        
        customer_id = request.data.get('customerID')
        customer_obj = None

        if customer_id != 0:
            customer_obj = Teacher.objects.get(id=customer_id)
        
        new_bid = Bids(name=request.data.get('name'),
                       phone=request.data.get('phone'),
                       select=request.data.get('select'),
                       someInfo=request.data.get('someInfo'),
                       who=doc,
                       customer=customer_obj,
                       in_med_center=request.data.get('in_med_center'),
                       med_center=med)

        

        new_bid.save()

        data = {
            'newBid': 'created'
        }

        print("new bid created")

        return Response(data)   



class CreateCompletedTask(APIView):
    def post(self, request, *args, **kwargs):

        usr = Teacher.objects.get(id=request.data.get('user'))
        bd  = Bids.objects.get(id=request.data.get('bid'))

        new_CT = CompletedTask(user=usr,
                               bid=bd)
        new_CT.save()

        data = {
            'newCT' : 'created'
        }

        print("new completed task created")

        return Response(data)


class Search(APIView):

    def post(self, request, *args, **kwargs):
        
        search = request.data.get('search')
        all_docs = Teacher.objects.filter(is_doctor=True)
        all_docs_end = []
        search_end = []
        search_end_end = []

        is_prod = settings.PROD
        photo_url = 'http://127.0.0.1:8000/upload/'

        if is_prod:
            photo_url = 'https://vetplus.kz/upload/'

        for i in all_docs:
            all_docs_end.append( i.first_name.lower() )
            if i.tegs is not None:
                all_docs_end.append( str(i.tegs).strip().lower() )
        
        
        search = search.lower()

        for i in all_docs_end:
            if str(search) in i:
                search_end.append(i)


        for i in all_docs:
            for j in search_end:
                if i.first_name.lower() == j or str(i.tegs).strip().lower() == j:
                    if photo_url in str(i.photo):
                        pass
                    else:
                        i.photo = photo_url + str(i.photo)
                    search_end_end.append(i)



        all_meds = MedicalCenter.objects.all()
        all_meds_end = []
        all_meds_end_end = []
        search_end = []
        med_search_end = []


        for i in all_meds:
            all_meds_end.append(i.name.strip().lower())
            if i.tegs is not None:
                all_meds_end.append( str( i.tegs ).strip().lower() )

        
        for i in all_meds_end:
            if str(search) in i:
                search_end.append(i)


        for i in all_meds:
            for j in search_end:
                if i.name.lower() == j or str( i.tegs ).strip().lower() == j:
                    if photo_url in str(i.photo):
                        pass
                    else:
                        i.photo = photo_url + str(i.photo)
                    search_end_end.append(i)
                    
        

        serialized_qs = {"result": "null"}

        if search_end_end != []:
            search_end_end_end = [el for el, _ in groupby(search_end_end)]
            print(search_end_end_end)
            res = search_end_end_end
            #res += med_search_end
            serialized_qs = serializers.serialize('json', res)

        return Response(serialized_qs)
        

class ChangePassword(APIView):
    def post(self, request, *args, **kwargs):
        new_pass = request.data.get('new_pass')

        request.user.set_password(new_pass)
        request.user.save()

        data = {
            "password": "updated"
        }

        return Response(data)


class DocWithoutMed(APIView):
    def get(self, request, *args, **kwargs):
        
        doc_without = Teacher.objects.filter(med=None, is_doctor=True)

        res = doc_without.values()

        return Response(res)


class BidsForCurrMed(APIView):
    def get(self, request, *args, **kwargs):

        medID = request.user.is_med.id

        med = MedicalCenter.objects.get(id=medID) #request.data.get('medID'))

        curr_bids = Bids.objects.filter(med_center=med).order_by('-date')

        serializer = BidSerializer(curr_bids, many=True)

        return Response(serializer.data)

    
class ChangeDocForCurrBid(APIView):
    def patch(self, request, *args, **kwargs):

        bidID = request.data.get('bidID')
        docID = request.data.get('docID')

        bid = Bids.objects.get(id=bidID)
        doc = Teacher.objects.get(id=docID)

        bid.who = doc

        bid.save()

        bid_str = 'bid id: ' + str(bidID)

        data = {
            bid_str : "saved"
        }

        return Response(data)


class AddDocForCurrMed(APIView):
    def patch(self, request, *args, **kwargs):
        docID = request.data.get('docID')
        medID = request.data.get("medID")

        doc = Teacher.objects.get(id=docID)
        med = MedicalCenter.objects.get(id=medID)

        doc.med = med
        doc.save()

        text = "Доктор: " + str(doc.first_name) + " добавлен к мед центру: " + str(med.name)

        data = {
            text: "success"
        }

        return Response(data)


class DeleteDocFromMed(APIView):
    def patch(self, request, *args, **kwargs):

        doc = Teacher.objects.get(id=request.data.get('docID'))

        doc.med = None
        doc.save()

        text = "Доктор: " + str(doc.first_name) + " удалён от клиники"

        data = {
            text: "success"
        }

        return Response(data)


class GetDocsForServices(APIView):
    def post(self, request, *args, **kwargs):

        serviceID = request.data.get('id')

        docs = Teacher.objects.filter(services=serviceID)

        """
        is_prod = settings.PROD
        photo_url = 'http://127.0.0.1:8000/upload/'

        if is_prod:
            photo_url = 'https://vetplus.kz/upload/'
        
        for i in docs:
            if photo_url in str(i.photo):
                pass
            else:
                i.photo = photo_url + str(i.photo)
        """
        
        res_sz = TeacherSerializer(docs, many=True)

        return Response(res_sz.data)


class SetNewImageMed(APIView):

    def post(self, request, *args, **kwargs):

        image = request.FILES.get('image')

        medID = request.user.is_med.id

        med = MedicalCenter.objects.get(id=medID)

        med.photo = image
        med.save()

        data = {
            "med_image0": "gotovo"
        }

        return Response(data)


class SetNewImageUser(APIView):

    def post(self, request, *args, **kwargs):

        image = request.FILES.get('image')

        userID = request.user.id

        user = Teacher.objects.get(id=userID)

        user.photo = image
        user.save()

        data = {
            "user_image0": "gotovo"
        }

        return Response(data)


class AddNewImageMed(APIView):

    def post(self, request, *args, **kwargs):

        image = request.FILES.get('image')

        medID = request.user.is_med.id

        med = MedicalCenter.objects.get(id=medID)

        new_image = MedicalImage(image=image, med=med)
        new_image.save()

        data = {
            "med_image0": "gotovo"
        }

        return Response(data)


@api_view(['GET'])
def GetMedImages(request, pk):
    med = MedicalCenter.objects.get(pk=pk)
    images = MedicalImage.objects.filter(med=med)

    res_sz = MedicalImageSerializer(images, many=True)

    return Response(res_sz.data)


@api_view(['GET'])
def GetMedServices(request, pk):
    med = MedicalCenter.objects.get(pk=pk)
    services = MedicalServices.objects.filter(med=med)

    res_sz = MedicalServicesSerializer(services, many=True)

    return Response(res_sz.data)


class AddNewMedService(APIView):
    def post(self, request, *args, **kwargs):
        new_med_service = MedicalServices(med=MedicalCenter.objects.get(id=request.data.get('id')), 
                                        name=request.data.get('name'),
                                        price=request.data.get('price'))

        new_med_service.save()

        data = {
            "new_med_service": "ok"
        }

        return Response(data)


@api_view(['GET'])
def GetBidDataForCalendar(request, pk):
        
    doctor = Teacher.objects.get(pk=pk)
    bids = Bids.objects.filter(who=doctor)

    today = datetime.datetime.now()
    today2 = today + timedelta(minutes=20)

    data = []

    for i in bids:
        
        date1 = i.date
        date2 = date1 + timedelta(minutes=30)

        template = { 
            "id": i.id,
            "description": i.someInfo,
            'location': '',
            'subject': i.name,
            'calendar': 'Лист 1',
            'start': date1,
            'end': date2
        }

        data.append(template)

    #res_sz = BidSerializer(bids, many=True)

    return Response(data)


class UpdateBidData(APIView):
    def post(self, request, *args, **kwargs):

        someInfo = request.data.get('someInfo')
        start = request.data.get('start')
        bid_id = request.data.get('id')
        
        bid = Bids.objects.get(id=bid_id)

        bid.date = start
        bid.someInfo = someInfo
        bid.save()

        data = {
            "bid update": "success"
        }

        return Response(data)