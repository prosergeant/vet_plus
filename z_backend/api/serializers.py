from django.contrib.auth.models import User, Group
from rest_framework import serializers
from main.models import * # Teacher, MedicalCenter, Bids, Review, MedReview, CompletedTask

"""
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
"""

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'
        depth=1

class MedSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicalCenter
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = '__all__'


class BidSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bids
        fields = '__all__'
        depth=1


class PartnerBidSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartnerBid
        fields = '__all__'
        depth=1


class CompletedTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompletedTask
        fields = '__all__'
        depth=2


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        depth=1


class MedReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedReview
        fields = '__all__'
        depth=1

class MessagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Messages
        fields = '__all__'
        depth=1

class MedicalImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicalImage
        fields = '__all__'
        depth=1

class MedicalServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicalServices
        fields = '__all__'
        depth=1