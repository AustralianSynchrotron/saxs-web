from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse

def test(request, type):

    return render_to_response('%s.html' % (type))
