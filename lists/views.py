from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Term1,Term2,Term3,Term4,Term5,Term6,Term7,Term8,GPA
from lists.models import Userinfo

# แสดงหน้าหลักของ GradeGuide
def home_page(request):
    # render หน้า home.html
    return render(request, 'home.html')

# count user ที่มา register
def register(request):
    # เก็บ GPA ลง dataGPA
    dataGPA = GPA.objects.all()

    # ถ้าความยาวของ dataGPA เป็น 0
    if len(dataGPA) == 0:
        # ให้สร้าง GPA ตั้งแต่เทอมแรกจนถึงเทอมสุดท้าย โดยค่าแรกของแต่ละเทอมเป็น 0
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )

    # นับ User ที่มา register
    count = User.objects.count()

    # render หน้า index.html และบอกจำนวนที่ user มา register
    return render(request, 'index.html', {
        'count': count
    })

# หน้า sign up
def signup(request):
    # ถ้า request เป็น post
    if request.method == 'POST':
        # เก็บ form สร้าง User ไว้ที่ form
        form = UserCreationForm(request.POST)
        # ถ้า form นี้ถูกต้อง
        if form.is_valid():
            # ให้ save form นี้ไว้ใน user
            user = form.save()
            # ให้ refresh user จาก database
            user.refresh_from_db()
            # get username
            username = form.cleaned_data.get('username')
            # get password
            raw_password = form.cleaned_data.get('password1')
            # สร้าง username จาก username ที่ได้พิมพ์ไป
            Userinfo.objects.create(name=username)
            # save user
            user.save()
            # user เก็บทั้ง username และ password
            user = authenticate(username=username, password=raw_password)
            # log in โดยใช้ user ที่สร้างมา
            login(request, user)
            # return กลับไปที่หน้า home
            return redirect('home')
    else:
        form = UserCreationForm()
    # render หน้า signup.html พร้อมใช้ form ที่จะสร้าง user
    return render(request, 'registration/signup.html', {
        'form': form
    })

