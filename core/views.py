from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import CompanyForm
from .models import Company
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.


def pagination(param, request):
    paginator = Paginator(param, 3)
    page = request.GET.get('page')

    return paginator.get_page(page)


def list_companies(request):
    companies_list = Company.objects.all()

    companies = pagination(companies_list, request)

    return render(request, 'homepage.html', {'companies': companies})


@login_required
def new_company(request):
    form = CompanyForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(admin_list_companies)

    return render(request, 'form.html', {'form': form})


@login_required
def edit_company(request, id):
    company = get_object_or_404(Company, pk=id)
    form = CompanyForm(request.POST or None, request.FILES or None, instance=company)

    if form.is_valid():
        form.save()
        return redirect(admin_list_companies)

    return render(request, 'form.html', {'form': form})


@login_required
def delete_company(request, id):
    search_by_id(id).delete()

    return redirect(admin_list_companies)


def search(request):
    get_companies_by_category = request.GET.get('category')
    get_companies_by_local = request.GET.get('local')

    if get_companies_by_category and get_companies_by_local:
        companies_list = search_by_category_and_location(get_companies_by_category, get_companies_by_local)
        save_to_db_nr_searches(companies_list)

    elif get_companies_by_category:
        companies_list = search_by_category(get_companies_by_category)
        save_to_db_nr_searches(companies_list)

    elif get_companies_by_local:
        companies_list = search_by_location(get_companies_by_local)

    else:
        companies_list = Company.objects.all()

    companies = pagination(companies_list, request)

    return render(request, 'homepage.html', {'companies': companies})


def search_by_category(category):
    return Company.objects.all().filter(category__exact=category).order_by('name')


def search_by_location(location):
    return Company.objects.all().filter(district__exact=location).order_by('name')


def search_by_category_and_location(category, location):
    return Company.objects.all().filter(category__exact=category,
                                        district__exact=location).order_by('name')


def search_by_id(id):
    return Company.objects.all().filter(id__exact=id)


@login_required
def admin_list_companies(request):
    companies_list = Company.objects.all()

    companies = pagination(companies_list, request)

    form = new_company(request)
    return render(request, 'admin.html', {'companies': companies, 'form': form})


@login_required
def back_to_homepage(request):
    logout(request)
    return redirect(list_companies)


@login_required
def back_to_adminpage(request):
    return redirect(admin_list_companies)


@login_required
def reset_form(request):
    CompanyForm()


def save_to_db_nr_searches(companies_list):
    for company in companies_list.iterator():
        company.nr_searches += 1
        company.save()


def get_most_searched_categories(request):
    for company in Company.objects.all():
        most_searched_companies = search_by_category(company.category).order_by('nr_searches')[:2]

        return render(request, 'homepage.html', {'most_searched_companies': most_searched_companies})
