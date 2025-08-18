from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.shortcuts import get_object_or_404


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