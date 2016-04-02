from django.shortcuts import render

def reader_view(request):
    return render(request, 'lito/reader_view.html', {'reader_view': reader_view})
