from django.shortcuts import render
from houses.forms import UserProfileInfoForm



# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'houses/index.html')


@login_required
def uploadpics(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if profile_form.is_valid():

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)


            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['housespics']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'houses/index.html',
                          {'profile_form':profile_form,
                           'registered':registered})
