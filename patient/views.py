import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count,Sum
from django.contrib.auth.models import User

from datetime import date
import calendar

from .forms import QucikPatientForm, PatientForm
from .models import Patient

def home(request):
    return render(request, "index.html")

def doctor_login(request):
    if request.method != 'POST':
        return render(request, "index.html", {'page_title': 'Doctor Login'})
    
    username = request.POST.get('username')
    password = request.POST.get('password')

    if not username or not password:
        messages.error(request, "Username and password are required")
        return render(request, "login.html", {'page_title': 'Doctor Login'})

    user = authenticate(username=username, password=password)

    if user:
        login(request, user)
        return redirect("doctor-dashboard")
    else:
        messages.error(request, "Invalid credentials! Please login again...")
        return render(request, "index.html", {'page_title': 'Doctor Login'})
    
def doctor_register(request):
    if request.method != 'POST':
        return render(request, "index.html")
    # Get form data
    user_name = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    # Check if username exists
    if User.objects.filter(username=user_name).exists():
        messages.error(request, 'Username is already taken')
        return redirect('/doctor-register/')

    # Create user and profile
    user = User.objects.create_user(username=user_name, email=email, password=password)

    login(request, user)
    
    messages.success(request, 'Account created successfully')
    return redirect('doctor-dashboard')


@login_required
def doctor_reset_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('reset-password')

        request.user.set_password(new_password)
        request.user.save()
        messages.success(request, 'Password reset successfully. Please log in again.')
        logout(request)
        return redirect('home')
    
    return render(request, "reset_password.html", {'page_title': 'Reset Password'})


@login_required
def doctor_logout(request):
    logout(request)
    return redirect('home')

@login_required
def doctor_dashboard(request):
    if request.user.is_authenticated:
        data = Patient.objects.filter(user=request.user.id)
        total_amount = Patient.objects.filter(user=request.user).values('amount').aggregate(total=Sum('amount'))
    else:
        return redirect('doctor-login')
    return render(request, 'doctor_dashboard.html', {'data': data, 'total_amount': total_amount})

def dashboard(request):
    return render(request, 'dashboard.html')

def patient(request):
    # Filter patients by the logged-in user
    data = Patient.objects.filter(user=request.user).order_by('-id')
    return render(request, 'all_patients.html', {'data': data})

def quick_add_patient(request):
    if request.method == 'POST':
        form = QucikPatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user  # Associate the patient with the logged-in user
            patient.save()
            messages.success(request, "Patient added successfully.")
            return redirect('quick-add-patient')
        else:
            messages.warning(request, "Something went wrong!!")
            return redirect('quick-add-patient')
    else:
        form = QucikPatientForm
        return render(request, "quick_add_patient_form.html", {
            'form': form
        })

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user  # Associate the patient with the logged-in user
            patient.save()
            messages.success(request, "Patient added successfully.")
            return redirect('add-patient')
        else:
            print(form.errors)
            messages.warning(request, "Something went wrong!!")
            return redirect('add-patient')
    else:
        form = PatientForm
        return render(request, "add_patient_form.html", {
            'form': form
        })

@login_required
def update_patient(request, id):
    patient = get_object_or_404(Patient, id=id, user=request.user)  # Ensure patient belongs to the logged-in user
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient updated successfully.")
            return redirect('update-patient', id)
        else:
            print(form.errors)
            messages.warning(request, "Something went wrong!!")
            return redirect('update-patient', id)
    else:
        form = PatientForm(instance=patient)
        return render(request, "update_patient_form.html", {
            'form': form
        })

def delete_patient(request,id):
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    messages.success(request, "Patient deleted successfully.")
    return redirect('all-patients')  # Redirect to the list of all patients


