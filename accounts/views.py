from django.shortcuts import render

from .forms import UserForm
from .models import User, Pirg
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, PirgSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class PirgViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pirgs to be viewed or edited.
    """
    queryset = Pirg.objects.all()
    serializer_class = PirgSerializer
    permission_classes = [permissions.IsAuthenticated]


def index(request):
    ctx = {"msg": "hello world", "other_data": ["dogs", "cats"]}
    return render(request, "index.html", ctx)

def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            # check if user exists
            if User.objects.filter(username=form.cleaned_data['username']):
                return render(request, 'add_user_failed.html')

            default_sponsor = User.objects.get(username="lcrown")
            user = User(
                firstname=form.cleaned_data['firstname'],
                lastname=form.cleaned_data['lastname'],
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                is_pi=form.cleaned_data['is_pi'],
                sponsor=default_sponsor,
            )
            user.save()
            return render(request, 'add_user_success.html')

    else:
        form = UserForm()

    return render(request, 'add_user.html', {"form": form})