# calculate the grade
def calGrade(request):
    term1 = Term1()
    term2 = Term2()
    # เก้บ Plese check your infromation before saving. ไว้ใน not_input
    not_input = "Plese check your infromation before saving."
    # บวกหน่วยกิตกับเกรดของทุกวิชาเก็บไว้ที่ checkinput
    checkinput = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject1Grade'))+\
                 float(request.POST.get('subject2Unit')) + float(request.POST.get('subject2Grade'))+\
                 float(request.POST.get('subject3Unit')) + float(request.POST.get('subject3Grade'))+\
                 float(request.POST.get('subject4Unit')) + float(request.POST.get('subject4Grade'))+\
                 float(request.POST.get('subject5Unit')) + float(request.POST.get('subject5Grade'))+\
                 float(request.POST.get('subject6Unit')) + float(request.POST.get('subject6Grade'))+\
                 float(request.POST.get('subject7Unit')) + float(request.POST.get('subject7Grade'))+\
                 float(request.POST.get('subject8Unit')) + float(request.POST.get('subject8Grade'))+\
                 float(request.POST.get('subject9Unit')) + float(request.POST.get('subject9Grade'))

    # ถ้าความยาวของวิชาในเทอม 1 น้อยกว่าหรือเท่ากับ 9
    if len(Term1.objects.all()) <= 9:

        # ------------------------------------------------------ Term 1 -------------------------------------------------------------
        # ถ้า value ของ subjectTerm มีค่าเท่ากับ 1 (ถ้าเลือกเทอม 1)
        if request.POST.get('subjectTerm') == "1":
            # ถ้า checkinput รวมแล้วมีค่าเท่ากับ 0.0
            if checkinput == 0.0:
                # ให้ render หน้า home.html พร้อมบอกตามตัวแปร notinput ที่ได้กำหนดไว้ข้างต้น
                return render(request, 'home.html', {'notinput': not_input})
            # ให้แต่ละวิชาคูณจำนวนหน่วยกิตและเกรดที่ได้เก็บไว้ใน sub1 - sub9 ตามลำดับ
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            sub9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))

            # เก็บผลบวกของหน่วยกิตทุกวิชาไว้ใน sumunit
            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit')
            )

            # นำ sub1 บวกไปจนถึง sub9 เก็บไว้ที่ sumsub
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9
            # นำ sumsub หารด้วย sumunit เก็บไว้ใน res ซึ่งเป็นเกรดในเทอมนี้
            res = sumsub / sumunit

            # ถ้าความยาวของวิชาในเทอม 1 มีค่าเท่ากับ 0
            if len(Term1.objects.all()) == 0 :
                # ให้สร้างช่องใส่ชื่อวิชา ช่องเลือกหน่วยกิต ช่องเลือกเกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term1.objects.create(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)

                Term1.objects.create(subject=request.POST['subject2name'],unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)

                Term1.objects.create(subject =request.POST['subject3name'],unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)

                Term1.objects.create(subject =request.POST['subject4name'],unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)

                Term1.objects.create(subject =request.POST['subject5name'],unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)

                Term1.objects.create(subject=request.POST['subject6name'],unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)

                Term1.objects.create(subject =request.POST['subject7name'],unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)

                Term1.objects.create(subject=request.POST['subject8name'],unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)

                Term1.objects.create(subject=request.POST['subject9name'],unit=request.POST['subject9Unit'],Grade=request.POST['subject9Grade'],GPA=res)

                # update GPA term 1 
                GPA.objects.filter(pk=1).update(GPA_1=res)

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

            # other
            else:
                # update ช่องใส่ชื่อวิชา ช่องเลือกหน่วยกิต ช่องเลือกเกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term1.objects.filter(pk=1).update(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)
                Term1.objects.filter(pk=2).update(subject =request.POST['subject2name'], unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)
                Term1.objects.filter(pk=3).update(subject =request.POST['subject3name'], unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)
                Term1.objects.filter(pk=4).update(subject =request.POST['subject4name'], unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)
                Term1.objects.filter(pk=5).update(subject =request.POST['subject5name'], unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)
                Term1.objects.filter(pk=6).update(subject =request.POST['subject6name'], unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)
                Term1.objects.filter(pk=7).update(subject =request.POST['subject7name'], unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)
                Term1.objects.filter(pk=8).update(subject =request.POST['subject8name'], unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)
                Term1.objects.filter(pk=9).update(subject =request.POST['subject9name'], unit=request.POST['subject9Unit'],Grade=request.POST['subject9Grade'],GPA=res)

                # update GPA term 1 
                GPA.objects.filter(pk=1).update(GPA_1=res)

                # เก็บ ชื่อวิชา หน่วยกิต เกรด ของแต่ละวิชาไว้ใน data
                data = Term1.objects.all()
                # ให้ res หรือ GPA ที่คำนวณไว้ก่อนหน้านี้ เก็บไว้ใน term1.GPA
                term1.GPA = res
                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

        # ------------------------------------------------------ Term 2 -------------------------------------------------------------
        # ถ้า value ของ subjectTerm มีค่าเท่ากับ 2 (ถ้าเลือกเทอม 2)
        if request.POST.get('subjectTerm') == "2":
            # ถ้า checkinput รวมแล้วมีค่าเท่ากับ 0.0
            if checkinput == 0.0:
                # ให้ render หน้า home.html พร้อมบอกตามตัวแปร notinput ที่ได้กำหนดไว้ข้างต้น
                return render(request, 'home.html', {'notinput': not_input})
            # ให้แต่ละวิชาคูณจำนวนหน่วยกิตและเกรดที่ได้เก็บไว้ใน sub1 - sub9 ตามลำดับ
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            sub9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))

            # เก็บผลบวกของหน่วยกิตทุกวิชาไว้ใน sumunit
            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit')
            )

            # นำ sub1 บวกไปจนถึง sub9 เก็บไว้ที่ sumsub
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9
            # นำ sumsub หารด้วย sumunit เก็บไว้ใน res ซึ่งเป็นเกรดในเทอมนี้
            res = sumsub / sumunit

            # ถ้าความยาวของวิชาในเทอม 2 มีค่าเท่ากับ 0
            if len(Term2.objects.all()) == 0 :
                # ให้สร้างช่องใส่ชื่อวิชา ช่องเลือกหน่วยกิต ช่องเลือกเกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term2.objects.create(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)

                Term2.objects.create(subject=request.POST['subject2name'],unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)

                Term2.objects.create(subject =request.POST['subject3name'],unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)

                Term2.objects.create(subject =request.POST['subject4name'],unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)

                Term2.objects.create(subject =request.POST['subject5name'],unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)

                Term2.objects.create(subject=request.POST['subject6name'],unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)

                Term2.objects.create(subject =request.POST['subject7name'],unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)

                Term2.objects.create(subject=request.POST['subject8name'],unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)

                Term2.objects.create(subject=request.POST['subject9name'],unit=request.POST['subject9Unit'],Grade=request.POST['subject9Grade'],GPA=res)

                # update GPA term 2
                GPA.objects.filter(pk=1).update(GPA_2=res)

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

            # other
            else:
                # update ช่องใส่ชื่อวิชา ช่องเลือกหน่วยกิต ช่องเลือกเกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term2.objects.filter(pk=1).update(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)
                Term2.objects.filter(pk=2).update(subject =request.POST['subject2name'], unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)
                Term2.objects.filter(pk=3).update(subject =request.POST['subject3name'], unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)
                Term2.objects.filter(pk=4).update(subject =request.POST['subject4name'], unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)
                Term2.objects.filter(pk=5).update(subject =request.POST['subject5name'], unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)
                Term2.objects.filter(pk=6).update(subject =request.POST['subject6name'], unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)
                Term2.objects.filter(pk=7).update(subject =request.POST['subject7name'], unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)
                Term2.objects.filter(pk=8).update(subject =request.POST['subject8name'], unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)
                Term2.objects.filter(pk=9).update(subject =request.POST['subject9name'], unit=request.POST['subject9Unit'],Grade=request.POST['subject9Grade'],GPA=res)

                # update GPA term 2
                GPA.objects.filter(pk=1).update(GPA_2=res)

                # ให้ res หรือ GPA ที่คำนวณไว้ก่อนหน้านี้ เก็บไว้ใน term2.GPA
                term2.GPA = res
                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

        # ------------------------------------------------------ Term 3 -------------------------------------------------------------
        # ถ้า value ของ subjectTerm มีค่าเท่ากับ 3 (ถ้าเลือกเทอม 3)
        if request.POST.get('subjectTerm') == "3":
            # ถ้า checkinput รวมแล้วมีค่าเท่ากับ 0.0
            if checkinput == 0.0:
                # ให้ render หน้า home.html พร้อมบอกตามตัวแปร notinput ที่ได้กำหนดไว้ข้างต้น
                return render(request, 'home.html', {'notinput': not_input})
            # ให้แต่ละวิชาคูณจำนวนหน่วยกิตและเกรดที่ได้เก็บไว้ใน sub1 - sub9 ตามลำดับ
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            sub9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))

            # เก็บผลบวกของหน่วยกิตทุกวิชาไว้ใน sumunit
            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit')
            )

            # นำ sub1 บวกไปจนถึง sub9 เก็บไว้ที่ sumsub
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9
            # นำ sumsub หารด้วย sumunit เก็บไว้ใน res ซึ่งเป็นเกรดในเทอมนี้
            res = sumsub / sumunit

            # ถ้าความยาวของวิชาในเทอม 3 มีค่าเท่ากับ 0
            if len(Term3.objects.all()) == 0 :
                # ให้สร้างช่องใส่ชื่อวิชา ช่องเลือกหน่วยกิต ช่องเลือกเกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term3.objects.create(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)

                Term3.objects.create(subject=request.POST['subject2name'],unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)

                Term3.objects.create(subject =request.POST['subject3name'],unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)

                Term3.objects.create(subject =request.POST['subject4name'],unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)

                Term3.objects.create(subject =request.POST['subject5name'],unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)

                Term3.objects.create(subject=request.POST['subject6name'],unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)

                Term3.objects.create(subject =request.POST['subject7name'],unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)

                Term3.objects.create(subject=request.POST['subject8name'],unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)

                Term3.objects.create(subject=request.POST['subject9name'],unit=request.POST['subject9Unit'],Grade=request.POST['subject9Grade'],GPA=res)

                # update GPA term 3
                GPA.objects.filter(pk=1).update(GPA_3=res)

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

            # other    
            else:
                # update ช่องใส่ชื่อวิชา ช่องเลือกหน่วยกิต ช่องเลือกเกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term3.objects.filter(pk=1).update(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)
                Term3.objects.filter(pk=2).update(subject =request.POST['subject2name'], unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)
                Term3.objects.filter(pk=3).update(subject =request.POST['subject3name'], unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)
                Term3.objects.filter(pk=4).update(subject =request.POST['subject4name'], unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)
                Term3.objects.filter(pk=5).update(subject =request.POST['subject5name'], unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)
                Term3.objects.filter(pk=6).update(subject =request.POST['subject6name'], unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)
                Term3.objects.filter(pk=7).update(subject =request.POST['subject7name'], unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)
                Term3.objects.filter(pk=8).update(subject =request.POST['subject8name'], unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)
                Term3.objects.filter(pk=9).update(subject =request.POST['subject9name'], unit=request.POST['subject9Unit'],Grade=request.POST['subject9Grade'],GPA=res)
                
                # update GPA term 3
                GPA.objects.filter(pk=1).update(GPA_3=res)

                # ให้ res หรือ GPA ที่คำนวณไว้ก่อนหน้านี้ เก็บไว้ใน term3.GPA
                term3.GPA = res
                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

        # ------------------------------------------------------ Term 4 -------------------------------------------------------------
        # ถ้า value ของ subjectTerm มีค่าเท่ากับ 4 (ถ้าเลือกเทอม 4)
        if request.POST.get('subjectTerm') == "4":
            # ถ้า checkinput รวมแล้วมีค่าเท่ากับ 0.0
            if checkinput == 0.0:
                # ให้ render หน้า home.html พร้อมบอกตามตัวแปร notinput ที่ได้กำหนดไว้ข้างต้น
                return render(request, 'home.html', {'notinput': not_input})
            # ให้แต่ละวิชาคูณจำนวนหน่วยกิตและเกรดที่ได้เก็บไว้ใน sub1 - sub9 ตามลำดับ
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            sub9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))

            # เก็บผลบวกของหน่วยกิตทุกวิชาไว้ใน sumunit
            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit')
            )

            # นำ sub1 บวกไปจนถึง sub9 เก็บไว้ที่ sumsub
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9
            # นำ sumsub หารด้วย sumunit เก็บไว้ใน res ซึ่งเป็นเกรดในเทอมนี้
            res = sumsub / sumunit

            # ถ้าความยาวของวิชาในเทอม 4 มีค่าเท่ากับ 0
            if len(Term4.objects.all()) == 0 :
                # ให้สร้างช่องใส่ชื่อวิชา ช่องเลือกหน่วยกิต ช่องเลือกเกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term4.objects.create(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)

                Term4.objects.create(subject=request.POST['subject2name'],unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)

                Term4.objects.create(subject =request.POST['subject3name'],unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)

                Term4.objects.create(subject =request.POST['subject4name'],unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)

                Term4.objects.create(subject =request.POST['subject5name'],unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)

                Term4.objects.create(subject=request.POST['subject6name'],unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)

                Term4.objects.create(subject =request.POST['subject7name'],unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)

                Term4.objects.create(subject=request.POST['subject8name'],unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)

                Term4.objects.create(subject=request.POST['subject9name'],unit=request.POST['subject9Unit'],Grade=request.POST['subject9Grade'],GPA=res)
                
                # update GPA term 4
                GPA.objects.filter(pk=1).update(GPA_4=res)

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

            # other
            else:
                # update ช่องใส่ชื่อวิชา ช่องเลือกหน่วยกิต ช่องเลือกเกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term4.objects.filter(pk=1).update(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)
                Term4.objects.filter(pk=2).update(subject =request.POST['subject2name'], unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)
                Term4.objects.filter(pk=3).update(subject =request.POST['subject3name'], unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)
                Term4.objects.filter(pk=4).update(subject =request.POST['subject4name'], unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)
                Term4.objects.filter(pk=5).update(subject =request.POST['subject5name'], unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)
                Term4.objects.filter(pk=6).update(subject =request.POST['subject6name'], unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)
                Term4.objects.filter(pk=7).update(subject =request.POST['subject7name'], unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)
                Term4.objects.filter(pk=8).update(subject =request.POST['subject8name'], unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)
                Term4.objects.filter(pk=9).update(subject =request.POST['subject9name'], unit=request.POST['subject9Unit'],Grade=request.POST['subject9Grade'],GPA=res)
                
                # update GPA term 4
                GPA.objects.filter(pk=1).update(GPA_4=res)

                # ให้ res หรือ GPA ที่คำนวณไว้ก่อนหน้านี้ เก็บไว้ใน term4.GPA
                term4.GPA = res

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

        # ------------------------------------------------------ Term 5 -------------------------------------------------------------
        # ถ้า value ของ subjectTerm มีค่าเท่ากับ 5 (ถ้าเลือกเทอม 5)                
        if request.POST.get('subjectTerm') == "5":
            # ถ้า checkinput รวมแล้วมีค่าเท่ากับ 0.0
            if checkinput == 0.0:
                # ให้ render หน้า home.html พร้อมบอกตามตัวแปร notinput ที่ได้กำหนดไว้ข้างต้น
                return render(request, 'home.html', {'notinput': not_input})
            # ให้แต่ละวิชาคูณจำนวนหน่วยกิตและเกรดที่ได้เก็บไว้ใน sub1 - sub9 ตามลำดับ
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            sub9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))

            # เก็บผลบวกของหน่วยกิตทุกวิชาไว้ใน sumunit
            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit')
            )

            # นำ sub1 บวกไปจนถึง sub9 เก็บไว้ที่ sumsub
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9
            # นำ sumsub หารด้วย sumunit เก็บไว้ใน res ซึ่งเป็นเกรดในเทอมนี้
            res = sumsub / sumunit

            # ถ้าความยาวของวิชาในเทอม 5 มีค่าเท่ากับ 0
            if len(Term5.objects.all()) == 0 :
                # ให้สร้างช่องใส่ชื่อวิชา ช่องเลือกหน่วยกิต ช่องเลือกเกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term5.objects.create(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)

                Term5.objects.create(subject=request.POST['subject2name'],unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)

                Term5.objects.create(subject =request.POST['subject3name'],unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)

                Term5.objects.create(subject =request.POST['subject4name'],unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)

                Term5.objects.create(subject =request.POST['subject5name'],unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)

                Term5.objects.create(subject=request.POST['subject6name'],unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)

                Term5.objects.create(subject =request.POST['subject7name'],unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)

                Term5.objects.create(subject=request.POST['subject8name'],unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)

                Term5.objects.create(subject=request.POST['subject9name'],unit=request.POST['subject9Unit'],Grade=request.POST['subject9Grade'],GPA=res)
                
                # update GPA term 5
                GPA.objects.filter(pk=1).update(GPA_5=res)

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

            # other
            else:
                # update ช่องใส่ชื่อวิชา ช่องเลือกหน่วยกิต ช่องเลือกเกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term5.objects.filter(pk=1).update(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)
                Term5.objects.filter(pk=2).update(subject =request.POST['subject2name'], unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)
                Term5.objects.filter(pk=3).update(subject =request.POST['subject3name'], unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)
                Term5.objects.filter(pk=4).update(subject =request.POST['subject4name'], unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)
                Term5.objects.filter(pk=5).update(subject =request.POST['subject5name'], unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)
                Term5.objects.filter(pk=6).update(subject =request.POST['subject6name'], unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)
                Term5.objects.filter(pk=7).update(subject =request.POST['subject7name'], unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)
                Term5.objects.filter(pk=8).update(subject =request.POST['subject8name'], unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)
                Term5.objects.filter(pk=9).update(subject =request.POST['subject9name'], unit=request.POST['subject9Unit'],Grade=request.POST['subject9Grade'],GPA=res)
                
                # update GPA term 5
                GPA.objects.filter(pk=1).update(GPA_5=res)

                # ให้ res หรือ GPA ที่คำนวณไว้ก่อนหน้านี้ เก็บไว้ใน term5.GPA
                term5.GPA = res

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

        # ------------------------------------------------------ Term 6 -------------------------------------------------------------
        # ถ้า value ของ subjectTerm มีค่าเท่ากับ 6 (ถ้าเลือกเทอม 6)   
        if request.POST.get('subjectTerm') == "6":
            # ถ้า checkinput รวมแล้วมีค่าเท่ากับ 0.0
            if checkinput == 0.0:
                # ให้ render หน้า home.html พร้อมบอกตามตัวแปร notinput ที่ได้กำหนดไว้ข้างต้น
                return render(request, 'home.html', {'notinput': not_input})
            # ให้แต่ละวิชาคูณจำนวนหน่วยกิตและเกรดที่ได้เก็บไว้ใน sub1 - sub9 ตามลำดับ
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            sub9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))

            # เก็บผลบวกของหน่วยกิตทุกวิชาไว้ใน sumunit
            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit')
            )

            # นำ sub1 บวกไปจนถึง sub9 เก็บไว้ที่ sumsub
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9
            # นำ sumsub หารด้วย sumunit เก็บไว้ใน res ซึ่งเป็นเกรดในเทอมนี้
            res = sumsub / sumunit

            # ถ้าความยาวของวิชาในเทอม 6 มีค่าเท่ากับ 0
            if len(Term6.objects.all()) == 0 :
                # ให้สร้างช่องใส่ชื่อวิชา ช่องเลือกหน่วยกิต ช่องเลือกเกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term6.objects.create(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)

                Term6.objects.create(subject=request.POST['subject2name'],unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)

                Term6.objects.create(subject =request.POST['subject3name'],unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)

                Term6.objects.create(subject =request.POST['subject4name'],unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)

                Term6.objects.create(subject =request.POST['subject5name'],unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)

                Term6.objects.create(subject=request.POST['subject6name'],unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)

                Term6.objects.create(subject =request.POST['subject7name'],unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)

                Term6.objects.create(subject=request.POST['subject8name'],unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)

                Term6.objects.create(subject=request.POST['subject9name'],unit=request.POST['subject9Unit'],Grade=request.POST['subject9Grade'],GPA=res)
                
                # update GPA term 6
                GPA.objects.filter(pk=1).update(GPA_6=res)

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

            # other
            else:
                # update ช่องใส่ชื่อวิชา ช่องเลือกหน่วยกิต ช่องเลือกเกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term6.objects.filter(pk=1).update(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)
                Term6.objects.filter(pk=2).update(subject =request.POST['subject2name'], unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)
                Term6.objects.filter(pk=3).update(subject =request.POST['subject3name'], unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)
                Term6.objects.filter(pk=4).update(subject =request.POST['subject4name'], unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)
                Term6.objects.filter(pk=5).update(subject =request.POST['subject5name'], unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)
                Term6.objects.filter(pk=6).update(subject =request.POST['subject6name'], unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)
                Term6.objects.filter(pk=7).update(subject =request.POST['subject7name'], unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)
                Term6.objects.filter(pk=8).update(subject =request.POST['subject8name'], unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)
                Term6.objects.filter(pk=9).update(subject =request.POST['subject9name'], unit=request.POST['subject9Unit'],Grade=request.POST['subject9Grade'],GPA=res)
                
                # update GPA term 6
                GPA.objects.filter(pk=1).update(GPA_6=res)

                # ให้ res หรือ GPA ที่คำนวณไว้ก่อนหน้านี้ เก็บไว้ใน term6.GPA
                term6.GPA = res

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

        # ------------------------------------------------------ Term 7 -------------------------------------------------------------
        # ถ้า value ของ subjectTerm มีค่าเท่ากับ 7 (ถ้าเลือกเทอม 7)   
        if request.POST.get('subjectTerm') == "7":
            # ถ้า checkinput รวมแล้วมีค่าเท่ากับ 0.0
            if checkinput == 0.0:
                # ให้ render หน้า home.html พร้อมบอกตามตัวแปร notinput ที่ได้กำหนดไว้ข้างต้น
                return render(request, 'home.html', {'notinput': not_input})
            # ให้แต่ละวิชาคูณจำนวนหน่วยกิตและเกรดที่ได้เก็บไว้ใน sub1 - sub9 ตามลำดับ
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            sub9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))

            # เก็บผลบวกของหน่วยกิตทุกวิชาไว้ใน sumunit
            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit')
            )

            # นำ sub1 บวกไปจนถึง sub9 เก็บไว้ที่ sumsub
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9
            # นำ sumsub หารด้วย sumunit เก็บไว้ใน res ซึ่งเป็นเกรดในเทอมนี้
            res = sumsub / sumunit

            # ถ้าความยาวของวิชาในเทอม 7 มีค่าเท่ากับ 0
            if len(Term7.objects.all()) == 0 :
                # ให้สร้างช่องใส่ชื่อวิชา ช่องเลือกหน่วยกิต ช่องเลือกเกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term7.objects.create(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)

                Term7.objects.create(subject=request.POST['subject2name'],unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)

                Term7.objects.create(subject =request.POST['subject3name'],unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)

                Term7.objects.create(subject =request.POST['subject4name'],unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)

                Term7.objects.create(subject =request.POST['subject5name'],unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)

                Term7.objects.create(subject=request.POST['subject6name'],unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)

                Term7.objects.create(subject =request.POST['subject7name'],unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)

                Term7.objects.create(subject=request.POST['subject8name'],unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)

                Term7.objects.create(subject=request.POST['subject9name'],unit=request.POST['subject9Unit'],Grade=request.POST['subject9Grade'],GPA=res)

                # update GPA term 7
                GPA.objects.filter(pk=1).update(GPA_7=res)

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

            # other
            else:
                # update ช่องใส่ชื่อวิชา ช่องเลือกหน่วยกิต ช่องเลือกเกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term7.objects.filter(pk=1).update(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)
                Term7.objects.filter(pk=2).update(subject =request.POST['subject2name'], unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)
                Term7.objects.filter(pk=3).update(subject =request.POST['subject3name'], unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)
                Term7.objects.filter(pk=4).update(subject =request.POST['subject4name'], unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)
                Term7.objects.filter(pk=5).update(subject =request.POST['subject5name'], unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)
                Term7.objects.filter(pk=6).update(subject =request.POST['subject6name'], unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)
                Term7.objects.filter(pk=7).update(subject =request.POST['subject7name'], unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)
                Term7.objects.filter(pk=8).update(subject =request.POST['subject8name'], unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)
                Term7.objects.filter(pk=9).update(subject =request.POST['subject9name'], unit=request.POST['subject9Unit'],Grade=request.POST['subject9Grade'],GPA=res)
                
                # update GPA term 7
                GPA.objects.filter(pk=1).update(GPA_7=res)

                # ให้ res หรือ GPA ที่คำนวณไว้ก่อนหน้านี้ เก็บไว้ใน term7.GPA
                term7.GPA = res

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

        # ------------------------------------------------------ Term 8 -------------------------------------------------------------
        # ถ้า value ของ subjectTerm มีค่าเท่ากับ 8 (ถ้าเลือกเทอม 8)   
        if request.POST.get('subjectTerm') == "8":
            # ถ้า checkinput รวมแล้วมีค่าเท่ากับ 0.0
            if checkinput == 0.0:
                # ให้ render หน้า home.html พร้อมบอกตามตัวแปร notinput ที่ได้กำหนดไว้ข้างต้น
                return render(request, 'home.html', {'notinput': not_input})
            # ให้แต่ละวิชาคูณจำนวนหน่วยกิตและเกรดที่ได้เก็บไว้ใน sub1 - sub9 ตามลำดับ
            sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            sub9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))

            # เก็บผลบวกของหน่วยกิตทุกวิชาไว้ใน sumunit
            sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit')
            )

            # นำ sub1 บวกไปจนถึง sub9 เก็บไว้ที่ sumsub
            sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9
            # นำ sumsub หารด้วย sumunit เก็บไว้ใน res ซึ่งเป็นเกรดในเทอมนี้
            res = sumsub / sumunit

            # ถ้าความยาวของวิชาในเทอม 8 มีค่าเท่ากับ 0
            if len(Term8.objects.all()) == 0 :
                # ให้สร้างช่องใส่ชื่อวิชา ช่องเลือกหน่วยกิต ช่องเลือกเกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term8.objects.create(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)

                Term8.objects.create(subject=request.POST['subject2name'],unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)

                Term8.objects.create(subject =request.POST['subject3name'],unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)

                Term8.objects.create(subject =request.POST['subject4name'],unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)

                Term8.objects.create(subject =request.POST['subject5name'],unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)

                Term8.objects.create(subject=request.POST['subject6name'],unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)

                Term8.objects.create(subject =request.POST['subject7name'],unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)

                Term8.objects.create(subject=request.POST['subject8name'],unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)

                Term8.objects.create(subject=request.POST['subject9name'],unit=request.POST['subject9Unit'],Grade=request.POST['subject9Grade'],GPA=res)

                # update GPA term 8
                GPA.objects.filter(pk=1).update(GPA_8=res)

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

            # other
            else:
                # update ช่องใส่ชื่อวิชา ช่องเลือกหน่วยกิต ช่องเลือกเกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term8.objects.filter(pk=1).update(subject =request.POST['subject1name'], unit=request.POST['subject1Unit'],Grade=request.POST['subject1Grade'],GPA=res)
                Term8.objects.filter(pk=2).update(subject =request.POST['subject2name'], unit=request.POST['subject2Unit'],Grade=request.POST['subject2Grade'],GPA=res)
                Term8.objects.filter(pk=3).update(subject =request.POST['subject3name'], unit=request.POST['subject3Unit'],Grade=request.POST['subject3Grade'],GPA=res)
                Term8.objects.filter(pk=4).update(subject =request.POST['subject4name'], unit=request.POST['subject4Unit'],Grade=request.POST['subject4Grade'],GPA=res)
                Term8.objects.filter(pk=5).update(subject =request.POST['subject5name'], unit=request.POST['subject5Unit'],Grade=request.POST['subject5Grade'],GPA=res)
                Term8.objects.filter(pk=6).update(subject =request.POST['subject6name'], unit=request.POST['subject6Unit'],Grade=request.POST['subject6Grade'],GPA=res)
                Term8.objects.filter(pk=7).update(subject =request.POST['subject7name'], unit=request.POST['subject7Unit'],Grade=request.POST['subject7Grade'],GPA=res)
                Term8.objects.filter(pk=8).update(subject =request.POST['subject8name'], unit=request.POST['subject8Unit'],Grade=request.POST['subject8Grade'],GPA=res)
                Term8.objects.filter(pk=9).update(subject =request.POST['subject9name'], unit=request.POST['subject9Unit'],Grade=request.POST['subject9Grade'],GPA=res)
                
                # update GPA term 8
                GPA.objects.filter(pk=1).update(GPA_8=res)

                # ให้ res หรือ GPA ที่คำนวณไว้ก่อนหน้านี้ เก็บไว้ใน term8.GPA
                term8.GPA = res

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

        # other 
        else:
            # เก็บ Please select term before saving grade ไว้ใน message
            message = 'Please select term before saving grade'
            # render home.html พร้อมบอก message ตามข้างต้นที่ได้กำหนดไว้
            return render(request, 'home.html',{'message':message})

