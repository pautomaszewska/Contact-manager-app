from mail.models import Person, Address, PhoneNumber, Mail, Group
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

class AddPerson(View):
    def get(self, request):
        return render(request, 'add_person.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        description = request.POST.get('description')

        p = Person()
        p.first_name = first_name
        p.last_name = last_name
        p.description = description
        p.save()

        return HttpResponseRedirect(reverse('details', args=(p.id,)))

class AddPhone(View):
    def get(self, request, id):
        p = Person.objects.get(id=id)
        return render(request, 'add_phone.html')

    def post(self, request, id):
        p = Person.objects.get(id=id)
        phone = request.POST.get('phone')
        phone_type = request.POST.get('phone_type')

        t = PhoneNumber()
        t.number = phone
        t.type = phone_type
        t.person = p
        t.save()

        return HttpResponseRedirect(reverse('details', args=(p.id,)))

class AddMail(View):
    def get(self, request, id):
        p = Person.objects.get(id=id)
        return render(request, 'add_mail.html')

    def post(self, request, id):
        p = Person.objects.get(id=id)
        email = request.POST.get('email')
        email_type = request.POST.get('email_type')

        e = Mail()
        e.email = email
        e.type = email_type
        e.person = p
        e.save()

        return HttpResponseRedirect(reverse('details', args=(p.id,)))

class AddAddress(View):
    def get(self, request, id):
        p = Person.objects.get(id=id)
        return render(request, 'add_address.html')

    def post(self, request, id):
        city = request.POST.get('city')
        street = request.POST.get('street')
        house_num = request.POST.get('house_num')
        flat_num = request.POST.get('flat_num')
        if not flat_num:
            flat_num = None

        a = Address()
        a.city = city
        a.street = street
        a.house_num = house_num
        a.flat_num = flat_num
        a.save()

        p = Person.objects.get(id=id)
        p.address = a
        p.save()

        return HttpResponseRedirect(reverse('details', args=(p.id,)))

class EditPerson(View):
    def get(self, request, id):
        p = Person.objects.get(id=id)

        return render(request, 'edit_person.html', {'person': p, })

    def post(self, request, id):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        description = request.POST.get('description')

        p = Person.objects.get(id=id)
        p.first_name = first_name
        p.last_name = last_name
        p.description = description
        p.save()

        return HttpResponseRedirect(reverse('details', args=(p.id,)))

class EditPhone(View):
    def get(self, request, id):
        t = PhoneNumber.objects.get(id=id)

        return render(request, 'edit_phone.html', {'t': t })

    def post(self, request, id):
        phone = request.POST.get('phone')
        phone_type = request.POST.get('phone_type')

        t = PhoneNumber.objects.get(id=id)
        t.number = phone
        t.type = phone_type
        t.save()

        return HttpResponseRedirect(reverse('details', args=(t.person_id,)))

class EditMail(View):
    def get(self, request, id):
        e = Mail.objects.get(id=id)

        return render(request, 'edit_mail.html', {'e': e })

    def post(self, request, id):
        email = request.POST.get('email')
        email_type = request.POST.get('email_type')

        e = Mail.objects.get(id=id)
        e.email = email
        e.type = email_type
        e.save()

        return HttpResponseRedirect(reverse('details', args=(e.person_id,)))

class EditAddress(View):
    def get(self, request, id):
        a = Address.objects.get(id=id)

        return render(request, 'edit_address.html', {'a': a })

    def post(self, request, id):
        city = request.POST.get('city')
        street = request.POST.get('street')
        house_num = request.POST.get('house_num')

        flat_num = request.POST.get('flat_num')

        a = Address.objects.get(id=id)
        a.city = city
        a.street = street
        a.house_num = house_num
        a.flat_num = flat_num
        a.save()

        return HttpResponseRedirect(reverse('details', args=(a.person__id,)))

class DeletePerson(View):
    def get(self, request, id):
        p = Person.objects.get(id=id)
        p.delete()
        return redirect('showall')

class DeletePhone(View):
    def get(self, request, id):
        t = PhoneNumber.objects.get(id=id)
        t.delete()

        return HttpResponseRedirect(reverse('details', args=(t.person_id,)))

class DeleteMail(View):
    def get(self, request, id):
        e = Mail.objects.get(id=id)
        e.delete()

        return HttpResponseRedirect(reverse('details', args=(e.person_id,)))

class DeleteAddress(View):
    def get(self, request, id):
        p = Person.objects.get(address_id=id)
        p.address = None
        p.save()

        a = Address.objects.get(id=id)
        a.delete()

        return HttpResponseRedirect(reverse('details', args=(p.id,)))

class ShowAll(View):
    def get(self, request):
        p = Person.objects.all().order_by('last_name')
        return render(request, 'show_all.html', {'person': p})

class PersonDetails(View):
    def get(self, request, id):
        try:
            p = Person.objects.get(id=id)
            t = PhoneNumber.objects.filter(person_id=id)
            e = Mail.objects.filter(person_id=id)
            a = Address.objects.get(person__id=id)

        except PhoneNumber.DoesNotExist:
            t = None
        except Mail.DoesNotExist:
            e = None
        except Address.DoesNotExist:
            a = None

        return render(request, 'person_details.html', {'person': p, 'telephone': t, 'email': e, 'address': a})

class Groups(View):
    def get(self, request):
        g = Group.objects.all().order_by('name')
        return render(request, 'groups.html', {'group': g})

class AddGroup(View):
    def get(self, request):
        return render(request, 'group_add.html')

    def post(self, request):
        name = request.POST.get('name')

        g = Group()
        g.name = name
        g.save()

        return redirect('groups')

class GroupDetails(View):
    def get(self, request, group_id):
        g = Group.objects.get(id=group_id)
        people = Person.objects.all()
        person = g.person.all()
        return render(request, 'group_details.html', {'people': people, 'person': person, 'group': g})
    def post(self, request, group_id):
        g = Group.objects.get(id=group_id)
        person = request.POST['people-list']
        idp = person[0]
        p = Person.objects.get(id=idp)
        g.person.add(p)

        return HttpResponseRedirect(reverse('groupdetails', args=(g.id,)))

class EditGroup(View):
    def get(self, request, group_id):
        g = Group.objects.get(id=group_id)
        return render(request, 'group_edit.html', {'g': g})
    def post(self, request, group_id):
        name = request.POST.get('name')

        g = Group.objects.get(id=group_id)
        g.name = name
        g.save()

        return redirect('groups')

class DeleteGroup(View):
    def get(self, request, group_id):
        g = Group.objects.get(id=group_id)
        g.delete()
        return redirect('groups')

class DeleteFromGroup(View):
    def get(self,request, group_id, id):
        g = Group.objects.get(id=group_id)
        p = Person.objects.get(id=id)
        p.group_set.remove(g)
        p.save()

        return HttpResponseRedirect(reverse('groupdetails', args=(g.id,)))

class Search(View):
    def get(self, request):
        return render(request, 'search.html')
    def post(self, request):
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')

        if first_name:
            person = Person.objects.filter(first_name=first_name)
            group = Group.objects.filter(person__first_name=first_name)
        elif last_name:
            person = Person.objects.filter(last_name=last_name)
            group = Group.objects.filter(person__last_name=last_name)

        elif first_name and last_name:
            person = Person.objects.filter(first_name=first_name, last_name=last_name)
            group = Group.objects.filter(person__first_name=first_name, person__last_name=last_name)

        return render(request, 'search_results.html', {'person': person, 'group': group})



