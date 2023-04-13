from rest_framework import generics, status
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
from .form import ContactForm

class ContactView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return Response({'form': form.as_p()}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.data)
        if form.is_valid():
            form.save()
            return Response({'message': 'Thank you for contacting us!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'form': form.as_p()}, status=status.HTTP_400_BAD_REQUEST)