# เลือกเทอม
def termselect(request):
    # เก็บเทอมที่เลือกไว้ที่ termsel
    termsel=str(request.POST.get('selectterm'))
    # render หน้า home.html พร้อมบอกเทอมที่เลือก
    return render(request, 'home.html', {'term1': termsel})

# Search หาวิชาที่ต้องการดูตัวต่อของวิชานั้น ๆ
def flow(request):
    # เก็บ Result เป็นช่องว่าง
    Result = ''
    # เก็บ text input ที่จะ search เป็น string
    subjects = str(request.POST.get('searchFlow',''))
    # ถ้ามีการกดปุ่ม search
    if 'searchSubject' in request.POST :
        # ถ้า text input เป็นวิชานี้ ให้ Result เป็นวิชานี้
        # 1 ProFund
        if subjects == "Programming Fundamental" :
            Result = """Semister2 : Algorithms and Data Structures <br />
            Semister5 : Operating Systems"""

        # 2 MathI
        elif subjects == "Engineering Mathematics I" :
            Result = """Semister2 : Math II <br />
            Semister3 : Statistics for Computer Engineer"""

        # 3 ComExplo
        elif subjects == "Computer Engineering Exploration" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 4 PhysicsI
        elif subjects == "Physics I" :
            Result = "Semister2 : Physics II"

        # 5 PhyLabI
        elif subjects == "Physics Laboratory I" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 6 EnglishI
        elif subjects == "Language Elective Course I" :
            Result = "Language Elective Course II"

        # 7 TableTennis
        elif subjects == "Physical Education Elective Course I" :
            Result = "Physical Education Elective Course II"

        # 8 ManSo
        elif subjects == "Social Sciences Elective Course" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 9 Intro
        elif subjects == "Introduction to Engineer" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 10 Circuit
        elif subjects == "Electric Circuit Theory" :
            Result = "Semister4 : Analog and Digital Electronics"

        # 11 CircuitLab
        elif subjects == "Electric Circuit Lab" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 12 Algo
        elif subjects == "Algorithms and Data Structure" :
            Result = """Semister3 : Software Development Practice I <br />
            Semister5 : Computer Organization <br />
            Semister6 : Database Systems"""

        # 13 Work Ethics
        elif subjects == "Work Ethics" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 14 MathII
        elif subjects == "Engineering Mathematics II" :
            Result = """Semister3 : Discrete Mathematics <br />
            Semister3 : Introduction to Signals and System"""

        # 15 PhysicsII
        elif subjects == "Physics II" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 16 PhyLab2
        elif subjects == "Physics Laboratory II" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 17 EnglishII
        elif subjects == "Language Elective Course II" :
            Result = "Language Elective Course III"

        # 18 Basketball
        elif subjects == "Physical Education Elective Course II" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 19 Stat
        elif subjects == "Statistics for Computer Engineer" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 20 Signal
        elif subjects == "Introduction to Signals and System" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 21 Digital
        elif subjects == "Logic Design of Digital System" :
            Result = """Semister3 : Digital System Design Laboratory <br />
            Semister4 : Computer Organization"""

        # 22 DigiLab
        elif subjects == "Digital System Design Laboratory" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 23 SoftwareI
        elif subjects == "Software Development Practice I" :
            Result = "Semister4 : Software Development Practice II"

        # 24 Discrete Math
        elif subjects == "Discrete Mathematics" :
            Result = "Semister6 : Database Systems"

        # 25 PhyLife
        elif subjects == "Science and Maths Elective I" :
            Result = "Science and Maths Elective II"

        # 26 SoftwareII
        elif subjects == "Software Development Practice II" :
            Result = "Semister5 : Software Engineering"

        # 27 NetworkI
        elif subjects == "Computer Networks I" :
            Result = "Semister5 : Computer Networks II"

        # 28 ComOr
        elif subjects == "Computer Organization" :
            Result = "Semister5 : Embedded System Design"

        # 29 Ubi
        elif subjects == "Ubiquitous Computing" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 30 Analog
        elif subjects == "Analog and Digital Electronics" :
            Result = "Semister5 : Analog and Digital Electronics Lab"

        # 31 GenMath
        elif subjects == "Science and Maths Elective II" :
            Result = "Science and Maths Elective III"

        # 32 SoftEng
        elif subjects == "Software Engineering" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 33 NetworkII
        elif subjects == "Computer Networks II" :
            Result = "Semister6 : Computer Networks Lab"

        # 34 OS
        elif subjects == "Operating Systems" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 35 Embedded
        elif subjects == "Embedded System Design" :
            Result = "Semister6 : Embedded System Design Laboratory"

        # 36 AnalogLab
        elif subjects == "Analog and Digital Electronics Lab" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 37 Language Elective III
        elif subjects == "Language Elective Course III" :
            Result = "Language Elective Course IV"

        # 38 Database
        elif subjects == "Database Systems" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 39 NetworkLab
        elif subjects == "Computer Networks Lab" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 40 EmbeddedLab
        elif subjects == "Embedded System Design Laboratory" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 41 Language Elective IV
        elif subjects == "Language Elective Course IV" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 42 Computer Eng. Elective Course I
        elif subjects == "Computer Eng. Elective Course I" :
            Result = "Computer Eng. Elective Course II"

        # 43 Computer Eng. Elective Course II
        elif subjects == "Computer Eng. Elective Course II" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 44 Humanities Elective Course I
        elif subjects == "Humanities Elective Course I" :
            Result = "Humanities Elective Course II"

        # 45 ProjectI
        elif subjects == "Project I" :
            Result = "Semister8 : Project II"

        # 46 Free Elective Course I
        elif subjects == "Free Elective Course I" :
            Result = "Free Elective Course I"

        # 47 Humanities Elective Course II
        elif subjects == "Humanities Elective Course II" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 48 Computer Eng. Elective Course III
        elif subjects == "Computer Eng. Elective Course III" :
            Result = "Computer Eng. Elective Course IV"

        # 49 Computer Eng. Elective Course IV
        elif subjects == "Computer Eng. Elective Course IV" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 50 ProjectII
        elif subjects == "Project II" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 51 Computer Eng. Seminar
        elif subjects == "Computer Eng. Seminar" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 52 Free Elective Course II
        elif subjects == "Free Elective Course II" :
            Result = "The subject hasn't other subjects to connect the flow"

        # 53 Science and Maths Elective III
        elif subjects == "Science and Maths Elective III" :
            Result = "The subject hasn't other subjects to connect the flow"

        # Other
        else :
            # ถ้าวิชานั้นไม่มีใน Flow ให้ Result เป็น The subject isn't in the flow
            Result = "The subject isn't in the flow"

    # ให้ render หน้า flow.html ออกมา โดย render วิชาและ Result ที่เป็นตัวต่อของวิชานั้น ๆ ออกมาด้วย ตามที่ได้กำหนดไว้ใน flow.html
    return render(request, 'flow.html',{'subjects':subjects, 'Result':Result})

