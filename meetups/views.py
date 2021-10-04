from django.shortcuts import redirect, render,HttpResponse
from meetups.forms import RegistrationForm
from meetups.models import Meetup, Participant

# Create your views here.
def index(request):
    # return HttpResponse("hello World")

    # meetups = [
    #     { 'title': 'A First Meetup', 'location': 'kathmandu', 'slug': 'a-first-meetup'},
    #     { 'title': 'A Second Meetup', 'location': 'Pokhara', 'slug': 'a-second-meetup'},
    # ]

    meetups = Meetup.objects.all()

    return render(request, 'meetups/index.html', {
        'meetups': meetups,
        'show_meetups': True
    })

def meetup_details(request, meetup_slug):
    # selected_meetup = {
    #     'title': 'A First Meetup',
    #     'description': 'this is first meetup'
    # }

    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        registration_form = RegistrationForm(request.POST or None)
        if registration_form.is_valid():
            # participant = registration_form.save()
            email = registration_form.cleaned_data['email']
            participant, _ = Participant.objects.get_or_create(email=email)
            selected_meetup.participants.add(participant)
            return redirect('registration-succes', meetup_slug=meetup_slug)
        return render(request,'meetups/meetup-details.html', {
            'meetup_found': True,
            # 'meetup_title': selected_meetup.title,
            # 'meetup_description': selected_meetup.description
            'meetup': selected_meetup,
            'form': registration_form,
        })
    except Exception as e:
        return render(request,'meetups/meetup-details.html', {
            'meetup_found': False,
    })


def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html',{
        'organizer_email': meetup.organizer_email
    })
