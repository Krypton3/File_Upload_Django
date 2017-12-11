from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View

from .forms import FileForm
from .models import Files


class Upload(View):
    def get(self, request):
        f_list = Files.objects.all()
        return render(self.request, 'main/basic_upload/index.html', {'Obj': f_list})

    def post(self, request):
        form = FileForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            f = form.save()
            data = {'is_valid': True, 'name': f.file.name, 'url': f.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


def Delete_Files(request):
    for f in Files.objects.all():
        f.file.delete()
        f.delete()
    return redirect(request.POST.get('next'))
