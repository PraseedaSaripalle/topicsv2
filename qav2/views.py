import json
from django.http import JsonResponse
from django.shortcuts import render

from pydoc_data.topics import topics
from wsgiref.util import request_uri
from qav2.models import Answer, Question, Topic
from django.template.loader import render_to_string

def topic(request):
    print("in topic section")
    topics=list()
    if 'term' in request.GET:
        print("inside topic if condition")
        qs=Topic.objects.filter(topic_name__istartswith=request.GET.get("term"))   
        print("json object in topic function. 1", qs)
        for topic in qs:
            topics.append(topic.topic_name)
            print("json object in topic function.2 ")
        return JsonResponse(topics, safe=False)
    return render(request,"topicssummary.html",{'topics':topics})

def retireveTopic(request):
    print("inside retrieve topic")
    #topic=Topic.objects.all()
    topic=Topic.objects.filter(topic_level=1)
    print("My topics",topic)
    
    return render(request,'topic.html',{'topic':topic})

def retireveSubTopicTemp(request):
    print("inside retireveSubTopitemp")
    if request.method == 'GET':
        topic_name=request.GET['topicname']
        print("topic_name", topic_name)
        topic=Topic.objects.get(topic_name=topic_name)
        subtopics=topic.children.all()
        print("My subtopics",subtopics)
        html = render_to_string('topicssummary.html', {"topics":subtopics})
        return JsonResponse(html, safe=False)
    return render(request,"topic.html",{"topic":subtopics})

def retireveSubTopic(request,topic_name):
    print("inside retireveSubTopi")
    print("topic_name", topic_name)
    topic=Topic.objects.get(topic_name=topic_name)
    subtopics=topic.children.all()
    print("My subtopics",subtopics)
    return render(request,'topicssummary.html',{'topic':subtopics})

def retireveQTopic(request):
    print("inside retrieve topic")
    #topic=Topic.objects.all()
    topic=Topic.objects.all()
    print("My topics",topic)
    return render(request,'topicquestions.html',{'topic':topic})

def questionDetails(request, topic_name):
    print("Displaying the details of the subtopics and the questions.")
    #Retrieving the Subtopics for a given topic
    print("topic_name",topic_name)
    rquestions=Question.objects.all().filter(topics__topic_name=topic_name)
    #or question in rquestions:
        #print("each question in loop", question)
        #
        #print("answer", ranswer)
    #print("answers",ranswers)
    print("questions for that topic",rquestions)

    return render(request,'questions.html',{'questions':rquestions})

def AnswerDetails(request,question_text):
    print("Displaying the details of answers")
    ranswers=Answer.objects.all().filter(question__question_text=question_text)
    print("The answers for the particular Question are",ranswers)
    return render(request,'answers.html',{'answers':ranswers})