# รวมทุกวิชาใน flow โดยเรียงตามเทอมในรูป flow
def listOfSubject(request) :
    # term 1
    listSemister1 = """ Programming Fundamental<br />
            Engineering Mathematics I<br />
            Computer Engineering Exploration<br />
            Physics I<br />
            Physics Laboratory I<br />
            Language Elective Course I<br />
            Physical Education Elective Course I<br />
            Social Sciences Elective Course<br />
            Introduction to Engineer<br />"""

    # term 2
    listSemister2 = """Electric Circuit Theory<br />
            Electric Circuit Lab<br />
            Algorithms and Data Structure<br />
            Work Ethics<br />
            Engineering Mathematics II<br />
            Physics II<br />
            Physics Laboratory II<br />
            Language Elective Course II<br />
            Physical Education Elective Course II<br />"""

    # term 3
    listSemister3 = """Statistics for Computer Engineer<br />
            Introduction to Signals and System<br />
            Logic Design of Digital System<br />
            Digital System Design Laboratory<br />
            Software Development Practice I<br />
            Discrete Mathematics<br />
            Science and Maths Elective I<br />"""

    # term 4
    listSemister4 = """Software Development Practice II<br />
            Computer Networks I<br />
            Computer Organization<br />
            Ubiquitous Computing<br />
            Analog and Digital Electronics<br />
            Science and Maths Elective II<br />"""

    # term 5
    listSemister5 = """Software Engineering<br />
            Computer Networks II<br />
            Operating Systems<br />
            Embedded System Design<br />
            Analog and Digital Electronics Lab<br />
            Language Elective Course III<br />"""

    # term 6
    listSemister6 = """Database Systems<br />
            Computer Networks Lab<br />
            Embedded System Design Laboratory<br />
            Language Elective Course IV<br />
            Computer Eng. Elective Course I<br />
            Computer Eng. Elective Course II<br />
            Humanities Elective Course I<br />"""

    # term 7
    listSemister7 = """Project I<br />
            Free Elective Course I<br />
            Humanities Elective Course II<br />
            Computer Eng. Elective Course III<br />
            Computer Eng. Elective Course IV<br />"""

    # term 8
    listSemister8 = """Project II<br />
            Computer Eng. Seminar<br />
            Free Elective Course II<br />
            Science and Maths Elective III"""

    # render หน้า subject.html ออกมา เรียงตามเทอมนั้น ๆ 
    return render(request, 'subject.html', {'semister1':listSemister1,'semister2':listSemister2,'semister3':listSemister3,'semister4':listSemister4,'semister5':listSemister5,'semister6':listSemister6,'semister7':listSemister7,'semister8':listSemister8})

