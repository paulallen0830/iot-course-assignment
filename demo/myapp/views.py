from django.shortcuts import render, redirect
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("E:/Projects/iot-course-assignment/demo/credentials.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://iot-course-assignment-default-rtdb.firebaseio.com/"
})

# Create your views here.

ref = db.reference()

def home_view(request):
    return render(request, 'home.html')

def insert_sensor(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        sensor_ref = ref.child('SENSOR')
        sensor_ref.update({key: value})
        return render(request, 'success.html')
    return render(request, 'insert_sensor.html')

def insert_user(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        user_ref = ref.child('USER')
        user_ref.update({key: value})
        return render(request, 'success.html')
    return render(request, 'insert_user.html')

def dashboard_view(request):
    return render(request, 'home.html')