from django.urls import path
from . import views

urlpatterns= [
    path('home/', views.topic, name='topic'),
    #path('home/',views.retireveTopic),
    #path('home/tques/',views.detailTopic),
    path('tmques/', views.retireveTopic, name='tmques'),
    path('tsubques/', views.retireveSubTopicTemp, name='tsubquestemp'),
    #path('tsubques/(<topic_name>)/', views.retireveSubTopic, name='tsubques'),
    path('tques/',views.retireveQTopic, name='tques'),
    path('questions/(<topic_name>)/',views.questionDetails,name='questions'),
    path('answers/(<question_text>)/',views.AnswerDetails,name='answers'),
    
]