def Graph(request):
    countunit = 0
    GPAX = 0
    dataterm_1 = Term1.objects.all()
    dataterm_2 = Term2.objects.all()
    dataterm_3 = Term3.objects.all()
    dataterm_4 = Term4.objects.all()
    dataterm_5 = Term5.objects.all()
    dataterm_6 = Term6.objects.all()
    dataterm_7 = Term7.objects.all()
    dataterm_8 = Term8.objects.all()
    dataGPA = GPA.objects.all()
    countunit = 0
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    for i in dataGPA:
        GPAX = float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4) + float(i.GPA_5) + float(i.GPA_6) + float(i.GPA_7) + float(i.GPA_8)
    if GPAX > 0.0:
        for unit in dataGPA:
            if unit.GPA_1 != "0" :
                countunit+=1
            if unit.GPA_2 != "0" :
                countunit+=1
            if unit.GPA_3 != "0" :
                countunit+=1
            if unit.GPA_4 != "0" :
                countunit+=1
            if unit.GPA_5 != "0" :
                countunit+=1
            if unit.GPA_6 != "0" :
                countunit+=1
            if unit.GPA_7 != "0" :
                countunit+=1
            if unit.GPA_8 != "0" :
                countunit+=1
    else:
        countunit+=1
    resGPAX = float(GPAX) / float(countunit)
    newGPAX = '%.2f' % resGPAX
    return render(request, 'Graph.html', {'dataterm1': dataterm_1, 'dataterm2': dataterm_2, 'dataterm3': dataterm_3,
                                          'dataterm4': dataterm_4, 'dataterm5': dataterm_5, 'dataterm6': dataterm_6,
                                          'dataterm7': dataterm_7, 'dataterm8': dataterm_8, 'GPARES': dataGPA,
                                          'res_GPAX': newGPAX})
