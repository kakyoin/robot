import datetime

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.core.mail import send_mail
from django.template import RequestContext

from books.forms import ContactForm, NameForm
from books.models import Book


def hello(request):
    return HttpResponse("Hello world")


def page_404(request):
    return render_to_response('error-404.html', {})


# def current_datetime(request):
# now = datetime.datetime.now()
# html = "<html><body>It is now %s.</body></html>" % now
# return HttpResponse(html)


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return render_to_response('hours_ahead.html', {'hour_offset': offset, 'next_time': dt})


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


# def search_form(request):
# return render_to_response('search_form.html')
#
#
# def search(request):
#     if 'q' in request.GET:
#         message = 'You searched for: %r' % request.GET['q']
#     else:
#         message = 'You submitted an empty form.'
#     return HttpResponse(message)

def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books': books, 'query': q})
    return render(request, 'search_form.html', {'errors': errors})


# def contact(request):
# errors = []
#     if request.method == 'POST':
#         if not request.POST.get('subject', ''):
#             errors.append('Enter a subject.')
#         if not request.POST.get('message', ''):
#             errors.append('Enter a message.')
#         if request.POST.get('email') and '@' not in request.POST['email']:
#             errors.append('Enter a valid e-mail address.')
#         if not errors:
#             send_mail(
#                 request.POST['subject'],
#                 request.POST['message'],
#                 request.POST.get('email', 'noreply@example.com'),
#                 ['siteowner@example.com'],
#             )
#             return HttpResponseRedirect('/contact/thanks/')
#     return render_to_response('contact_form.html', {'errors': errors, 'subject': request.POST.get('subject', ''),
#                                                     'message': request.POST.get('message', ''),
#                                                     'email': request.POST.get('email', ''), },
#                               context_instance=RequestContext(request))
#
#
#     # def get_name(request):
#     # # if this is a POST request we need to process the form data
#     #     if request.method == 'POST':
#     #         # create a form instance and populate it with data from the request:
#     #         form = NameForm(request.POST)
#     #         # check whether it's valid:
#     #         if form.is_valid():
#     #             # process the data in form.cleaned_data as required
#     #             # ...
#     #             # redirect to a new URL:
#     #             return HttpResponseRedirect('/thanks/')
#     #
#     #     # if a GET (or any other method) we'll create a blank form
#     #     else:
#     #         form = NameForm()
#     #
#     #     return render(request, 'name.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    return render_to_response('contact_form.html', {'form': form}, context_instance=RequestContext(request))


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})