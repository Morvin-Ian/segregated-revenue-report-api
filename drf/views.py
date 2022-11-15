from django.shortcuts import render

from .models import Revenue
from django.contrib.auth.models import User
from .serializers import RevenueSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

   
class RevenueList(APIView):
    def get(self, request, format=None):
        revenues = Revenue.objects.all()
        serializer = RevenueSerializer(revenues, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = RevenueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RevenueDetail(APIView):
    def get_object(self, pk):
        try:
            return Revenue.objects.get(pk=pk)
        except Revenue.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        revenue = self.get_object(pk)
        serializer = RevenueSerializer(revenue)
        return Response(serializer.data)

class RegistrationTotal(APIView):
    def get(self, request, format=None):
        revenues = Revenue.objects.exclude(registration=0.00)
        serializer = RevenueSerializer(revenues, many=True)
        return Response(serializer.data)

class PharmacyTotal(APIView):
    def get(self, request, format=None):
        revenues = Revenue.objects.exclude(pharmacy=0.00)
        serializer = RevenueSerializer(revenues, many=True)
        return Response(serializer.data)


class LaboratoryTotal(APIView):
    def get(self, request, format=None):
        revenues = Revenue.objects.exclude(laboratory=0.00)
        rev_lab = revenues[0]
        serializer = RevenueSerializer(revenues, many=True)
        return Response(serializer.data)


class RadiologyTotal(APIView):
    def get(self, request, format=None):
        revenues = Revenue.objects.exclude(radiology=0.00)
        serializer = RevenueSerializer(revenues, many=True)
        return Response(serializer.data)


class ProceduresTotal(APIView):
    def get(self, request, format=None):
        revenues = Revenue.objects.exclude(procedure=0.00)
        serializer = RevenueSerializer(revenues, many=True)
        return Response(serializer.data)


class PaymentMethodCount(APIView):
    def get(self, request, method, format=None):
        payment_method = Revenue.objects.filter(payment_method=method.upper())
        total_payments = Revenue.objects.all()
        counter = {f"{method}":payment_method.count(), "Out of":total_payments.count()}
        return Response(counter)