def Result(request):
    dataGPA = GPA.objects.all()
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    dataterm_1 = Term1.objects.all()
    dataterm_2 = Term2.objects.all()
    dataGPA = GPA.objects.all()
    return render(request, 'Result.html',{'dataterm1':dataterm_1,'dataterm2':dataterm_2,'GPARES':dataGPA})
def firstTerm(request):
    dataGPA = GPA.objects.all()
    dataterm_1 = Term1.objects.all()
    countunit = 0
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    for i in dataGPA:
        GPAX = float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4) + float(i.GPA_5) + float(i.GPA_6) + float(i.GPA_7) + float(i.GPA_8)
    if GPAX > 0.0:
        for unit in dataGPA:
            if unit.GPA_1 != "0" :
                countunit+=1
            if unit.GPA_2 != "0" :
                countunit+=1
            if unit.GPA_3 != "0" :
                countunit+=1
            if unit.GPA_4 != "0" :
                countunit+=1
            if unit.GPA_5 != "0" :
                countunit+=1
            if unit.GPA_6 != "0" :
                countunit+=1
            if unit.GPA_7 != "0" :
                countunit+=1
            if unit.GPA_8 != "0" :
                countunit+=1
    else:
        countunit+=1
    resGPAX = float(GPAX) / float(countunit)
    newGPAX = '%.2f' % resGPAX
    return render(request, 'firstTerm.html', {'dataterm1':dataterm_1,'GPARES':dataGPA,'res_GPAX': newGPAX})

