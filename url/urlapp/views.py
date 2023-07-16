from django.shortcuts import render, redirect
from .models import *
from .forms import *
import re

url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
new_url_pattern = "^[a-zA-Z0-9]+$"

# Create your views here.
def main(request):
    context = {}
    form = urlForm(request.POST or None)
    context["form"] = form
    if(request.method == 'POST'):
        if form.is_valid():
            form_new = form.cleaned_data["new"]
            form_source = form.cleaned_data["source"]
            all = url.objects.filter(new=form_new)
            valid_source = re.match(url_pattern, form_source)
            valid_new = re.match(new_url_pattern, form_new)
            if(valid_source != None):
                if(valid_new != None):
                    if(not all):
                        form.save()
                        newContext = {}
                        newContext["new"] = form.cleaned_data["new"]
                        newContext["source"] = form.cleaned_data["source"]
                        return render(request, 'urlapp/success.html', newContext)
                    else:
                        context["error"] = "URL already exists."
                else:
                    context["error"] = "Invalid chosen URL"
            else:
                context["error"] = "Invalid source URL"
    return render(request, 'urlapp/main.html', context)

def redir(request, string):
    context = {}
    try:
        link = url.objects.get(new=string)
        context["link"] = link.source
    except:
        pass
    return render(request, 'urlapp/redirect.html', context)

