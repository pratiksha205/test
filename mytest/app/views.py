from django.shortcuts import render
from django.http import HttpResponse, response, HttpResponseRedirect
from .models import Student,State,City
import csv
from django.contrib import messages
from django.urls import reverse
import logging
# Create your views here.

def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Middle Name', 'Last Name', 'State Name', 'City Name', 'Gender'])
    
    students = Student.objects.all().values_list('student_f_name','student_m_name','student_l_name','student_state','student_city','gender')

    for student in students:
        writer.writerow(student)

    return response

def upload_csv(request):
	data = {}
	if "GET" == request.method:
		return render(request, "app/upload_csv.html", data)
    # if not GET, then proceed
	try:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return HttpResponseRedirect(reverse("myapp:upload_csv"))
        #if file is too large, return
		if csv_file.multiple_chunks():
			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
			return HttpResponseRedirect(reverse("myapp:upload_csv"))

		file_data = csv_file.read().decode("utf-8")		

		
	except Exception as e:
		logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
		messages.error(request,"Unable to upload file. "+repr(e))

	return HttpResponseRedirect(reverse("app:upload_csv"))