def secondTerm(request):
    dataGPA = GPA.objects.all()
    dataterm_2 = Term2.objects.all()
    countunit = 0
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    for i in dataGPA:
        GPAX = float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4) + float(i.GPA_5) + float(i.GPA_6) + float(i.GPA_7) + float(i.GPA_8)
    if GPAX > 0.0:
        for unit in dataGPA:
            if unit.GPA_1 != "0" :
                countunit+=1
            if unit.GPA_2 != "0" :
                countunit+=1
            if unit.GPA_3 != "0" :
                countunit+=1
            if unit.GPA_4 != "0" :
                countunit+=1
            if unit.GPA_5 != "0" :
                countunit+=1
            if unit.GPA_6 != "0" :
                countunit+=1
            if unit.GPA_7 != "0" :
                countunit+=1
            if unit.GPA_8 != "0" :
                countunit+=1
    else:
        countunit+=1
    resGPAX = float(GPAX) / float(countunit)
    newGPAX = '%.2f' % resGPAX
    return render(request, 'secondTerm.html', {'dataterm2':dataterm_2,'GPARES':dataGPA,'res_GPAX': newGPAX})

def thirdTerm(request):
    dataGPA = GPA.objects.all()
    dataterm_3 = Term3.objects.all()
    countunit = 0
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    for i in dataGPA:
        GPAX = float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4) + float(i.GPA_5) + float(i.GPA_6) + float(i.GPA_7) + float(i.GPA_8)
    if GPAX > 0.0:
        for unit in dataGPA:
            if unit.GPA_1 != "0" :
                countunit+=1
            if unit.GPA_2 != "0" :
                countunit+=1
            if unit.GPA_3 != "0" :
                countunit+=1
            if unit.GPA_4 != "0" :
                countunit+=1
            if unit.GPA_5 != "0" :
                countunit+=1
            if unit.GPA_6 != "0" :
                countunit+=1
            if unit.GPA_7 != "0" :
                countunit+=1
            if unit.GPA_8 != "0" :
                countunit+=1
    else:
        countunit+=1
    resGPAX = float(GPAX) / float(countunit)
    newGPAX = '%.2f' % resGPAX
    return render(request, 'thirdTerm.html', {'dataterm3':dataterm_3,'GPARES':dataGPA,'res_GPAX': newGPAX})

