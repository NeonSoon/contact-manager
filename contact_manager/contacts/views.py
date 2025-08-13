from django.http import HttpResponse

def contact_list(request):
    return HttpResponse("這是聯絡人列表頁面")