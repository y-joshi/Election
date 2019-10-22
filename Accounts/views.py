from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
import http.client
import face_recognition
import base64

import random
from .models import Voter, Candidate, Party, Alliance, Constituency, Constituency_Votes, Constituency_Result, \
    Alliance_Result, Party_Result
from django.views.decorators.csrf import csrf_protect


# Create your views here.
otpg = "1234"


def login(request):
    loginerror = ""
    if request.method == 'POST':
        username = request.POST['voterid']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)

            # otp sending
            conn = http.client.HTTPConnection("2factor.in")
            payload = ""
            mobileno = 9725712667
            # otp = random.randint(100000, 999999)
            otp = 1234
            headers = {'content-type': "application/x-www-form-urlencoded"}
            smsrequest = "/API/V1/4bdb0a52-db4a-11e9-ade6-0200cd936042/SMS/" + str(mobileno) + "/" + str(otp)
            conn.request("GET", smsrequest, payload, headers)
            res = conn.getresponse()
            # data = res.read()
            #print("OTP sent is : "+ str(otp))
            return render(request, 'OTPverify.html')

        else:
            loginerror = "Invalid username or password"
            return render(request, 'login.html', {'loginerror': loginerror})
    else:
        return render(request, 'login.html', {'loginerror': loginerror})


def register(request):
    if request.method == 'POST':
        vid = request.POST['voterid']
        name = request.POST['name']
        fathername = request.POST['fathername']
        password = request.POST['pass']
        img = request.POST['image']
        gender = request.POST['gender']
        dob = request.POST['dob']
        mobileno = request.POST['mobileno']
        age = request.POST['age']
        voteriderror = ""
        if User.objects.filter(username=vid).exists():
            voteriderror = "This voter id is already registered!!"
            return render(request, 'register.html', {'voteriderror': voteriderror})
        else:
            user = User.objects.create_user(username=vid, password=password, first_name=name)
            user.save()
            voter = Voter(vid=vid, name=name, fathername=fathername, img=img, gender=gender, dob=dob, mobileno=mobileno,
                          age=age)
            voter.save()
            return redirect('/')
    else:
        return render(request, 'register.html')


def home(request):
    if request.method == 'POST':
        data = request.POST.copy()
        pid = data.get('cand_list')
        party = Party.objects.get(pk=pid)
        constituency_Votes = Constituency_Votes.objects.get(party=party)
        constituency_Votes.votes = constituency_Votes.votes + 1
        constituency_Votes.save()

        user = request.user
        vid = user.username
        voter = Voter.objects.get(vid=vid)
        voter.voted = True
        voter.save()
        return render(request, 'Exit.html')
    else:
        username = request.user.username
        voter = Voter.objects.get(vid=username)
        const = voter.constituency
        candidates = Candidate.objects.filter(constituency=const)
        return render(request, 'home.html', {'candidates': candidates})


def Result(request):
    constitueny_votes = Constituency_Votes.objects.all();
    return render(request, 'Result.html', {'const_votes': constitueny_votes})


def OTPverify(request):
    if request.method == 'POST':
        otp = request.POST.get('otp', False)
        if otp == otpg:
            return render(request, 'FaceRecognition.html')
        else:
            otperror = "OTP is not matching!!"
            #print(otperror)
            return render(request, 'OTPverify.html', {'otperror': otperror})

    else:
        otperror = "OTP sent Successfully."
        # otp sending
        conn = http.client.HTTPConnection("2factor.in")
        payload = ""
        mobileno = 9725712667
        # otp = random.randint(100000, 999999)
        otp = 1234
        headers = {'content-type': "application/x-www-form-urlencoded"}
        smsrequest = "/API/V1/4bdb0a52-db4a-11e9-ade6-0200cd936042/SMS/" + str(mobileno) + "/" + str(otp)
        # conn.request("GET", smsrequest, payload, headers)
        # res = conn.getresponse()
        # data = res.read()
        return render(request, 'OTPverify.html', {'otperror': otperror})

@csrf_protect
def FaceRecognition(request):
    if request.method == 'POST':
        image_base64 = request.POST.get('imgBase64')
        image_base64 = str(image_base64)
        image_base64 = image_base64.partition(",")[2]
        #msg =request.POST.get('message')
        #print(str(image_base64))
        #print(image_base64)
        image_data = base64.b64decode(image_base64)

        #image = open("image64.png", "wb")
        #image.write(base64.decode('base64'))
        #image.close()

        filename = 'image64.jpg'
        with open(filename, 'wb') as f:
            f.write(image_data)

        username = request.user.username
        voter = Voter.objects.get(vid=username)
        voterimage = "media/" + str(voter.img)


        known_image = face_recognition.load_image_file(voterimage)
        unknown_image = face_recognition.load_image_file(filename)

        biden_encodings = face_recognition.face_encodings(known_image)[0]
        unknown_encodings = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces([biden_encodings], unknown_encodings)
        if results[0] == True:
            print("Face is Matched!!")
        else:
            print("Face is not Matching!!")

        #username = request.user.username
        #voter = Voter.objects.get(vid=username)
        #const = voter.constituency
        #candidates = Candidate.objects.filter(constituency=const)
        #return render(request, 'home.html', {'candidates': candidates})
        return render(request, 'FaceRecognition.html')
    else:
        return render(request, 'FaceRecognition.html')


