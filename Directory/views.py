from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from django.db.models import Max,Count
from django.db.models import F
from django.utils.timezone import datetime
from Directory.models import StudentPrimdetail,SemTiming,Studentsession1920O,StudentCourseDetail,StudentDropdown,Sections,EmployeeDropdown,StudentSemester

def get_Course(request):
	if request.method == 'POST' :
		data = json.loads(request.body)

		if(data["Username"]=="admin" and data["Password"]=="12345"):
			q=StudentDropdown.objects.filter(field="COURSE").values('value','sno')
			d1={"Status":"True","data":list(q)}
			# print(d1)
			return JsonResponse(d1)
		elif((data["Username"]!="admin" and data["Password"]!="12345") or (data["Username"]=="admin" and data["Password"]!="12345") or (data["Username"]!="admin" and data["Password"]=="12345")) :
			d2={"Status":"False" , "data":{}}
			# print(d2)
			return JsonResponse(d2)
	elif request.method == 'GET' :
		cou=request.GET.get('cou','x')
		bran=request.GET.get('bran','x')
		sem=request.GET.get('sem','x')
		sec=request.GET.get('sec','x')
		Cou = cou.split (",")
		Bran = bran.split(",")
		Sem = sem.split(",")
		Sec = sec.split(",")
		if(cou!='x'):
			drop1=get_branch(Cou)
			return JsonResponse (list(drop1), safe=False)
		
		elif(cou=='x' and bran!='x' and sem=='x'):
			drop2=get_sem(Bran)
			return JsonResponse (drop2)
		
		elif(cou=='x' and  bran!='x' and sem!='x' and sec=='x'):
			drop3=get_sec(Bran,Sem)
			return JsonResponse (drop3)
		
		elif(bran!='x' and  sec!='x' and sem!='x'):
			data=get_Detail(Bran,Sem,Sec)
			return JsonResponse (data,safe=False)



	    


def get_branch(course):
	    #course=12,13,14
		q2=list(StudentCourseDetail.objects.filter(course_id__in=course).values('id','dept_id__value','course_id__value'))
		return(q2)

def get_sem(dept):
	#dept=41,42,
	t=datetime.today().date()
	q2=list (SemTiming.objects.filter(sem_start__lte=t , sem_end__gte=t).values('sem_type'))
	q3=StudentSemester.objects.none()
	sem=[]
	if q2[0]['sem_type'] == "odd":
		q3 = StudentSemester.objects.filter(dept__in=dept).annotate(odd=F('sem') % 2).filter(odd=True).order_by('sem').distinct().values('sem').order_by('sem')
	t1=len(q3)
	for x in range (0,t1):
		sem.append(q3[x]['sem'])
	d1={'sem':list(sem)}
	return(d1)


def get_sec(dept,sem):
	# dept=41,42.sem=1,3,5,7
	q4=list(StudentSemester.objects.filter(dept__in=dept,sem__in=sem).values_list('sem_id',flat=True))
	q5=list(Sections.objects.filter(sem_id__in=q4).annotate(max1=Count('section')).values_list('section',flat=True))
	section = set()
	for q in q5:
		if q not in section:
			section.add(q)

	d1={'sec':sorted(section)}		
	return(d1)

def get_Detail(dept,sem,sec):
	# section=A,B...dept=41,41...sem=1,3,4	
	# print(dept,sem,sec)/
	q4=list(StudentSemester.objects.filter(dept__in=dept,sem__in=sem).values_list('sem_id',flat=True))
	
	q5=list(Sections.objects.filter(dept_detail__in=dept,sem_id__in=q4,section__in=sec).values('section_id'))

	l=len(q5)
	uid=[]
	for x in range(0,l):
		q2=list(Studentsession1920O.objects.filter(section_id=q5[x]['section_id']).values('uniq_id'))
		uid.extend(q2)

	l=len(uid)
	data=[]
	for x in range (0,l):
		q3=list(StudentPrimdetail.objects.filter(uniq_id=uid[x]['uniq_id']).values('name','dept_detail__dept__value','lib_id','uni_roll_no','email_id','uniq_id','uniq_id__mob','uniq_id__class_roll_no'))
		data.extend(q3)
	return(data)


 