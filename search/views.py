# coding=utf8
from django.shortcuts import render
from recommand.models import raw_course
from recommand.models import course
from recommand.models import user_detail
from recommand.models import course_score
from recommand.models import user_course
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import re
from django.db import connection
from django.db.models import Avg
from django.db.models import Q

# Create your views here.
@csrf_exempt
def dosearch(request):

    result_list = list()
    result_dict =dict()

    if request.method == 'GET':
        keyword = request.GET.get('key')
	department = request.GET.get('department')
	time = request.GET.get('time')
        cur_page=request.GET.get('page')
	stars=request.GET.get('stars')
        if stars=='':
	    stars = 0

        number = 1
        leftNumber = (int(cur_page)-1) * 10
        rightNumber = int(cur_page) * 10
        avg_score=course_score.objects.values('c_id').annotate(Avg('cs_score'))
        print avg_score
	
	#filter
        querykeyword=Q(rc_name__contains=keyword)
	
	
	querydepartment = Q()
	for d in department.split(','):
	    querydepartment = Q(rc_department__contains=d) | querydepartment
	
	querytime=Q()
	for d in time.split(','):
	    querytime = Q(rc_weekday__contains=d) | querytime

	
 	query = querykeyword & querydepartment & querytime
	
        for row in raw_course.objects.filter(query).order_by('rc_name'):
            	    	  
            
            if number <= rightNumber and number > leftNumber:
		
		course_avg = 0
		for s in avg_score:
		    #print row.c_id.id
	            if str(s['c_id']) == str(row.c_id.id):
		        print str(s['c_id'])+' '+str(row.c_id.id)
		        print s['cs_score__avg']
			course_avg = s['cs_score__avg']
                if  (int(stars) <= course_avg) | (course_avg == 0):
		       
                    temp_dict = {'course_id':row.id,
                             'course_c_id':row.c_id.id,  
                             'course_name':row.rc_name,
                             'course_teacher':row.rc_teacher,
                             'course_date':row.rc_time,
                             'course_weekday':row.rc_weekday,
                             'course_credit':row.rc_credit,
                             'course_department':row.rc_department,
			     'course_star':course_avg,
                      }
                    result_list.append(temp_dict)
            
            number = number+1

   	result_dict = {'allnumber':number,'page': cur_page,'courses':result_list}
    return HttpResponse(json.dumps(result_dict))

@csrf_exempt
def moreinfor(request):
     
    result_list=list()
    temp_list1 = list()
    temp_list2 = list()
    temp_dict1 = dict()
    temp_dict2 = dict()
    result_dict =dict()

    if request.method == 'GET':
         courseid = request.GET.get('courseid')    
	 row = raw_course.objects.get(id=courseid)
         temp_dict1={      'course_id':row.id,
                           'course_c_id':row.c_id.id,  
                           'course_name':row.rc_name,
                           'course_teacher':row.rc_teacher,
                           'course_date':row.rc_time,
			   'course_weekday':row.rc_weekday,
                           'course_credit':row.rc_credit,
                           'course_department':row.rc_department,
                          }
    	 temp_list1.append(temp_dict1)

         print row.c_id
         for aa in course_score.objects.filter(c_id = row.c_id.id):
	      user = user_detail.objects.get(u_id=aa.u_id)
              temp_dict2 = {
                           'course_score':aa.cs_score,
                           'course_comment':aa.cs_comment,
			   'course_commentname':user.u_name,
		           'course_commentphoto':'http://graph.facebook.com/'+user.u_fid+'/picture?type=large',
                           'course_createon':str(aa.cs_createon),
                          }
    
              temp_list2.append(temp_dict2)
               
    
    result_dict = {'course':temp_list1,'reviews':temp_list2}
    return HttpResponse(json.dumps(result_dict))





