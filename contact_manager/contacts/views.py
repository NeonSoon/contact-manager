from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/contact_list.html", {"contacts": contacts})

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')  # 新增後回到列表頁
    else:
        form = ContactForm()
    return render(request, 'contacts/add_contact.html', {'form': form})

def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else:
        form = ContactForm(instance=contact)
    return render(request, "contacts/edit_contact.html", {"form": form, "contact": contact})

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == "POST":
        contact.delete()
        return redirect("contact_list")
    return render(request, "contacts/delete_contact.html", {"contact": contact})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("contact_list")
        else:
            return render(request, "contacts/login.html", {"error": "帳號或密碼錯誤"})
    return render(request, "contacts/login.html")

def user_logout(request):
    logout(request)
    return redirect("login")