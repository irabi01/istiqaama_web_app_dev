from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import MemberInfo, Dependant_info
from .forms import MemberInfoForm, DependantInfoForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.utils import timezone
from django.template.loader import get_template
from .render import Render
from django.views.decorators.cache import cache_control
from django.db.models import Sum


# @login_required(login_url = '/dashboard/user/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def generate_view(request):
    data_zote = Dependant_info.objects.all()
    today = timezone.now()
    params = {
        'today': today,
        'datas': data_zote,
        'request': request
    }
    return Render.render('dashboard/pdf.html', params)

# start of print report for individual member
# @login_required(login_url = '/dashboard/user/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def generate_single_view(request, id):
    # data_zote = Dependant_info.objects.all()
    full_details = Dependant_info.objects.get(id = id)
    today = timezone.now()
    params = {
        'today': today,
        'datas': full_details,
        'request': request
    }
    return Render.render('dashboard/member_details_pdf.html', params)
# end of print report for individual member

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home_view'))
    else:
        if request.method == 'POST':
            form = AuthenticationForm(data = request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request,user)
                return redirect('/dashboard/home/')
                # return render(request, 'dashboard/home.html')
        else:
            form = AuthenticationForm()
    login_template = 'dashboard/login.html'
    return render(request, login_template, {'form':form})

# @login_required(login_url = '/dashboard/user/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home_view(request):
    member = MemberInfo.objects.all()[:2]
    count_member = MemberInfo.objects.all().count()
    total = MemberInfo.objects.aggregate(Sum("amount"))
    count_user = User.objects.all().count()
    home_template = 'dashboard/home.html'
    context = {
        'member':member,
        'count_member':count_member,
        'count_user':count_user,
        'total':total,
    }
    return render(request, home_template, context)


# @cache_control(no_cache=True, must_revalidate=True)
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_view(request):
    logout(request)
    return redirect('login_view')

# @login_required(login_url = '/dashboard/user/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_view(request):
    count_member = MemberInfo.objects.all().count()
    if request.method == 'POST':
        form = MemberInfoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member Added Successfully')
            return redirect('/dashboard/add_member/')
    else:
        form = MemberInfoForm()
    context = {
        'form':form,
        'count_member':count_member
    }
    add_template = 'dashboard/add.html'
    return render(request, add_template, context)

# @login_required(login_url = '/dashboard/user/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_dependant(request):
    count_member = MemberInfo.objects.all().count()
    if request.method == 'POST':
        form = DependantInfoForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dependant Added Successfully')
            return redirect('/dashboard/dependant/')
    else:
        form = DependantInfoForm()
    context = {
        'form':form,
        'count_member':count_member
    }
    dependant_template = 'dashboard/dependant.html'
    return render(request, dependant_template, context)

# @login_required(login_url = '/dashboard/user/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def list_view(request):
    count_member = MemberInfo.objects.all().count()
    query = request.GET.get('query', None)
    member = MemberInfo.objects.all()
    if query is not None:
        member = member.filter(
            Q(f_name__icontains = query) |
            Q(l_name__icontains = query) |
            Q(member_id__icontains = query) |
            Q(married__icontains = query) |
            Q(phone_number__icontains = query) |
            Q(gender__contains = query) |
            Q(mwaka__contains = query)
        )
    list_template = 'dashboard/view.html'
    context = {
        'member':member,
        'count_member':count_member
    }
    return render(request, list_template, context)

# @login_required(login_url = '/dashboard/user/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def detail_view(request, id):
    count_member = MemberInfo.objects.all().count()
    full_details = Dependant_info.objects.get(id = id)
    context = {
        'fd':full_details,
        'count_member':count_member
        # 'd_info':d_info
    }
    detail_template = 'dashboard/detail.html'
    return render(request, detail_template, context)

# @login_required(login_url = '/dashboard/user/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_profile(request):
    count_member = MemberInfo.objects.all().count()
    context = {
        'count_member':count_member
    }
    profile_template = 'dashboard/profile.html'
    return render(request, profile_template, context)

# @login_required(login_url = '/dashboard/user/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home_setting(request):
    count_member = MemberInfo.objects.all().count()
    context = {
        'count_member':count_member
    }
    setting_template = 'dashboard/setting.html'
    return render(request, setting_template, context)

# @login_required(login_url = '/dashboard/user/login/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_detail_view(request, id):
    delete_data = get_object_or_404(MemberInfo , id = id)
    delete_data.delete()
    messages.info(request, 'Data Deleted successfully')
    return redirect('/dashboard/member_list/')