def fourthTerm(request):
    dataGPA = GPA.objects.all()
    dataterm_4 = Term4.objects.all()
    countunit = 0
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    for i in dataGPA:
        GPAX = float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4) + float(i.GPA_5) + float(i.GPA_6) + float(i.GPA_7) + float(i.GPA_8)
    if GPAX > 0.0:
        for unit in dataGPA:
            if unit.GPA_1 != "0" :
                countunit+=1
            if unit.GPA_2 != "0" :
                countunit+=1
            if unit.GPA_3 != "0" :
                countunit+=1
            if unit.GPA_4 != "0" :
                countunit+=1
            if unit.GPA_5 != "0" :
                countunit+=1
            if unit.GPA_6 != "0" :
                countunit+=1
            if unit.GPA_7 != "0" :
                countunit+=1
            if unit.GPA_8 != "0" :
                countunit+=1
    else:
        countunit+=1
    resGPAX = float(GPAX) / float(countunit)
    newGPAX = '%.2f' % resGPAX
    return render(request, 'fourthTerm.html', {'dataterm4':dataterm_4,'GPARES':dataGPA,'res_GPAX': newGPAX})

def fifthTerm(request):
    dataGPA = GPA.objects.all()
    dataterm_5 = Term5.objects.all()
    countunit = 0
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    for i in dataGPA:
        GPAX = float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4) + float(i.GPA_5) + float(i.GPA_6) + float(i.GPA_7) + float(i.GPA_8)
    if GPAX > 0.0:
        for unit in dataGPA:
            if unit.GPA_1 != "0" :
                countunit+=1
            if unit.GPA_2 != "0" :
                countunit+=1
            if unit.GPA_3 != "0" :
                countunit+=1
            if unit.GPA_4 != "0" :
                countunit+=1
            if unit.GPA_5 != "0" :
                countunit+=1
            if unit.GPA_6 != "0" :
                countunit+=1
            if unit.GPA_7 != "0" :
                countunit+=1
            if unit.GPA_8 != "0" :
                countunit+=1
    else:
        countunit+=1
    resGPAX = float(GPAX) / float(countunit)
    newGPAX = '%.2f' % resGPAX
    return render(request, 'fifthTerm.html', {'dataterm5':dataterm_5,'GPARES':dataGPA,'res_GPAX': newGPAX})

def sixthTerm(request):
    dataGPA = GPA.objects.all()
    dataterm_6 = Term6.objects.all()
    countunit = 0
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    for i in dataGPA:
        GPAX = float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4) + float(i.GPA_5) + float(i.GPA_6) + float(i.GPA_7) + float(i.GPA_8)
    if GPAX > 0.0:
        for unit in dataGPA:
            if unit.GPA_1 != "0" :
                countunit+=1
            if unit.GPA_2 != "0" :
                countunit+=1
            if unit.GPA_3 != "0" :
                countunit+=1
            if unit.GPA_4 != "0" :
                countunit+=1
            if unit.GPA_5 != "0" :
                countunit+=1
            if unit.GPA_6 != "0" :
                countunit+=1
            if unit.GPA_7 != "0" :
                countunit+=1
            if unit.GPA_8 != "0" :
                countunit+=1
    else:
        countunit+=1
    resGPAX = float(GPAX) / float(countunit)
    newGPAX = '%.2f' % resGPAX
    return render(request, 'sixthTerm.html', {'dataterm6':dataterm_6,'GPARES':dataGPA,'res_GPAX': newGPAX})

def seventhTerm(request):
    dataterm_7 = Term7.objects.all()
    dataGPA = GPA.objects.all()
    countunit = 0
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    for i in dataGPA:
        GPAX = float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4) + float(i.GPA_5) + float(i.GPA_6) + float(i.GPA_7) + float(i.GPA_8)
    if GPAX > 0.0:
        for unit in dataGPA:
            if unit.GPA_1 != "0" :
                countunit+=1
            if unit.GPA_2 != "0" :
                countunit+=1
            if unit.GPA_3 != "0" :
                countunit+=1
            if unit.GPA_4 != "0" :
                countunit+=1
            if unit.GPA_5 != "0" :
                countunit+=1
            if unit.GPA_6 != "0" :
                countunit+=1
            if unit.GPA_7 != "0" :
                countunit+=1
            if unit.GPA_8 != "0" :
                countunit+=1
    else:
        countunit+=1
    resGPAX = float(GPAX) / float(countunit)
    newGPAX = '%.2f' % resGPAX
    return render(request, 'seventhTerm.html', {'dataterm7':dataterm_7,'GPARES':dataGPA,'res_GPAX': newGPAX})

def eightTerm(request):
    dataGPA = GPA.objects.all()
    dataterm_8 = Term8.objects.all()
    countunit = 0
    if len(dataGPA) == 0:
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    for i in dataGPA:
        GPAX = float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4) + float(i.GPA_5) + float(i.GPA_6) + float(i.GPA_7) + float(i.GPA_8)
    if GPAX > 0.0:
        for unit in dataGPA:
            if unit.GPA_1 != "0" :
                countunit+=1
            if unit.GPA_2 != "0" :
                countunit+=1
            if unit.GPA_3 != "0" :
                countunit+=1
            if unit.GPA_4 != "0" :
                countunit+=1
            if unit.GPA_5 != "0" :
                countunit+=1
            if unit.GPA_6 != "0" :
                countunit+=1
            if unit.GPA_7 != "0" :
                countunit+=1
            if unit.GPA_8 != "0" :
                countunit+=1
    else:
        countunit+=1
    resGPAX = float(GPAX) / float(countunit)
    newGPAX = '%.2f' % resGPAX
    return render(request, 'eightTerm.html', {'dataterm8':dataterm_8,'GPARES':dataGPA,'res_GPAX': newGPAX})

# แสดงรูป flow
def picFlow(request):

    # render หน้า picFlow.html เพื่อแสดงรูป Flow
    return render(request, 'picFlow.html')

# แสดงหน้า about
def about(request):

    # render หน้า about.html
    return render(request, 'about.html')

# แสดงหน้า help
def help(request):

    # render หน้า help.html
    return render(request, 'help.html')
