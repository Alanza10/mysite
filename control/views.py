# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.management import call_command
from django.core.exceptions import ObjectDoesNotExist


def releOn(request):

    try:
        selected_choice = request.POST['choice']
        selected_time   = request.POST['time']
        print selected_choice
	if selected_choice == 'RELE1':
	    call_command('regar', '1', selected_time)
	elif selected_choice == 'RELE2':
	    call_command('regar', '2', selected_time)
	elif selected_choice == 'RELE3':
	    call_command('regar', '3', selected_time)
	elif selected_choice == 'RELE4':
	    call_command('regar', '4', selected_time)
    except ObjectDoesNotExist:
        # Redisplay the poll voting form.
        return HttpResponseRedirect(reverse('control_index'))
    else:
        return HttpResponseRedirect(reverse('control_index'))

def humedad(request):
    call_command('moisture2db')
    return HttpResponseRedirect(reverse('mois_index'))

def temperatura(request):
    call_command('temper2db')
    return HttpResponseRedirect(reverse('temp_index'))