#Reports
def reports(request):
    selectedYear = date.today().year
    if request.GET.get('year'):
        selectedYear = request.GET.get('year')

    selectedMonth = date.today().month
    if request.GET.get('month'):
        selectedMonth = request.GET.get('month')

    # Fetch years for the dropdown
    years = Patient.objects.filter(user=request.user).values('visit_date__year').annotate(total=Count('id'))

    # Fetch months for the dropdown
    monthName = []
    months = Patient.objects.filter(user=request.user, visit_date__year=selectedYear).values('visit_date__month').annotate(total=Count('id'))
    for month in months:
        monthName.append({'id': month['visit_date__month'], 'name': calendar.month_name[month['visit_date__month']]})

    # Daily Chart Data
    dPatients = Patient.objects.filter(
        user=request.user,
        visit_date__year=selectedYear,
        visit_date__month=selectedMonth
    ).values('visit_date').annotate(total=Count('id'))

    dailyChartLabels = [data['visit_date'].strftime('%d-%m-%y') for data in dPatients]
    dailyChartValues = [data['total'] for data in dPatients]

    # Monthly Chart Data
    mPatients = Patient.objects.filter(
        user=request.user,
        visit_date__year=selectedYear
    ).values('visit_date__month').annotate(total=Count('id'))

    monthChartLabels = [calendar.month_name[data['visit_date__month']] for data in mPatients]
    monthChartValues = [data['total'] for data in mPatients]

    # Yearly Chart Data
    yPatients = Patient.objects.filter(user=request.user).values('visit_date__year').annotate(total=Count('id'))

    yearChartLabels = [data['visit_date__year'] for data in yPatients]
    yearChartValues = [data['total'] for data in yPatients]

    return render(request, 'reports.html', {
        'dailyPatients': dPatients,
        'dailyChart': json.dumps({
            'dailyChartLabels': dailyChartLabels,
            'dailyChartValues': dailyChartValues
        }),
        'monthlyChart': json.dumps({
            'monthlyChartLabels': monthChartLabels,
            'monthlyChartValues': monthChartValues
        }),
        'yearlyChart': json.dumps({
            'yearlyChartLabels': yearChartLabels,
            'yearlyChartValues': yearChartValues
        }),
        'years': years,
        'currentYear': int(selectedYear),
        'currentMonth': int(selectedMonth),
        'monthName': monthName,
    })


def collection_reports(request):
    selectedYear = date.today().year
    if request.GET.get('year'):
        selectedYear = request.GET.get('year')

    selectedMonth = date.today().month
    if request.GET.get('month'):
        selectedMonth = request.GET.get('month')

    # Fetch years for the dropdown
    years = Patient.objects.filter(user=request.user).values('visit_date__year').annotate(total=Count('id'))

    # Fetch months for the dropdown
    monthName = []
    months = Patient.objects.filter(user=request.user, visit_date__year=selectedYear).values('visit_date__month').annotate(total=Count('id'))
    for month in months:
        monthName.append({'id': month['visit_date__month'], 'name': calendar.month_name[month['visit_date__month']]})

    # Daily Chart Data
    dPatients = Patient.objects.filter(
        user=request.user,
        visit_date__year=selectedYear,
        visit_date__month=selectedMonth
    ).values('visit_date').annotate(total=Sum('amount'))

    dailyChartLabels = [data['visit_date'].strftime('%d-%m-%y') for data in dPatients]
    dailyChartValues = [float(data['total']) if data['total'] else 0 for data in dPatients]  # Convert Decimal to float

    # Monthly Chart Data
    mPatients = Patient.objects.filter(
        user=request.user,
        visit_date__year=selectedYear
    ).values('visit_date__month').annotate(total=Sum('amount'))

    monthChartLabels = [calendar.month_name[data['visit_date__month']] for data in mPatients]
    monthChartValues = [float(data['total']) if data['total'] else 0 for data in mPatients]  # Convert Decimal to float

    # Yearly Chart Data
    yPatients = Patient.objects.filter(user=request.user).values('visit_date__year').annotate(total=Sum('amount'))

    yearChartLabels = [data['visit_date__year'] for data in yPatients]
    yearChartValues = [float(data['total']) if data['total'] else 0 for data in yPatients]  # Convert Decimal to float

    return render(request, 'collection_reports.html', {
        'dailyPatients': dPatients,
        'dailyChart': json.dumps({
            'dailyChartLabels': dailyChartLabels,
            'dailyChartValues': dailyChartValues
        }),
        'monthlyChart': json.dumps({
            'monthlyChartLabels': monthChartLabels,
            'monthlyChartValues': monthChartValues
        }),
        'yearlyChart': json.dumps({
            'yearlyChartLabels': yearChartLabels,
            'yearlyChartValues': yearChartValues
        }),
        'years': years,
        'currentYear': int(selectedYear),
        'currentMonth': int(selectedMonth),
        'monthName': monthName,
    })


