from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Donation
from .serializers import DonationSerializer

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    def create(self, request, *args, **kwargs):
        # Step 1: create a pending donation
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        donation = serializer.save(status='pending')

        # Step 2: send data to frontend to process with PayPal
        # You could return a PayPal payment link or client token
        return Response({
            "id": donation.id,
            "amount": donation.amount,
            "currency": donation.currency,
            "message": "Send this to PayPal frontend flow"
        }, status=status.HTTP_201_CREATED)

    def update_status(self, request, *args, **kwargs):
        """
        This endpoint receives the PayPal webhook or frontend confirmation
        and updates the donation status to completed/failed.
        """
        donation_id = request.data.get("donation_id")
        transaction_id = request.data.get("transaction_id")
        status_value = request.data.get("status")  # 'completed' or 'failed'

        try:
            donation = Donation.objects.get(id=donation_id)
            donation.status = status_value
            donation.transaction_id = transaction_id
            donation.save()
            return Response({"success": True, "donation": DonationSerializer(donation).data})
        except Donation.DoesNotExist:
            return Response({"error": "Donation not found"}, status=status.HTTP_404_NOT_FOUND)
