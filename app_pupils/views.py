from django.shortcuts import render

pupils=[

     {'id':1,'name':"Inomjon Qurbonov",'bal1':2,'bal2':4,'bal3':1,'bal4':5,'bal5':10,'bal6':5,'bal7':5,'bal8':5,'jami':37},
     {'id':2,'name':"Muhammadyusuf Abduvaliyev",'bal1':3,'bal2':5,'bal3':2,'bal4':4,'bal5':10,'bal6':4,'bal7':5,'bal8':3,'jami':36},
     {'id':3,'name':"Shohruhbek Turdialiyev",'bal1':3,'bal2':0,'bal3':2,'bal4':3,'bal5':10,'bal6':3,'bal7':5,'bal8':3,'jami':29},
     {'id':4,'name':"Zafarbek Olimboyev",'bal1':3,'bal2':5,'bal3':2,'bal4':5,'bal5':10,'bal6':4,'bal7':5,'bal8':5,'jami':39},
     {'id':5,'name':"Samariddin Baxtiyorov",'bal1':2,'bal2':5,'bal3':2,'bal4':3,'bal5':10,'bal6':1,'bal7':5,'bal8':3,'jami':31}

]


def talaba(request):

    global pupils

    return render(request, 'pupils.html', {'pupils': pupils})


def talaba1(request,pk):
    global puplis
    return render(request, 'pupil.html', {"puplil": pupils[pk-1]})

