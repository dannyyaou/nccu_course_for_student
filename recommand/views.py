# coding=utf8
from django.shortcuts import render
from recommand.models import raw_course
from recommand.models import course
from recommand.models import user_detail
from recommand.models import course_score
from recommand.models import user_course
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

from scikits.crab.models import MatrixPreferenceDataModel
from scikits.crab.metrics import pearson_correlation
from scikits.crab.similarities import UserSimilarity
from scikits.crab.recommenders.knn import UserBasedRecommender
# Create your views here.

@csrf_exempt
def read_Coursecsv(request):
    #F = open('/home/jimmy/Desktop/course2.csv','r')
    #F.readline()
    #F.close()
    LineLenth = 0
    weHave = 0
    weDotHave =0
    rawHave =0
    rawDotHave =0

    for line in open('/home/jimmy/Desktop/allcourse4.csv','r'):
        if (LineLenth>0):
            b = line.replace('\n','').rsplit(',')

            #我們本身有沒有這堂課嗎，並抓出id
            Course = course.objects.filter(c_name=b[3], c_teacher=b[5])
            CourseId = 0
            if(Course):
                CourseId = Course[0].id
                weHave = weHave+1
            else:
                NewCourse = course.objects.create(c_name=b[3], c_teacher=b[5])
                CourseId = NewCourse.id
                weDotHave = weDotHave+1

            #學校這堂課有被輸入近學校課程資料課嗎，沒有舊輸進去
            RawCoures = raw_course.objects.filter(rc_subjectid=b[1])
            if(RawCoures):
		if RawCoures[0].rc_department != str(b[7]):
			RawCoures[0].rc_department = b[7]
			RawCoures[0].save()
                rawHave = rawHave+1
            else:
                NewRawCourse = raw_course.objects.create(rc_name=b[3], rc_teacher=b[5], rc_semester=b[0], rc_subjectid=b[1], rc_credit=b[2], rc_weekday=b[8].decode('utf8')[0], rc_time=b[8].decode('utf8')[1:],rc_room="",c_id=CourseId)
                #return HttpResponse(b[8].decode('utf8')[1:])   
                rawDotHave = rawDotHave+1
	     
		
        LineLenth = LineLenth+1     


    #return HttpResponse(json.dumps(unicode(b[3])))
    return HttpResponse('csv長度:'+str(LineLenth)+' 課程已有:'+str(weHave)+' 課程未有:'+str(weDotHave)+' 學校課程已有:'+str(rawHave)+' 學校課程未有:'+str(rawDotHave))

@csrf_exempt
def courses_save(request):
    if request.method == 'POST':        
        sessionid = request.POST.get('sessionid') 
        s = Session.objects.get(pk=str(sessionid)) #From django_session table 
        s_data = s.get_decoded() #s_data is a dictionary
        user_id = s_data['_auth_user_id'] 

        course_name = request.POST.getlist('course_name[]')
        course_code = request.POST.getlist('course_code[]')
        course_score = request.POST.getlist('course_score[]')
        course_year = request.POST.getlist('course_year[]')
        course_semester = request.POST.getlist('course_semester[]')
        final = zip(course_name,course_code,course_score,course_year,course_semester)

	#print user_id
	IsUserHaveCourse = user_course.objects.filter(u_id = user_id)
	if(IsUserHaveCourse):
	    print 'nogo'
	else:
            for i in final:
                #RawCourese = raw_course.objects.filter(rc_subjectid=str(i[1]) , rc_semester=str(i[3])+"/"+str(i[4]))
	        RawCourese = raw_course.objects.filter(rc_name=i[0])
                if(RawCourese):
                    user_course.objects.create(u_id = user_id, c_id = RawCourese[0].c_id, uc_grade = i[2] )
                #print i[1]
                #result_list = [{'result':'success'}]
        return HttpResponse('success')
    else:
        return HttpResponse('error')




@csrf_exempt
def get_recommend(request):
    result_list = list()

    if 1 == 1:
        #判斷是否登入，沒有登入則return not login
        if request.user.is_authenticated():  
           user_id = request.user.id
           if user_id == 1:
               result_list = [{'result':'no jimmy'}]
               return HttpResponse(json.dumps(result_list))
        else:
            result_list = [{'result':'notlogin'}]
            return HttpResponse(json.dumps(result_list))
        
        #取回所有評分資料
        for row in course_score.objects.all().order_by('u_id'):
            temp_dict = {'user_id':row.u_id, 
                         'course_id':row.c_id.id, 
                         'score':row.cs_score, 
                         'comment':row.cs_comment}
            result_list.append(temp_dict)
        #將評分資料做成crab格式
        crabdata = getCrabFormat(result_list)

#        return HttpResponse((result_list))
        #推薦系統
        model = MatrixPreferenceDataModel(crabdata)
        similarity = UserSimilarity(model, pearson_correlation)
        recommender = UserBasedRecommender(model, similarity, with_preference=True)
        recommend_list = recommender.recommend(user_id)
  
#        return HttpResponse((recommend_list))
        recommend_list = [ list(recommend_list[i]) for i in range(0, len(recommend_list))]

        
        #推薦後資料加上課程名稱、課程資訊...
        result_list = list()
        for i in range(0, len(recommend_list)):
            for course_row in course.objects.filter(id=recommend_list[i][0]):
                tem_dict = {'name':course_row.c_name,
                            'teacher':course_row.c_teacher,
                            'credit':course_row.raw_course_set.all()[0].rc_credit,
                            'depart':course_row.raw_course_set.all()[0].rc_department,
                            'semester':course_row.raw_course_set.all()[0].rc_semester,
                            'c_id':recommend_list[i][0],
                            'raw_cid':course_row.raw_course_set.all()[0].id,
                            'score':recommend_list[i][1]}
                result_list.append(tem_dict)    

        return HttpResponse(json.dumps(result_list))
    else:
        result_list = [{'result':'error'}]
        return HttpResponse(json.dumps(result_list))


@csrf_exempt
def score(request):
    if request.method == 'GET':
      
        if request.user.is_authenticated():  
           user_id = request.user.id
           if user_id == 1:
               result_list = [{'result':'no jimmy'}]
               return HttpResponse(json.dumps(result_list))
        else:
            result_list = [{'result':'not login'}]
            return HttpResponse(json.dumps(result_list))
        score = int(request.GET.get('score'))  
        course_id = int(request.GET.get('course_id'))
        comment = request.GET.get('comment')
        c = course.objects.get(id=course_id)
        course_score.objects.create(u_id=user_id, c_id=c, cs_score=score, cs_comment=comment)
        result_list = [{'result':'success'}]
        return HttpResponse(json.dumps(result_list))
    else:
        result = [{'result':'error'}]
        return HttpResponse(json.dumps(result))

def getCrabFormat(data):
    result = dict()
    temp_dict = dict()

    for i in range(0, len(data)):
        temp_dict[data[i]['course_id']] = data[i]['score']

        if i < len(data)-1:
            if data[i]['user_id'] != data[i+1]['user_id']:
                result[data[i]['user_id']] = temp_dict
                temp_dict = dict()      

    result[data[len(data)-1]['user_id']] = temp_dict
    return result

