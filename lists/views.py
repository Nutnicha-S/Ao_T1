from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Semister,GPA,GradeGPAX
from lists.models import Userinfo

# แสดงหน้าหลักของ GradeGuide
def home_page(request):
    # render หน้า home.html
    return render(request, 'home.html')

# count user ที่มา register
def count_user_register(request):
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
    return render(request, 'registration/signup.html', {'form': form})

# calculate the grade
def grade_calculator(request):
    # เก็บ Plese check your infromation before saving. ไว้ใน not_input
    not_input = "Plese check your infromation before saving."

    # เก็บ Please select term before saving grade ไว้ใน message
    message = 'Please select term before saving grade'

    # ให้แต่ละวิชาคูณจำนวนหน่วยกิตและเกรดที่ได้เก็บไว้ใน sub_1-9 ตามลำดับ
    sub_1 = ( float(request.POST.get('subject1Unit'))
            * float(request.POST.get('subject1Grade')) )

    sub_2 = ( float(request.POST.get('subject2Unit'))
            * float(request.POST.get('subject2Grade')) )

    sub_3 = ( float(request.POST.get('subject3Unit'))
            * float(request.POST.get('subject3Grade')) )

    sub_4 = ( float(request.POST.get('subject4Unit'))
            * float(request.POST.get('subject4Grade')) )

    sub_5 = ( float(request.POST.get('subject5Unit'))
            * float(request.POST.get('subject5Grade')) )

    sub_6 = ( float(request.POST.get('subject6Unit'))
            * float(request.POST.get('subject6Grade')) )

    sub_7 = ( float(request.POST.get('subject7Unit'))
            * float(request.POST.get('subject7Grade')) )

    sub_8 = ( float(request.POST.get('subject8Unit'))
            * float(request.POST.get('subject8Grade')) )

    sub_9 = ( float(request.POST.get('subject9Unit'))
            * float(request.POST.get('subject9Grade')) )

    # เก็บผลบวกของหน่วยกิตทุกวิชาไว้ใน sum_unit
    sum_unit = ( float(request.POST.get('subject1Unit'))
               + float(request.POST.get('subject2Unit'))
               + float(request.POST.get('subject3Unit'))
               + float(request.POST.get('subject4Unit'))
               + float(request.POST.get('subject5Unit'))
               + float(request.POST.get('subject6Unit'))
               + float(request.POST.get('subject7Unit'))
               + float(request.POST.get('subject8Unit'))
               + float(request.POST.get('subject9Unit')) )
            
    # นำ sub_1 บวกไปจนถึง sub_9 เก็บไว้ที่ sum_sub
    sum_sub = (sub_1 + sub_2 + sub_3 + sub_4 + sub_5 
               + sub_6 + sub_7 + sub_8 + sub_9)

    # check ตัวส่วนว่าเป็น 0 หรือไม่
    if sum_unit == 0 :
        # ถ้าเป็น 0 ให้ แสดง not_input
        return render(request, 'home.html', {'notinput': not_input})
    # ถ้าไม่เป็น 0 
    else :
        # นำ sum_sub หารด้วย sum_unit เก็บไว้ใน result
        result = sum_sub / sum_unit
        # นำ result มาทำให้เหลือทศนิยม 2 ตำแหน่ง 
        # ได้เกรดของเทอมนั้น ๆ
        grade_result = '%.2f' % result

    # ถ้าวิชาในทุกเทอมน้อยกว่าหรือเท่ากับ 80
    if len(Term1.objects.all()) <= 80:

        # ------------------------------------------------------ Term 1 -------------------------------------------------------------
        # ถ้า value ของ subjectTerm มีค่าเท่ากับ 1 (ถ้าเลือกเทอม 1)
        if request.POST.get('subjectTerm') == "1":
        
            # ถ้าความยาวของวิชาในเทอม 1 มีค่าเท่ากับ 0
            if len(Term1.objects.all()) == 0 :
                # ให้สร้างช่องใส่ ชื่อวิชา หน่วยกิต เกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term1.objects.create(subject =request.POST['subject1name'],
                                     unit=request.POST['subject1Unit'],
                                     Grade=request.POST['subject1Grade'],
                                     GPA=res)

                Term1.objects.create(subject=request.POST['subject2name'],
                                     unit=request.POST['subject2Unit'],
                                     Grade=request.POST['subject2Grade'],
                                     GPA=res)

                Term1.objects.create(subject =request.POST['subject3name'],
                                     unit=request.POST['subject3Unit'],
                                     Grade=request.POST['subject3Grade'],
                                     GPA=res)

                Term1.objects.create(subject =request.POST['subject4name'],
                                     unit=request.POST['subject4Unit'],
                                     Grade=request.POST['subject4Grade'],
                                     GPA=res)

                Term1.objects.create(subject =request.POST['subject5name'],
                                     unit=request.POST['subject5Unit'],
                                     Grade=request.POST['subject5Grade'],
                                     GPA=res)

                Term1.objects.create(subject=request.POST['subject6name'],
                                     unit=request.POST['subject6Unit'],
                                     Grade=request.POST['subject6Grade'],
                                     GPA=res)

                Term1.objects.create(subject =request.POST['subject7name'],
                                     unit=request.POST['subject7Unit'],
                                     Grade=request.POST['subject7Grade'],
                                     GPA=res)

                Term1.objects.create(subject=request.POST['subject8name'],
                                     unit=request.POST['subject8Unit'],
                                     Grade=request.POST['subject8Grade'],
                                     GPA=res)

                Term1.objects.create(subject=request.POST['subject9name'],
                                     unit=request.POST['subject9Unit'],
                                     Grade=request.POST['subject9Grade'],
                                     GPA=res)

                # update GPA term 1 
                GPA.objects.filter(pk=1).update(GPA_1=res)

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

            # other
            else:
                # update ช่องใส่ ชื่อวิชา หน่วยกิต เกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term1.objects.filter(pk=1).update(subject =request.POST['subject1name'],
                                                  unit=request.POST['subject1Unit'], 
                                                  Grade=request.POST['subject1Grade'],
                                                  GPA=res)

                Term1.objects.filter(pk=2).update(subject =request.POST['subject2name'],
                                                  unit=request.POST['subject2Unit'],
                                                  Grade=request.POST['subject2Grade'],
                                                  GPA=res)

                Term1.objects.filter(pk=3).update(subject =request.POST['subject3name'], 
                                                  unit=request.POST['subject3Unit'],
                                                  Grade=request.POST['subject3Grade'],
                                                  GPA=res)

                Term1.objects.filter(pk=4).update(subject =request.POST['subject4name'], 
                                                  unit=request.POST['subject4Unit'],
                                                  Grade=request.POST['subject4Grade'],
                                                  GPA=res)

                Term1.objects.filter(pk=5).update(subject =request.POST['subject5name'],
                                                  unit=request.POST['subject5Unit'],
                                                  Grade=request.POST['subject5Grade'],
                                                  GPA=res)

                Term1.objects.filter(pk=6).update(subject =request.POST['subject6name'],
                                                  unit=request.POST['subject6Unit'],
                                                  Grade=request.POST['subject6Grade'],
                                                  GPA=res)

                Term1.objects.filter(pk=7).update(subject =request.POST['subject7name'],
                                                  unit=request.POST['subject7Unit'],
                                                  Grade=request.POST['subject7Grade'],
                                                  GPA=res)

                Term1.objects.filter(pk=8).update(subject =request.POST['subject8name'],
                                                  unit=request.POST['subject8Unit'],
                                                  Grade=request.POST['subject8Grade'],
                                                  GPA=res)

                Term1.objects.filter(pk=9).update(subject =request.POST['subject9name'],
                                                  unit=request.POST['subject9Unit'],
                                                  Grade=request.POST['subject9Grade'],
                                                  GPA=res)

                # update GPA term 1 
                GPA.objects.filter(pk=1).update(GPA_1=res)

                # เก็บ ชื่อวิชา หน่วยกิต เกรด ของแต่ละวิชาไว้ใน data
                data = Term1.objects.all()

                # ให้ res หรือ GPA ที่คำนวณไว้ก่อนหน้านี้ เก็บไว้ใน term1.GPA
                term_1.GPA = res

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

        # ------------------------------------------------------ Term 2 -------------------------------------------------------------
        # ถ้า value ของ subjectTerm มีค่าเท่ากับ 2 (ถ้าเลือกเทอม 2)
        if request.POST.get('subjectTerm') == "2":

            # ถ้าความยาวของวิชาในเทอม 2 มีค่าเท่ากับ 0
            if len(Term2.objects.all()) == 0 :
                # ให้สร้างช่องใส่ ชื่อวิชา หน่วยกิต เกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term2.objects.create(subject =request.POST['subject1name'],
                                     unit=request.POST['subject1Unit'],
                                     Grade=request.POST['subject1Grade'],
                                     GPA=res)

                Term2.objects.create(subject=request.POST['subject2name'],
                                     unit=request.POST['subject2Unit'],
                                     Grade=request.POST['subject2Grade'],
                                     GPA=res)

                Term2.objects.create(subject =request.POST['subject3name'],
                                     unit=request.POST['subject3Unit'],
                                     Grade=request.POST['subject3Grade'],
                                     GPA=res)

                Term2.objects.create(subject =request.POST['subject4name'],
                                     unit=request.POST['subject4Unit'],
                                     Grade=request.POST['subject4Grade'],
                                     GPA=res)

                Term2.objects.create(subject =request.POST['subject5name'],
                                     unit=request.POST['subject5Unit'],
                                     Grade=request.POST['subject5Grade'],
                                     GPA=res)

                Term2.objects.create(subject=request.POST['subject6name'],
                                     unit=request.POST['subject6Unit'],
                                     Grade=request.POST['subject6Grade'],
                                     GPA=res)

                Term2.objects.create(subject =request.POST['subject7name'],
                                     unit=request.POST['subject7Unit'],
                                     Grade=request.POST['subject7Grade'],
                                     GPA=res)

                Term2.objects.create(subject=request.POST['subject8name'],
                                     unit=request.POST['subject8Unit'],
                                     Grade=request.POST['subject8Grade'],
                                     GPA=res)

                Term2.objects.create(subject=request.POST['subject9name'],
                                     unit=request.POST['subject9Unit'],
                                     Grade=request.POST['subject9Grade'],
                                     GPA=res)

                # update GPA term 2
                GPA.objects.filter(pk=1).update(GPA_2=res)

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

            # other
            else:
                # update ช่องใส่ ชื่อวิชา หน่วยกิต เกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term2.objects.filter(pk=1).update(subject =request.POST['subject1name'],
                                                  unit=request.POST['subject1Unit'], 
                                                  Grade=request.POST['subject1Grade'],
                                                  GPA=res)

                Term2.objects.filter(pk=2).update(subject =request.POST['subject2name'],
                                                  unit=request.POST['subject2Unit'],
                                                  Grade=request.POST['subject2Grade'],
                                                  GPA=res)

                Term2.objects.filter(pk=3).update(subject =request.POST['subject3name'], 
                                                  unit=request.POST['subject3Unit'],
                                                  Grade=request.POST['subject3Grade'],
                                                  GPA=res)

                Term2.objects.filter(pk=4).update(subject =request.POST['subject4name'], 
                                                  unit=request.POST['subject4Unit'],
                                                  Grade=request.POST['subject4Grade'],
                                                  GPA=res)

                Term2.objects.filter(pk=5).update(subject =request.POST['subject5name'],
                                                  unit=request.POST['subject5Unit'],
                                                  Grade=request.POST['subject5Grade'],
                                                  GPA=res)

                Term2.objects.filter(pk=6).update(subject =request.POST['subject6name'],
                                                  unit=request.POST['subject6Unit'],
                                                  Grade=request.POST['subject6Grade'],
                                                  GPA=res)

                Term2.objects.filter(pk=7).update(subject =request.POST['subject7name'],
                                                  unit=request.POST['subject7Unit'],
                                                  Grade=request.POST['subject7Grade'],
                                                  GPA=res)

                Term2.objects.filter(pk=8).update(subject =request.POST['subject8name'],
                                                  unit=request.POST['subject8Unit'],
                                                  Grade=request.POST['subject8Grade'],
                                                  GPA=res)

                Term2.objects.filter(pk=9).update(subject =request.POST['subject9name'],
                                                  unit=request.POST['subject9Unit'],
                                                  Grade=request.POST['subject9Grade'],
                                                  GPA=res)

                # update GPA term 2
                GPA.objects.filter(pk=1).update(GPA_2=res)

                # ให้ res หรือ GPA ที่คำนวณไว้ก่อนหน้านี้ เก็บไว้ใน term2.GPA
                term_2.GPA = res

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

        # ------------------------------------------------------ Term 3 -------------------------------------------------------------
        # ถ้า value ของ subjectTerm มีค่าเท่ากับ 3 (ถ้าเลือกเทอม 3)
        if request.POST.get('subjectTerm') == "3":

            # ถ้าความยาวของวิชาในเทอม 3 มีค่าเท่ากับ 0
            if len(Term3.objects.all()) == 0 :
                # ให้สร้างช่องใส่ ชื่อวิชา หน่วยกิต เกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term3.objects.create(subject =request.POST['subject1name'],
                                     unit=request.POST['subject1Unit'],
                                     Grade=request.POST['subject1Grade'],
                                     GPA=res)

                Term3.objects.create(subject=request.POST['subject2name'],
                                     unit=request.POST['subject2Unit'],
                                     Grade=request.POST['subject2Grade'],
                                     GPA=res)

                Term3.objects.create(subject =request.POST['subject3name'],
                                     unit=request.POST['subject3Unit'],
                                     Grade=request.POST['subject3Grade'],
                                     GPA=res)

                Term3.objects.create(subject =request.POST['subject4name'],
                                     unit=request.POST['subject4Unit'],
                                     Grade=request.POST['subject4Grade'],
                                     GPA=res)

                Term3.objects.create(subject =request.POST['subject5name'],
                                     unit=request.POST['subject5Unit'],
                                     Grade=request.POST['subject5Grade'],
                                     GPA=res)

                Term3.objects.create(subject=request.POST['subject6name'],
                                     unit=request.POST['subject6Unit'],
                                     Grade=request.POST['subject6Grade'],
                                     GPA=res)

                Term3.objects.create(subject =request.POST['subject7name'],
                                     unit=request.POST['subject7Unit'],
                                     Grade=request.POST['subject7Grade'],
                                     GPA=res)

                Term3.objects.create(subject=request.POST['subject8name'],
                                     unit=request.POST['subject8Unit'],
                                     Grade=request.POST['subject8Grade'],
                                     GPA=res)

                Term3.objects.create(subject=request.POST['subject9name'],
                                     unit=request.POST['subject9Unit'],
                                     Grade=request.POST['subject9Grade'],
                                     GPA=res)

                # update GPA term 3
                GPA.objects.filter(pk=1).update(GPA_3=res)

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

            # other
            else:
                # update ช่องใส่ ชื่อวิชา หน่วยกิต เกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term3.objects.filter(pk=1).update(subject =request.POST['subject1name'],
                                                  unit=request.POST['subject1Unit'], 
                                                  Grade=request.POST['subject1Grade'],
                                                  GPA=res)

                Term3.objects.filter(pk=2).update(subject =request.POST['subject2name'],
                                                  unit=request.POST['subject2Unit'],
                                                  Grade=request.POST['subject2Grade'],
                                                  GPA=res)

                Term3.objects.filter(pk=3).update(subject =request.POST['subject3name'], 
                                                  unit=request.POST['subject3Unit'],
                                                  Grade=request.POST['subject3Grade'],
                                                  GPA=res)

                Term3.objects.filter(pk=4).update(subject =request.POST['subject4name'], 
                                                  unit=request.POST['subject4Unit'],
                                                  Grade=request.POST['subject4Grade'],
                                                  GPA=res)

                Term3.objects.filter(pk=5).update(subject =request.POST['subject5name'],
                                                  unit=request.POST['subject5Unit'],
                                                  Grade=request.POST['subject5Grade'],
                                                  GPA=res)

                Term3.objects.filter(pk=6).update(subject =request.POST['subject6name'],
                                                  unit=request.POST['subject6Unit'],
                                                  Grade=request.POST['subject6Grade'],
                                                  GPA=res)

                Term3.objects.filter(pk=7).update(subject =request.POST['subject7name'],
                                                  unit=request.POST['subject7Unit'],
                                                  Grade=request.POST['subject7Grade'],
                                                  GPA=res)

                Term3.objects.filter(pk=8).update(subject =request.POST['subject8name'],
                                                  unit=request.POST['subject8Unit'],
                                                  Grade=request.POST['subject8Grade'],
                                                  GPA=res)

                Term3.objects.filter(pk=9).update(subject =request.POST['subject9name'],
                                                  unit=request.POST['subject9Unit'],
                                                  Grade=request.POST['subject9Grade'],
                                                  GPA=res)

                # update GPA term 3
                GPA.objects.filter(pk=1).update(GPA_3=res)

                # ให้ res หรือ GPA ที่คำนวณไว้ก่อนหน้านี้ เก็บไว้ใน term3.GPA
                term3.GPA = res

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

        # ------------------------------------------------------ Term 4 -------------------------------------------------------------
        # ถ้า value ของ subjectTerm มีค่าเท่ากับ 4 (ถ้าเลือกเทอม 4)
        if request.POST.get('subjectTerm') == "4":

            # ถ้าความยาวของวิชาในเทอม 4 มีค่าเท่ากับ 0
            if len(Term4.objects.all()) == 0 :
                # ให้สร้างช่องใส่ ชื่อวิชา หน่วยกิต เกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term4.objects.create(subject =request.POST['subject1name'],
                                     unit=request.POST['subject1Unit'],
                                     Grade=request.POST['subject1Grade'],
                                     GPA=res)

                Term4.objects.create(subject=request.POST['subject2name'],
                                     unit=request.POST['subject2Unit'],
                                     Grade=request.POST['subject2Grade'],
                                     GPA=res)

                Term4.objects.create(subject =request.POST['subject3name'],
                                     unit=request.POST['subject3Unit'],
                                     Grade=request.POST['subject3Grade'],
                                     GPA=res)

                Term4.objects.create(subject =request.POST['subject4name'],
                                     unit=request.POST['subject4Unit'],
                                     Grade=request.POST['subject4Grade'],
                                     GPA=res)

                Term4.objects.create(subject =request.POST['subject5name'],
                                     unit=request.POST['subject5Unit'],
                                     Grade=request.POST['subject5Grade'],
                                     GPA=res)

                Term4.objects.create(subject=request.POST['subject6name'],
                                     unit=request.POST['subject6Unit'],
                                     Grade=request.POST['subject6Grade'],
                                     GPA=res)

                Term4.objects.create(subject =request.POST['subject7name'],
                                     unit=request.POST['subject7Unit'],
                                     Grade=request.POST['subject7Grade'],
                                     GPA=res)

                Term4.objects.create(subject=request.POST['subject8name'],
                                     unit=request.POST['subject8Unit'],
                                     Grade=request.POST['subject8Grade'],
                                     GPA=res)

                Term4.objects.create(subject=request.POST['subject9name'],
                                     unit=request.POST['subject9Unit'],
                                     Grade=request.POST['subject9Grade'],
                                     GPA=res)

                # update GPA term 4
                GPA.objects.filter(pk=1).update(GPA_4=res)

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

            # other
            else:
                # update ช่องใส่ ชื่อวิชา หน่วยกิต เกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term4.objects.filter(pk=1).update(subject =request.POST['subject1name'],
                                                  unit=request.POST['subject1Unit'], 
                                                  Grade=request.POST['subject1Grade'],
                                                  GPA=res)

                Term4.objects.filter(pk=2).update(subject =request.POST['subject2name'],
                                                  unit=request.POST['subject2Unit'],
                                                  Grade=request.POST['subject2Grade'],
                                                  GPA=res)

                Term4.objects.filter(pk=3).update(subject =request.POST['subject3name'], 
                                                  unit=request.POST['subject3Unit'],
                                                  Grade=request.POST['subject3Grade'],
                                                  GPA=res)

                Term4.objects.filter(pk=4).update(subject =request.POST['subject4name'], 
                                                  unit=request.POST['subject4Unit'],
                                                  Grade=request.POST['subject4Grade'],
                                                  GPA=res)

                Term4.objects.filter(pk=5).update(subject =request.POST['subject5name'],
                                                  unit=request.POST['subject5Unit'],
                                                  Grade=request.POST['subject5Grade'],
                                                  GPA=res)

                Term4.objects.filter(pk=6).update(subject =request.POST['subject6name'],
                                                  unit=request.POST['subject6Unit'],
                                                  Grade=request.POST['subject6Grade'],
                                                  GPA=res)

                Term4.objects.filter(pk=7).update(subject =request.POST['subject7name'],
                                                  unit=request.POST['subject7Unit'],
                                                  Grade=request.POST['subject7Grade'],
                                                  GPA=res)

                Term4.objects.filter(pk=8).update(subject =request.POST['subject8name'],
                                                  unit=request.POST['subject8Unit'],
                                                  Grade=request.POST['subject8Grade'],
                                                  GPA=res)

                Term4.objects.filter(pk=9).update(subject =request.POST['subject9name'],
                                                  unit=request.POST['subject9Unit'],
                                                  Grade=request.POST['subject9Grade'],
                                                  GPA=res)

                # update GPA term 4
                GPA.objects.filter(pk=1).update(GPA_4=res)

                # ให้ res หรือ GPA ที่คำนวณไว้ก่อนหน้านี้ เก็บไว้ใน term4.GPA
                term4.GPA = res

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

        # ------------------------------------------------------ Term 5 -------------------------------------------------------------
        # ถ้า value ของ subjectTerm มีค่าเท่ากับ 5 (ถ้าเลือกเทอม 5)                
        if request.POST.get('subjectTerm') == "5":

            # ถ้าความยาวของวิชาในเทอม 5 มีค่าเท่ากับ 0
            if len(Term5.objects.all()) == 0 :
                # ให้สร้างช่องใส่ ชื่อวิชา หน่วยกิต เกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term5.objects.create(subject =request.POST['subject1name'],
                                     unit=request.POST['subject1Unit'],
                                     Grade=request.POST['subject1Grade'],
                                     GPA=res)

                Term5.objects.create(subject=request.POST['subject2name'],
                                     unit=request.POST['subject2Unit'],
                                     Grade=request.POST['subject2Grade'],
                                     GPA=res)

                Term5.objects.create(subject =request.POST['subject3name'],
                                     unit=request.POST['subject3Unit'],
                                     Grade=request.POST['subject3Grade'],
                                     GPA=res)

                Term5.objects.create(subject =request.POST['subject4name'],
                                     unit=request.POST['subject4Unit'],
                                     Grade=request.POST['subject4Grade'],
                                     GPA=res)

                Term5.objects.create(subject =request.POST['subject5name'],
                                     unit=request.POST['subject5Unit'],
                                     Grade=request.POST['subject5Grade'],
                                     GPA=res)

                Term5.objects.create(subject=request.POST['subject6name'],
                                     unit=request.POST['subject6Unit'],
                                     Grade=request.POST['subject6Grade'],
                                     GPA=res)

                Term5.objects.create(subject =request.POST['subject7name'],
                                     unit=request.POST['subject7Unit'],
                                     Grade=request.POST['subject7Grade'],
                                     GPA=res)

                Term5.objects.create(subject=request.POST['subject8name'],
                                     unit=request.POST['subject8Unit'],
                                     Grade=request.POST['subject8Grade'],
                                     GPA=res)

                Term5.objects.create(subject=request.POST['subject9name'],
                                     unit=request.POST['subject9Unit'],
                                     Grade=request.POST['subject9Grade'],
                                     GPA=res)

                # update GPA term 5
                GPA.objects.filter(pk=1).update(GPA_5=res)

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

            # other
            else:
                # update ช่องใส่ ชื่อวิชา หน่วยกิต เกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term5.objects.filter(pk=1).update(subject =request.POST['subject1name'],
                                                  unit=request.POST['subject1Unit'], 
                                                  Grade=request.POST['subject1Grade'],
                                                  GPA=res)

                Term5.objects.filter(pk=2).update(subject =request.POST['subject2name'],
                                                  unit=request.POST['subject2Unit'],
                                                  Grade=request.POST['subject2Grade'],
                                                  GPA=res)

                Term5.objects.filter(pk=3).update(subject =request.POST['subject3name'], 
                                                  unit=request.POST['subject3Unit'],
                                                  Grade=request.POST['subject3Grade'],
                                                  GPA=res)

                Term5.objects.filter(pk=4).update(subject =request.POST['subject4name'], 
                                                  unit=request.POST['subject4Unit'],
                                                  Grade=request.POST['subject4Grade'],
                                                  GPA=res)

                Term5.objects.filter(pk=5).update(subject =request.POST['subject5name'],
                                                  unit=request.POST['subject5Unit'],
                                                  Grade=request.POST['subject5Grade'],
                                                  GPA=res)

                Term5.objects.filter(pk=6).update(subject =request.POST['subject6name'],
                                                  unit=request.POST['subject6Unit'],
                                                  Grade=request.POST['subject6Grade'],
                                                  GPA=res)

                Term5.objects.filter(pk=7).update(subject =request.POST['subject7name'],
                                                  unit=request.POST['subject7Unit'],
                                                  Grade=request.POST['subject7Grade'],
                                                  GPA=res)

                Term5.objects.filter(pk=8).update(subject =request.POST['subject8name'],
                                                  unit=request.POST['subject8Unit'],
                                                  Grade=request.POST['subject8Grade'],
                                                  GPA=res)

                Term5.objects.filter(pk=9).update(subject =request.POST['subject9name'],
                                                  unit=request.POST['subject9Unit'],
                                                  Grade=request.POST['subject9Grade'],
                                                  GPA=res)
                
                # update GPA term 5
                GPA.objects.filter(pk=1).update(GPA_5=res)

                # ให้ res หรือ GPA ที่คำนวณไว้ก่อนหน้านี้ เก็บไว้ใน term5.GPA
                term5.GPA = res

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

        # ------------------------------------------------------ Term 6 -------------------------------------------------------------
        # ถ้า value ของ subjectTerm มีค่าเท่ากับ 6 (ถ้าเลือกเทอม 6)   
        if request.POST.get('subjectTerm') == "6":

            # ถ้าความยาวของวิชาในเทอม 6 มีค่าเท่ากับ 0
            if len(Term6.objects.all()) == 0 :
                # ให้สร้างช่องใส่ ชื่อวิชา หน่วยกิต เกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term6.objects.create(subject =request.POST['subject1name'],
                                     unit=request.POST['subject1Unit'],
                                     Grade=request.POST['subject1Grade'],
                                     GPA=res)

                Term6.objects.create(subject=request.POST['subject2name'],
                                     unit=request.POST['subject2Unit'],
                                     Grade=request.POST['subject2Grade'],
                                     GPA=res)

                Term6.objects.create(subject =request.POST['subject3name'],
                                     unit=request.POST['subject3Unit'],
                                     Grade=request.POST['subject3Grade'],
                                     GPA=res)

                Term6.objects.create(subject =request.POST['subject4name'],
                                     unit=request.POST['subject4Unit'],
                                     Grade=request.POST['subject4Grade'],
                                     GPA=res)

                Term6.objects.create(subject =request.POST['subject5name'],
                                     unit=request.POST['subject5Unit'],
                                     Grade=request.POST['subject5Grade'],
                                     GPA=res)

                Term6.objects.create(subject=request.POST['subject6name'],
                                     unit=request.POST['subject6Unit'],
                                     Grade=request.POST['subject6Grade'],
                                     GPA=res)

                Term6.objects.create(subject =request.POST['subject7name'],
                                     unit=request.POST['subject7Unit'],
                                     Grade=request.POST['subject7Grade'],
                                     GPA=res)

                Term6.objects.create(subject=request.POST['subject8name'],
                                     unit=request.POST['subject8Unit'],
                                     Grade=request.POST['subject8Grade'],
                                     GPA=res)

                Term6.objects.create(subject=request.POST['subject9name'],
                                     unit=request.POST['subject9Unit'],
                                     Grade=request.POST['subject9Grade'],
                                     GPA=res)

                # update GPA term 6
                GPA.objects.filter(pk=1).update(GPA_6=res)

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

            # other
            else:
                # update ช่องใส่ ชื่อวิชา หน่วยกิต เกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term6.objects.filter(pk=1).update(subject =request.POST['subject1name'],
                                                  unit=request.POST['subject1Unit'], 
                                                  Grade=request.POST['subject1Grade'],
                                                  GPA=res)

                Term6.objects.filter(pk=2).update(subject =request.POST['subject2name'],
                                                  unit=request.POST['subject2Unit'],
                                                  Grade=request.POST['subject2Grade'],
                                                  GPA=res)

                Term6.objects.filter(pk=3).update(subject =request.POST['subject3name'], 
                                                  unit=request.POST['subject3Unit'],
                                                  Grade=request.POST['subject3Grade'],
                                                  GPA=res)

                Term6.objects.filter(pk=4).update(subject =request.POST['subject4name'], 
                                                  unit=request.POST['subject4Unit'],
                                                  Grade=request.POST['subject4Grade'],
                                                  GPA=res)

                Term6.objects.filter(pk=5).update(subject =request.POST['subject5name'],
                                                  unit=request.POST['subject5Unit'],
                                                  Grade=request.POST['subject5Grade'],
                                                  GPA=res)

                Term6.objects.filter(pk=6).update(subject =request.POST['subject6name'],
                                                  unit=request.POST['subject6Unit'],
                                                  Grade=request.POST['subject6Grade'],
                                                  GPA=res)

                Term6.objects.filter(pk=7).update(subject =request.POST['subject7name'],
                                                  unit=request.POST['subject7Unit'],
                                                  Grade=request.POST['subject7Grade'],
                                                  GPA=res)

                Term6.objects.filter(pk=8).update(subject =request.POST['subject8name'],
                                                  unit=request.POST['subject8Unit'],
                                                  Grade=request.POST['subject8Grade'],
                                                  GPA=res)

                Term6.objects.filter(pk=9).update(subject =request.POST['subject9name'],
                                                  unit=request.POST['subject9Unit'],
                                                  Grade=request.POST['subject9Grade'],
                                                  GPA=res)
                
                # update GPA term 6
                GPA.objects.filter(pk=1).update(GPA_6=res)

                # ให้ res หรือ GPA ที่คำนวณไว้ก่อนหน้านี้ เก็บไว้ใน term6.GPA
                term6.GPA = res

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

        # ------------------------------------------------------ Term 7 -------------------------------------------------------------
        # ถ้า value ของ subjectTerm มีค่าเท่ากับ 7 (ถ้าเลือกเทอม 7)   
        if request.POST.get('subjectTerm') == "7":

            # ถ้าความยาวของวิชาในเทอม 7 มีค่าเท่ากับ 0
            if len(Term7.objects.all()) == 0 :
                # ให้สร้างช่องใส่ ชื่อวิชา หน่วยกิต เกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term7.objects.create(subject =request.POST['subject1name'],
                                     unit=request.POST['subject1Unit'],
                                     Grade=request.POST['subject1Grade'],
                                     GPA=res)

                Term7.objects.create(subject=request.POST['subject2name'],
                                     unit=request.POST['subject2Unit'],
                                     Grade=request.POST['subject2Grade'],
                                     GPA=res)

                Term7.objects.create(subject =request.POST['subject3name'],
                                     unit=request.POST['subject3Unit'],
                                     Grade=request.POST['subject3Grade'],
                                     GPA=res)

                Term7.objects.create(subject =request.POST['subject4name'],
                                     unit=request.POST['subject4Unit'],
                                     Grade=request.POST['subject4Grade'],
                                     GPA=res)

                Term7.objects.create(subject =request.POST['subject5name'],
                                     unit=request.POST['subject5Unit'],
                                     Grade=request.POST['subject5Grade'],
                                     GPA=res)

                Term7.objects.create(subject=request.POST['subject6name'],
                                     unit=request.POST['subject6Unit'],
                                     Grade=request.POST['subject6Grade'],
                                     GPA=res)

                Term7.objects.create(subject =request.POST['subject7name'],
                                     unit=request.POST['subject7Unit'],
                                     Grade=request.POST['subject7Grade'],
                                     GPA=res)

                Term7.objects.create(subject=request.POST['subject8name'],
                                     unit=request.POST['subject8Unit'],
                                     Grade=request.POST['subject8Grade'],
                                     GPA=res)

                Term7.objects.create(subject=request.POST['subject9name'],
                                     unit=request.POST['subject9Unit'],
                                     Grade=request.POST['subject9Grade'],
                                     GPA=res)

                # update GPA term 7
                GPA.objects.filter(pk=1).update(GPA_7=res)

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

            # other
            else:
                # update ช่องใส่ชื่อวิชา หน่วยกิต เกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term7.objects.filter(pk=1).update(subject =request.POST['subject1name'],
                                                  unit=request.POST['subject1Unit'], 
                                                  Grade=request.POST['subject1Grade'],
                                                  GPA=res)

                Term7.objects.filter(pk=2).update(subject =request.POST['subject2name'],
                                                  unit=request.POST['subject2Unit'],
                                                  Grade=request.POST['subject2Grade'],
                                                  GPA=res)

                Term7.objects.filter(pk=3).update(subject =request.POST['subject3name'], 
                                                  unit=request.POST['subject3Unit'],
                                                  Grade=request.POST['subject3Grade'],
                                                  GPA=res)

                Term7.objects.filter(pk=4).update(subject =request.POST['subject4name'], 
                                                  unit=request.POST['subject4Unit'],
                                                  Grade=request.POST['subject4Grade'],
                                                  GPA=res)

                Term7.objects.filter(pk=5).update(subject =request.POST['subject5name'],
                                                  unit=request.POST['subject5Unit'],
                                                  Grade=request.POST['subject5Grade'],
                                                  GPA=res)

                Term7.objects.filter(pk=6).update(subject =request.POST['subject6name'],
                                                  unit=request.POST['subject6Unit'],
                                                  Grade=request.POST['subject6Grade'],
                                                  GPA=res)

                Term7.objects.filter(pk=7).update(subject =request.POST['subject7name'],
                                                  unit=request.POST['subject7Unit'],
                                                  Grade=request.POST['subject7Grade'],
                                                  GPA=res)

                Term7.objects.filter(pk=8).update(subject =request.POST['subject8name'],
                                                  unit=request.POST['subject8Unit'],
                                                  Grade=request.POST['subject8Grade'],
                                                  GPA=res)

                Term7.objects.filter(pk=9).update(subject =request.POST['subject9name'],
                                                  unit=request.POST['subject9Unit'],
                                                  Grade=request.POST['subject9Grade'],
                                                  GPA=res)
                # update GPA term 7
                GPA.objects.filter(pk=1).update(GPA_7=res)

                # ให้ res หรือ GPA ที่คำนวณไว้ก่อนหน้านี้ เก็บไว้ใน term7.GPA
                term7.GPA = res

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

        # ------------------------------------------------------ Term 8 -------------------------------------------------------------
        # ถ้า value ของ subjectTerm มีค่าเท่ากับ 8 (ถ้าเลือกเทอม 8)   
        if request.POST.get('subjectTerm') == "8":

            # ถ้าความยาวของวิชาในเทอม 8 มีค่าเท่ากับ 0
            if len(Term8.objects.all()) == 0 :
                # ให้สร้างช่องใส่ ชื่อวิชา หน่วยกิต เกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term8.objects.create(subject =request.POST['subject1name'],
                                     unit=request.POST['subject1Unit'],
                                     Grade=request.POST['subject1Grade'],
                                     GPA=res)

                Term8.objects.create(subject=request.POST['subject2name'],
                                     unit=request.POST['subject2Unit'],
                                     Grade=request.POST['subject2Grade'],
                                     GPA=res)

                Term8.objects.create(subject =request.POST['subject3name'],
                                     unit=request.POST['subject3Unit'],
                                     Grade=request.POST['subject3Grade'],
                                     GPA=res)

                Term8.objects.create(subject =request.POST['subject4name'],
                                     unit=request.POST['subject4Unit'],
                                     Grade=request.POST['subject4Grade'],
                                     GPA=res)

                Term8.objects.create(subject =request.POST['subject5name'],
                                     unit=request.POST['subject5Unit'],
                                     Grade=request.POST['subject5Grade'],
                                     GPA=res)

                Term8.objects.create(subject=request.POST['subject6name'],
                                     unit=request.POST['subject6Unit'],
                                     Grade=request.POST['subject6Grade'],
                                     GPA=res)

                Term8.objects.create(subject =request.POST['subject7name'],
                                     unit=request.POST['subject7Unit'],
                                     Grade=request.POST['subject7Grade'],
                                     GPA=res)

                Term8.objects.create(subject=request.POST['subject8name'],
                                     unit=request.POST['subject8Unit'],
                                     Grade=request.POST['subject8Grade'],
                                     GPA=res)

                Term8.objects.create(subject=request.POST['subject9name'],
                                     unit=request.POST['subject9Unit'],
                                     Grade=request.POST['subject9Grade'],
                                     GPA=res)

                # update GPA term 8
                GPA.objects.filter(pk=1).update(GPA_8=res)

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

            # other
            else:
                # update ช่องใส่ ชื่อวิชา หน่วยกิต เกรด และเก็บเกรดแต่ละวิชาไว้ รวมแล้ว 9 วิชา
                Term8.objects.filter(pk=1).update(subject =request.POST['subject1name'],
                                                  unit=request.POST['subject1Unit'], 
                                                  Grade=request.POST['subject1Grade'],
                                                  GPA=res)

                Term8.objects.filter(pk=2).update(subject =request.POST['subject2name'],
                                                  unit=request.POST['subject2Unit'],
                                                  Grade=request.POST['subject2Grade'],
                                                  GPA=res)

                Term8.objects.filter(pk=3).update(subject =request.POST['subject3name'], 
                                                  unit=request.POST['subject3Unit'],
                                                  Grade=request.POST['subject3Grade'],
                                                  GPA=res)

                Term8.objects.filter(pk=4).update(subject =request.POST['subject4name'], 
                                                  unit=request.POST['subject4Unit'],
                                                  Grade=request.POST['subject4Grade'],
                                                  GPA=res)

                Term8.objects.filter(pk=5).update(subject =request.POST['subject5name'],
                                                  unit=request.POST['subject5Unit'],
                                                  Grade=request.POST['subject5Grade'],
                                                  GPA=res)

                Term8.objects.filter(pk=6).update(subject =request.POST['subject6name'],
                                                  unit=request.POST['subject6Unit'],
                                                  Grade=request.POST['subject6Grade'],
                                                  GPA=res)

                Term8.objects.filter(pk=7).update(subject =request.POST['subject7name'],
                                                  unit=request.POST['subject7Unit'],
                                                  Grade=request.POST['subject7Grade'],
                                                  GPA=res)

                Term8.objects.filter(pk=8).update(subject =request.POST['subject8name'],
                                                  unit=request.POST['subject8Unit'],
                                                  Grade=request.POST['subject8Grade'],
                                                  GPA=res)

                Term8.objects.filter(pk=9).update(subject =request.POST['subject9name'],
                                                  unit=request.POST['subject9Unit'],
                                                  Grade=request.POST['subject9Grade'],
                                                  GPA=res)

                # update GPA term 8
                GPA.objects.filter(pk=1).update(GPA_8=res)

                # ให้ res หรือ GPA ที่คำนวณไว้ก่อนหน้านี้ เก็บไว้ใน term8.GPA
                term8.GPA = res

                # render home.html พร้อมบอก GPA ในเทอมนั้น ๆ
                return render(request, 'home.html',{'result':res})

        # other 
        else:
            # render home.html พร้อมบอก message ตามข้างต้นที่ได้กำหนดไว้
            return render(request, 'home.html',{'message':message})

# Search หาวิชาที่ต้องการดูตัวต่อของวิชานั้น ๆ
def search_subjects_in_the_flow(request):
    # เก็บ result เป็นช่องว่าง
    result = ''
    # เก็บ text input ที่จะ search เป็น string
    subjects = str(request.POST.get('searchFlow',''))
    # ถ้ามีการกดปุ่ม search
    if 'searchSubject' in request.POST :
        # ถ้า text input เป็นวิชานี้ ให้ result เป็นวิชานี้
        # 1 ProFund
        if subjects == "Programming Fundamental" :
            result = """Semister2 : Algorithms and Data Structures <br />
            Semister5 : Operating Systems"""

        # 2 MathI
        elif subjects == "Engineering Mathematics I" :
            result = """Semister2 : Math II <br />
            Semister3 : Statistics for Computer Engineer"""

        # 3 ComExplo
        elif subjects == "Computer Engineering Exploration" :
            result = "The subject hasn't other subjects to connect the flow"

        # 4 PhysicsI
        elif subjects == "Physics I" :
            result = "Semister2 : Physics II"

        # 5 PhyLabI
        elif subjects == "Physics Laboratory I" :
            result = "The subject hasn't other subjects to connect the flow"

        # 6 EnglishI
        elif subjects == "Language Elective Course I" :
            result = "Language Elective Course II"

        # 7 TableTennis
        elif subjects == "Physical Education Elective Course I" :
            result = "Physical Education Elective Course II"

        # 8 ManSo
        elif subjects == "Social Sciences Elective Course" :
            result = "The subject hasn't other subjects to connect the flow"

        # 9 Intro
        elif subjects == "Introduction to Engineer" :
            result = "The subject hasn't other subjects to connect the flow"

        # 10 Circuit
        elif subjects == "Electric Circuit Theory" :
            result = "Semister4 : Analog and Digital Electronics"

        # 11 CircuitLab
        elif subjects == "Electric Circuit Lab" :
            result = "The subject hasn't other subjects to connect the flow"

        # 12 Algo
        elif subjects == "Algorithms and Data Structure" :
            result = """Semister3 : Software Development Practice I <br />
            Semister5 : Computer Organization <br />
            Semister6 : Database Systems"""

        # 13 Work Ethics
        elif subjects == "Work Ethics" :
            result = "The subject hasn't other subjects to connect the flow"

        # 14 MathII
        elif subjects == "Engineering Mathematics II" :
            result = """Semister3 : Discrete Mathematics <br />
            Semister3 : Introduction to Signals and System"""

        # 15 PhysicsII
        elif subjects == "Physics II" :
            result = "The subject hasn't other subjects to connect the flow"

        # 16 PhyLab2
        elif subjects == "Physics Laboratory II" :
            result = "The subject hasn't other subjects to connect the flow"

        # 17 EnglishII
        elif subjects == "Language Elective Course II" :
            result = "Language Elective Course III"

        # 18 Basketball
        elif subjects == "Physical Education Elective Course II" :
            result = "The subject hasn't other subjects to connect the flow"

        # 19 Stat
        elif subjects == "Statistics for Computer Engineer" :
            result = "The subject hasn't other subjects to connect the flow"

        # 20 Signal
        elif subjects == "Introduction to Signals and System" :
            result = "The subject hasn't other subjects to connect the flow"

        # 21 Digital
        elif subjects == "Logic Design of Digital System" :
            result = """Semister3 : Digital System Design Laboratory <br />
            Semister4 : Computer Organization"""

        # 22 DigiLab
        elif subjects == "Digital System Design Laboratory" :
            result = "The subject hasn't other subjects to connect the flow"

        # 23 SoftwareI
        elif subjects == "Software Development Practice I" :
            result = "Semister4 : Software Development Practice II"

        # 24 Discrete Math
        elif subjects == "Discrete Mathematics" :
            result = "Semister6 : Database Systems"

        # 25 PhyLife
        elif subjects == "Science and Maths Elective I" :
            result = "Science and Maths Elective II"

        # 26 SoftwareII
        elif subjects == "Software Development Practice II" :
            result = "Semister5 : Software Engineering"

        # 27 NetworkI
        elif subjects == "Computer Networks I" :
            result = "Semister5 : Computer Networks II"

        # 28 ComOr
        elif subjects == "Computer Organization" :
            result = "Semister5 : Embedded System Design"

        # 29 Ubi
        elif subjects == "Ubiquitous Computing" :
            result = "The subject hasn't other subjects to connect the flow"

        # 30 Analog
        elif subjects == "Analog and Digital Electronics" :
            result = "Semister5 : Analog and Digital Electronics Lab"

        # 31 GenMath
        elif subjects == "Science and Maths Elective II" :
            result = "Science and Maths Elective III"

        # 32 SoftEng
        elif subjects == "Software Engineering" :
            result = "The subject hasn't other subjects to connect the flow"

        # 33 NetworkII
        elif subjects == "Computer Networks II" :
            result = "Semister6 : Computer Networks Lab"

        # 34 OS
        elif subjects == "Operating Systems" :
            result = "The subject hasn't other subjects to connect the flow"

        # 35 Embedded
        elif subjects == "Embedded System Design" :
            result = "Semister6 : Embedded System Design Laboratory"

        # 36 AnalogLab
        elif subjects == "Analog and Digital Electronics Lab" :
            result = "The subject hasn't other subjects to connect the flow"

        # 37 Language Elective III
        elif subjects == "Language Elective Course III" :
            result = "Language Elective Course IV"

        # 38 Database
        elif subjects == "Database Systems" :
            result = "The subject hasn't other subjects to connect the flow"

        # 39 NetworkLab
        elif subjects == "Computer Networks Lab" :
            result = "The subject hasn't other subjects to connect the flow"

        # 40 EmbeddedLab
        elif subjects == "Embedded System Design Laboratory" :
            result = "The subject hasn't other subjects to connect the flow"

        # 41 Language Elective IV
        elif subjects == "Language Elective Course IV" :
            result = "The subject hasn't other subjects to connect the flow"

        # 42 Computer Eng. Elective Course I
        elif subjects == "Computer Eng. Elective Course I" :
            result = "Computer Eng. Elective Course II"

        # 43 Computer Eng. Elective Course II
        elif subjects == "Computer Eng. Elective Course II" :
            result = "The subject hasn't other subjects to connect the flow"

        # 44 Humanities Elective Course I
        elif subjects == "Humanities Elective Course I" :
            result = "Humanities Elective Course II"

        # 45 ProjectI
        elif subjects == "Project I" :
            result = "Semister8 : Project II"

        # 46 Free Elective Course I
        elif subjects == "Free Elective Course I" :
            result = "Free Elective Course I"

        # 47 Humanities Elective Course II
        elif subjects == "Humanities Elective Course II" :
            result = "The subject hasn't other subjects to connect the flow"

        # 48 Computer Eng. Elective Course III
        elif subjects == "Computer Eng. Elective Course III" :
            result = "Computer Eng. Elective Course IV"

        # 49 Computer Eng. Elective Course IV
        elif subjects == "Computer Eng. Elective Course IV" :
            result = "The subject hasn't other subjects to connect the flow"

        # 50 ProjectII
        elif subjects == "Project II" :
            result = "The subject hasn't other subjects to connect the flow"

        # 51 Computer Eng. Seminar
        elif subjects == "Computer Eng. Seminar" :
            result = "The subject hasn't other subjects to connect the flow"

        # 52 Free Elective Course II
        elif subjects == "Free Elective Course II" :
            result = "The subject hasn't other subjects to connect the flow"

        # 53 Science and Maths Elective III
        elif subjects == "Science and Maths Elective III" :
            result = "The subject hasn't other subjects to connect the flow"

        # Other
        else :
            # ถ้าวิชานั้นไม่มีใน Flow ให้ Result เป็น The subject isn't in the flow
            result = "The subject isn't in the flow"

    # ให้ render หน้า flow.html ออกมา 
    # โดยให้แสดงชื่อวิชาและตัวต่อของวิชานั้น ๆ ตามที่ได้กำหนดไว้ใน flow.html
    return render(request, 'flow.html',{'subjects':subjects, 'Result':result})

# รวมทุกวิชาใน flow โดยเรียงตามเทอมในรูป flow
def list_of_subjects(request) :
    # term 1
    first_semister = """ Programming Fundamental<br />
            Engineering Mathematics I<br />
            Computer Engineering Exploration<br />
            Physics I<br />
            Physics Laboratory I<br />
            Language Elective Course I<br />
            Physical Education Elective Course I<br />
            Social Sciences Elective Course<br />
            Introduction to Engineer<br />"""

    # term 2
    second_semister = """Electric Circuit Theory<br />
            Electric Circuit Lab<br />
            Algorithms and Data Structure<br />
            Work Ethics<br />
            Engineering Mathematics II<br />
            Physics II<br />
            Physics Laboratory II<br />
            Language Elective Course II<br />
            Physical Education Elective Course II<br />"""

    # term 3
    third_semister = """Statistics for Computer Engineer<br />
            Introduction to Signals and System<br />
            Logic Design of Digital System<br />
            Digital System Design Laboratory<br />
            Software Development Practice I<br />
            Discrete Mathematics<br />
            Science and Maths Elective I<br />"""

    # term 4
    fourth_semister = """Software Development Practice II<br />
            Computer Networks I<br />
            Computer Organization<br />
            Ubiquitous Computing<br />
            Analog and Digital Electronics<br />
            Science and Maths Elective II<br />"""

    # term 5
    fifth_semister = """Software Engineering<br />
            Computer Networks II<br />
            Operating Systems<br />
            Embedded System Design<br />
            Analog and Digital Electronics Lab<br />
            Language Elective Course III<br />"""

    # term 6
    sixth_semister = """Database Systems<br />
            Computer Networks Lab<br />
            Embedded System Design Laboratory<br />
            Language Elective Course IV<br />
            Computer Eng. Elective Course I<br />
            Computer Eng. Elective Course II<br />
            Humanities Elective Course I<br />"""

    # term 7
    seventh_semister = """Project I<br />
            Free Elective Course I<br />
            Humanities Elective Course II<br />
            Computer Eng. Elective Course III<br />
            Computer Eng. Elective Course IV<br />"""

    # term 8
    eighth_semister = """Project II<br />
            Computer Eng. Seminar<br />
            Free Elective Course II<br />
            Science and Maths Elective III"""

    # render หน้า subject.html ออกมา เรียงตามเทอมนั้น ๆ 
    return render(request, 'subject.html', {'semister1':first_semister,
                                            'semister2':second_semister,
                                            'semister3':third_semister,
                                            'semister4':fourth_semister,
                                            'semister5':fifth_semister,
                                            'semister6':sixth_semister,
                                            'semister7':seventh_semister,
                                            'semister8':eighth_semister} )

# แสดงกราฟ
def graph(request):
    # ให้ค่า countunit เป็น 0
    COUNT_UNIT = 0
    # ให้ค่า GPAX เป็น 0
    GPAX = 0
    # เก็บ ชื่อวิชา หน่วยกิต และเกรด ของแต่ละเทอมไว้ใน dataterm_1 - dataterm_9 ตามลำดับ
    first_dataterm = Term1.objects.all()
    second_dataterm = Term2.objects.all()
    third_dataterm = Term3.objects.all()
    fourth_dataterm = Term4.objects.all()
    fifth_dataterm = Term5.objects.all()
    sixth_dataterm = Term6.objects.all()
    seventh_dataterm = Term7.objects.all()
    eighth_dataterm = Term8.objects.all()
    # เก็บ GPA ทั้วหมดไว้ใน DATA_GPA
    DATA_GPA = GPA.objects.all()

    # ถ้าความยาวของ DATA_GPA เป็น 0
    if len(DATA_GPA) == 0:
        # ให้สร้าง GPA ตั้งแต่เทอมแรกจนถึงเทอมสุดท้าย โดยค่าแรกของแต่ละเทอมเป็น 0
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, 
                           GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
    
    # loop สำหรับ i ใน DATA_GPA
    for i in DATA_GPA:
        # เก็บผลรวมของ GPA term 1 - GPA term 9 ไว้ใน GPAX
        GPAX = float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4) +\
               float(i.GPA_5) + float(i.GPA_6) + float(i.GPA_7) + float(i.GPA_8)
    
    # ถ้า GPAX มีค่ามากกว่า 0.0
    if GPAX > 0.0:
        # loop สำหรับ unit ใน dataGPA
        for unit in DATA_GPA:

            # ถ้า GPA ในเทอม 1 ไม่เท่ากับ 0 
            if unit.GPA_1 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 2 ไม่เท่ากับ 0 
            if unit.GPA_2 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1

            # ถ้า GPA ในเทอม 3 ไม่เท่ากับ 0 
            if unit.GPA_3 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 4 ไม่เท่ากับ 0 
            if unit.GPA_4 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 5 ไม่เท่ากับ 0 
            if unit.GPA_5 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 6 ไม่เท่ากับ 0 
            if unit.GPA_6 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 7 ไม่เท่ากับ 0 
            if unit.GPA_7 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 8 ไม่เท่ากับ 0 
            if unit.GPA_8 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
    
    # other
    else:
        # ให้ COUNT_UNIT บวกเท่ากับ 1
        COUNT_UNIT += 1

    # เก็บผลหารระหว่าง GPAX กับ countunit ไว้ใน resGPAX
    RES_GPAX = float(GPAX) / float(COUNT_UNIT)
    # นำ RES_GPAX มาทำให้เหลือทศนิยม 2 ตำแหน่ง เก็บไว้ใน NEW_GPAX
    NEW_GPAX = '%.2f' % RES_GPAX

    # render Graph.html ให้แสดงข้อมูลตามเทอม โดยมีเส้นกราฟ GPA ระบุไว้ พร้อมแสดง GPAX
    return render(request, 'Graph.html', {'dataterm1': first_dataterm,
                                          'dataterm2': second_dataterm,
                                          'dataterm3': third_dataterm, 
                                          'dataterm4': fourth_dataterm,
                                          'dataterm5': fifth_dataterm, 
                                          'dataterm6': sixth_dataterm,
                                          'dataterm7': seventh_dataterm, 
                                          'dataterm8': eighth_dataterm,
                                          'GPARES': DATA_GPA, 
                                          'res_GPAX': NEW_GPAX})

# แสดง วิชา หน่วยกิต เกรด ของแต่ละวิชา พร้อม GPA ในเทอม 1 และ GPAX 
def first_term(request):
    # เก็บ GPA ไว้ใน DATA_GPA
    DATA_GPA = GPA.objects.all()
    # เก็บ วิชา หน่วยกิต และเกรด ไว้ใน dataterm_1
    first_dataterm = Term1.objects.all()
    # ให้ค่า COUNT_UNIT เป็น 0
    COUNT_UNIT = 0

    # ถ้าความยาวของ DATA_GPA เป็น 0
    if len(DATA_GPA) == 0:
        # ให้สร้าง GPA ตั้งแต่เทอมแรกจนถึงเทอมสุดท้าย โดยค่าแรกของแต่ละเทอมเป็น 0
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0,
                           GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )

    # loop สำหรับ i ใน dataGPA
    for i in DATA_GPA:
        # เก็บผลรวมของ GPA term 1 - GPA term 8 ไว้ใน GPAX
        GPAX = ( float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4)
               + float(i.GPA_5) + float(i.GPA_6) + float(i.GPA_7) + float(i.GPA_8) )
    
    # ถ้า GPAX มีค่ามากกว่า 0.0
    if GPAX > 0.0:
        # loop สำหรับ unit ใน DATA_GPA
        for unit in DATA_GPA:

            # ถ้า GPA ในเทอม 1 ไม่เท่ากับ 0 
            if unit.GPA_1 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 2 ไม่เท่ากับ 0 
            if unit.GPA_2 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1

            # ถ้า GPA ในเทอม 3 ไม่เท่ากับ 0 
            if unit.GPA_3 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 4 ไม่เท่ากับ 0 
            if unit.GPA_4 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 5 ไม่เท่ากับ 0 
            if unit.GPA_5 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 6 ไม่เท่ากับ 0 
            if unit.GPA_6 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 7 ไม่เท่ากับ 0 
            if unit.GPA_7 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 8 ไม่เท่ากับ 0 
            if unit.GPA_8 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
    
    # other
    else:
        # ให้ COUNT_UNIT บวกเท่ากับ 1
        COUNT_UNIT += 1

    # เก็บผลหารระหว่าง GPAX กับ COUNT_UNIT ไว้ใน RES_GPAX
    RES_GPAX = float(GPAX) / float(COUNT_UNIT)
    # นำ RES_GPAX มาทำให้เหลือทศนิยม 2 ตำแหน่ง เก็บไว้ใน NEW_GPAX
    NEW_GPAX = '%.2f' % RES_GPAX
    
    # render firstTerm.html แสดงข้อมูลวิชา หน่วยกิต และเกรด ของแต่ละวิชา
    # ที่ได้ทำการคำนวณไว้ พร้อมแสดง GPA ในเทอมนี้ และแสดง GPAX
    return render(request, 'firstTerm.html', {'dataterm1':first_dataterm,
                                              'GPARES':DATA_GPA,
                                              'res_GPAX': NEW_GPAX})
    
# แสดง วิชา หน่วยกิต เกรด ของแต่ละวิชา พร้อม GPA ในเทอม 2 และ GPAX 
def second_term(request):
    # เก็บ GPA ไว้ใน DATA_GPA
    DATA_GPA = GPA.objects.all()
    # เก็บ วิชา หน่วยกิต และเกรด ไว้ใน dataterm_1
    second_dataterm = Term2.objects.all()
    # ให้ค่า COUNT_UNIT เป็น 0
    COUNT_UNIT = 0

    # ถ้าความยาวของ DATA_GPA เป็น 0
    if len(DATA_GPA) == 0:
        # ให้สร้าง GPA ตั้งแต่เทอมแรกจนถึงเทอมสุดท้าย โดยค่าแรกของแต่ละเทอมเป็น 0
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0,
                           GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )

    # loop สำหรับ i ใน dataGPA
    for i in DATA_GPA:
        # เก็บผลรวมของ GPA term 1 - GPA term 8 ไว้ใน GPAX
        GPAX = ( float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4)
               + float(i.GPA_5) + float(i.GPA_6) + float(i.GPA_7) + float(i.GPA_8) )
    
    # ถ้า GPAX มีค่ามากกว่า 0.0
    if GPAX > 0.0:
        # loop สำหรับ unit ใน DATA_GPA
        for unit in DATA_GPA:

            # ถ้า GPA ในเทอม 1 ไม่เท่ากับ 0 
            if unit.GPA_1 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 2 ไม่เท่ากับ 0 
            if unit.GPA_2 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1

            # ถ้า GPA ในเทอม 3 ไม่เท่ากับ 0 
            if unit.GPA_3 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 4 ไม่เท่ากับ 0 
            if unit.GPA_4 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 5 ไม่เท่ากับ 0 
            if unit.GPA_5 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 6 ไม่เท่ากับ 0 
            if unit.GPA_6 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 7 ไม่เท่ากับ 0 
            if unit.GPA_7 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 8 ไม่เท่ากับ 0 
            if unit.GPA_8 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
    
    # other
    else:
        # ให้ COUNT_UNIT บวกเท่ากับ 1
        COUNT_UNIT += 1

    # เก็บผลหารระหว่าง GPAX กับ COUNT_UNIT ไว้ใน RES_GPAX
    RES_GPAX = float(GPAX) / float(COUNT_UNIT)
    # นำ RES_GPAX มาทำให้เหลือทศนิยม 2 ตำแหน่ง เก็บไว้ใน NEW_GPAX
    NEW_GPAX = '%.2f' % RES_GPAX
    
    # render secondTerm.html แสดงข้อมูลวิชา หน่วยกิต และเกรด ของแต่ละวิชา
    # ที่ได้ทำการคำนวณไว้ พร้อมแสดง GPA ในเทอมนี้ และแสดง GPAX
    return render(request, 'secondTerm.html', {'dataterm2':second_dataterm,
                                              'GPARES':DATA_GPA,
                                              'res_GPAX': NEW_GPAX})

# แสดง วิชา หน่วยกิต เกรด ของแต่ละวิชา พร้อม GPA ในเทอม 3 และ GPAX 
def third_term(request):
    # เก็บ GPA ไว้ใน DATA_GPA
    DATA_GPA = GPA.objects.all()
    # เก็บ วิชา หน่วยกิต และเกรด ไว้ใน dataterm_1
    third_dataterm = Term3.objects.all()
    # ให้ค่า COUNT_UNIT เป็น 0
    COUNT_UNIT = 0

    # ถ้าความยาวของ DATA_GPA เป็น 0
    if len(DATA_GPA) == 0:
        # ให้สร้าง GPA ตั้งแต่เทอมแรกจนถึงเทอมสุดท้าย โดยค่าแรกของแต่ละเทอมเป็น 0
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0,
                           GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )

    # loop สำหรับ i ใน dataGPA
    for i in DATA_GPA:
        # เก็บผลรวมของ GPA term 1 - GPA term 8 ไว้ใน GPAX
        GPAX = ( float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4)
               + float(i.GPA_5) + float(i.GPA_6) + float(i.GPA_7) + float(i.GPA_8) )
    
    # ถ้า GPAX มีค่ามากกว่า 0.0
    if GPAX > 0.0:
        # loop สำหรับ unit ใน DATA_GPA
        for unit in DATA_GPA:

            # ถ้า GPA ในเทอม 1 ไม่เท่ากับ 0 
            if unit.GPA_1 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 2 ไม่เท่ากับ 0 
            if unit.GPA_2 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1

            # ถ้า GPA ในเทอม 3 ไม่เท่ากับ 0 
            if unit.GPA_3 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 4 ไม่เท่ากับ 0 
            if unit.GPA_4 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 5 ไม่เท่ากับ 0 
            if unit.GPA_5 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 6 ไม่เท่ากับ 0 
            if unit.GPA_6 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 7 ไม่เท่ากับ 0 
            if unit.GPA_7 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 8 ไม่เท่ากับ 0 
            if unit.GPA_8 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
    
    # other
    else:
        # ให้ COUNT_UNIT บวกเท่ากับ 1
        COUNT_UNIT += 1

    # เก็บผลหารระหว่าง GPAX กับ COUNT_UNIT ไว้ใน RES_GPAX
    RES_GPAX = float(GPAX) / float(COUNT_UNIT)
    # นำ RES_GPAX มาทำให้เหลือทศนิยม 2 ตำแหน่ง เก็บไว้ใน NEW_GPAX
    NEW_GPAX = '%.2f' % RES_GPAX
    
    # render thirdTerm.html แสดงข้อมูลวิชา หน่วยกิต และเกรด ของแต่ละวิชา
    # ที่ได้ทำการคำนวณไว้ พร้อมแสดง GPA ในเทอมนี้ และแสดง GPAX
    return render(request, 'thirdTerm.html', {'dataterm3':third_dataterm,
                                              'GPARES':DATA_GPA,
                                              'res_GPAX': NEW_GPAX})

# แสดง วิชา หน่วยกิต เกรด ของแต่ละวิชา พร้อม GPA ในเทอม 4 และ GPAX 
def fourth_term(request):
    # เก็บ GPA ไว้ใน DATA_GPA
    DATA_GPA = GPA.objects.all()
    # เก็บ วิชา หน่วยกิต และเกรด ไว้ใน dataterm_1
    fourth_dataterm = Term4.objects.all()
    # ให้ค่า COUNT_UNIT เป็น 0
    COUNT_UNIT = 0

    # ถ้าความยาวของ DATA_GPA เป็น 0
    if len(DATA_GPA) == 0:
        # ให้สร้าง GPA ตั้งแต่เทอมแรกจนถึงเทอมสุดท้าย โดยค่าแรกของแต่ละเทอมเป็น 0
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0,
                           GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )

    # loop สำหรับ i ใน dataGPA
    for i in DATA_GPA:
        # เก็บผลรวมของ GPA term 1 - GPA term 8 ไว้ใน GPAX
        GPAX = ( float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4)
               + float(i.GPA_5) + float(i.GPA_6) + float(i.GPA_7) + float(i.GPA_8) )
    
    # ถ้า GPAX มีค่ามากกว่า 0.0
    if GPAX > 0.0:
        # loop สำหรับ unit ใน DATA_GPA
        for unit in DATA_GPA:

            # ถ้า GPA ในเทอม 1 ไม่เท่ากับ 0 
            if unit.GPA_1 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 2 ไม่เท่ากับ 0 
            if unit.GPA_2 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1

            # ถ้า GPA ในเทอม 3 ไม่เท่ากับ 0 
            if unit.GPA_3 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 4 ไม่เท่ากับ 0 
            if unit.GPA_4 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 5 ไม่เท่ากับ 0 
            if unit.GPA_5 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 6 ไม่เท่ากับ 0 
            if unit.GPA_6 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 7 ไม่เท่ากับ 0 
            if unit.GPA_7 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 8 ไม่เท่ากับ 0 
            if unit.GPA_8 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
    
    # other
    else:
        # ให้ COUNT_UNIT บวกเท่ากับ 1
        COUNT_UNIT += 1

    # เก็บผลหารระหว่าง GPAX กับ COUNT_UNIT ไว้ใน RES_GPAX
    RES_GPAX = float(GPAX) / float(COUNT_UNIT)
    # นำ RES_GPAX มาทำให้เหลือทศนิยม 2 ตำแหน่ง เก็บไว้ใน NEW_GPAX
    NEW_GPAX = '%.2f' % RES_GPAX
    
    # render fourthTerm.html แสดงข้อมูลวิชา หน่วยกิต และเกรด ของแต่ละวิชา
    # ที่ได้ทำการคำนวณไว้ พร้อมแสดง GPA ในเทอมนี้ และแสดง GPAX
    return render(request, 'fourthTerm.html', {'dataterm4':fourth_dataterm,
                                              'GPARES':DATA_GPA,
                                              'res_GPAX': NEW_GPAX})

# แสดง วิชา หน่วยกิต เกรด ของแต่ละวิชา พร้อม GPA ในเทอม 5 และ GPAX 
def fifth_term(request):
    # เก็บ GPA ไว้ใน DATA_GPA
    DATA_GPA = GPA.objects.all()
    # เก็บ วิชา หน่วยกิต และเกรด ไว้ใน dataterm_1
    fifth_dataterm = Term5.objects.all()
    # ให้ค่า COUNT_UNIT เป็น 0
    COUNT_UNIT = 0

    # ถ้าความยาวของ DATA_GPA เป็น 0
    if len(DATA_GPA) == 0:
        # ให้สร้าง GPA ตั้งแต่เทอมแรกจนถึงเทอมสุดท้าย โดยค่าแรกของแต่ละเทอมเป็น 0
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0,
                           GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )

    # loop สำหรับ i ใน dataGPA
    for i in DATA_GPA:
        # เก็บผลรวมของ GPA term 1 - GPA term 8 ไว้ใน GPAX
        GPAX = ( float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4)
               + float(i.GPA_5) + float(i.GPA_6) + float(i.GPA_7) + float(i.GPA_8) )
    
    # ถ้า GPAX มีค่ามากกว่า 0.0
    if GPAX > 0.0:
        # loop สำหรับ unit ใน DATA_GPA
        for unit in DATA_GPA:

            # ถ้า GPA ในเทอม 1 ไม่เท่ากับ 0 
            if unit.GPA_1 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 2 ไม่เท่ากับ 0 
            if unit.GPA_2 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1

            # ถ้า GPA ในเทอม 3 ไม่เท่ากับ 0 
            if unit.GPA_3 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 4 ไม่เท่ากับ 0 
            if unit.GPA_4 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 5 ไม่เท่ากับ 0 
            if unit.GPA_5 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 6 ไม่เท่ากับ 0 
            if unit.GPA_6 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 7 ไม่เท่ากับ 0 
            if unit.GPA_7 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 8 ไม่เท่ากับ 0 
            if unit.GPA_8 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
    
    # other
    else:
        # ให้ COUNT_UNIT บวกเท่ากับ 1
        COUNT_UNIT += 1

    # เก็บผลหารระหว่าง GPAX กับ COUNT_UNIT ไว้ใน RES_GPAX
    RES_GPAX = float(GPAX) / float(COUNT_UNIT)
    # นำ RES_GPAX มาทำให้เหลือทศนิยม 2 ตำแหน่ง เก็บไว้ใน NEW_GPAX
    NEW_GPAX = '%.2f' % RES_GPAX
    
    # render fifthTerm.html แสดงข้อมูลวิชา หน่วยกิต และเกรด ของแต่ละวิชา
    # ที่ได้ทำการคำนวณไว้ พร้อมแสดง GPA ในเทอมนี้ และแสดง GPAX
    return render(request, 'fifthTerm.html', {'dataterm5':fifth_dataterm,
                                              'GPARES':DATA_GPA,
                                              'res_GPAX': NEW_GPAX})

# แสดง วิชา หน่วยกิต เกรด ของแต่ละวิชา พร้อม GPA ในเทอม 6 และ GPAX 
def sixth_term(request):
    # เก็บ GPA ไว้ใน DATA_GPA
    DATA_GPA = GPA.objects.all()
    # เก็บ วิชา หน่วยกิต และเกรด ไว้ใน dataterm_1
    sixth_dataterm = Term6.objects.all()
    # ให้ค่า COUNT_UNIT เป็น 0
    COUNT_UNIT = 0

    # ถ้าความยาวของ DATA_GPA เป็น 0
    if len(DATA_GPA) == 0:
        # ให้สร้าง GPA ตั้งแต่เทอมแรกจนถึงเทอมสุดท้าย โดยค่าแรกของแต่ละเทอมเป็น 0
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0,
                           GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )

    # loop สำหรับ i ใน dataGPA
    for i in DATA_GPA:
        # เก็บผลรวมของ GPA term 1 - GPA term 8 ไว้ใน GPAX
        GPAX = ( float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4)
               + float(i.GPA_5) + float(i.GPA_6) + float(i.GPA_7) + float(i.GPA_8) )
    
    # ถ้า GPAX มีค่ามากกว่า 0.0
    if GPAX > 0.0:
        # loop สำหรับ unit ใน DATA_GPA
        for unit in DATA_GPA:

            # ถ้า GPA ในเทอม 1 ไม่เท่ากับ 0 
            if unit.GPA_1 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 2 ไม่เท่ากับ 0 
            if unit.GPA_2 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1

            # ถ้า GPA ในเทอม 3 ไม่เท่ากับ 0 
            if unit.GPA_3 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 4 ไม่เท่ากับ 0 
            if unit.GPA_4 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 5 ไม่เท่ากับ 0 
            if unit.GPA_5 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 6 ไม่เท่ากับ 0 
            if unit.GPA_6 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 7 ไม่เท่ากับ 0 
            if unit.GPA_7 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 8 ไม่เท่ากับ 0 
            if unit.GPA_8 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
    
    # other
    else:
        # ให้ COUNT_UNIT บวกเท่ากับ 1
        COUNT_UNIT += 1

    # เก็บผลหารระหว่าง GPAX กับ COUNT_UNIT ไว้ใน RES_GPAX
    RES_GPAX = float(GPAX) / float(COUNT_UNIT)
    # นำ RES_GPAX มาทำให้เหลือทศนิยม 2 ตำแหน่ง เก็บไว้ใน NEW_GPAX
    NEW_GPAX = '%.2f' % RES_GPAX
    
    # render sixthTerm.html แสดงข้อมูลวิชา หน่วยกิต และเกรด ของแต่ละวิชา
    # ที่ได้ทำการคำนวณไว้ พร้อมแสดง GPA ในเทอมนี้ และแสดง GPAX
    return render(request, 'sixthTerm.html', {'dataterm6':sixth_dataterm,
                                              'GPARES':DATA_GPA,
                                              'res_GPAX': NEW_GPAX})

# แสดง วิชา หน่วยกิต เกรด ของแต่ละวิชา พร้อม GPA ในเทอม 7 และ GPAX 
def seventh_term(request):
    # เก็บ GPA ไว้ใน DATA_GPA
    DATA_GPA = GPA.objects.all()
    # เก็บ วิชา หน่วยกิต และเกรด ไว้ใน dataterm_1
    seventh_dataterm = Term7.objects.all()
    # ให้ค่า COUNT_UNIT เป็น 0
    COUNT_UNIT = 0

    # ถ้าความยาวของ DATA_GPA เป็น 0
    if len(DATA_GPA) == 0:
        # ให้สร้าง GPA ตั้งแต่เทอมแรกจนถึงเทอมสุดท้าย โดยค่าแรกของแต่ละเทอมเป็น 0
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0,
                           GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )

    # loop สำหรับ i ใน dataGPA
    for i in DATA_GPA:
        # เก็บผลรวมของ GPA term 1 - GPA term 8 ไว้ใน GPAX
        GPAX = ( float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4)
               + float(i.GPA_5) + float(i.GPA_6) + float(i.GPA_7) + float(i.GPA_8) )
    
    # ถ้า GPAX มีค่ามากกว่า 0.0
    if GPAX > 0.0:
        # loop สำหรับ unit ใน DATA_GPA
        for unit in DATA_GPA:

            # ถ้า GPA ในเทอม 1 ไม่เท่ากับ 0 
            if unit.GPA_1 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 2 ไม่เท่ากับ 0 
            if unit.GPA_2 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1

            # ถ้า GPA ในเทอม 3 ไม่เท่ากับ 0 
            if unit.GPA_3 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 4 ไม่เท่ากับ 0 
            if unit.GPA_4 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 5 ไม่เท่ากับ 0 
            if unit.GPA_5 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 6 ไม่เท่ากับ 0 
            if unit.GPA_6 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 7 ไม่เท่ากับ 0 
            if unit.GPA_7 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 8 ไม่เท่ากับ 0 
            if unit.GPA_8 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
    
    # other
    else:
        # ให้ COUNT_UNIT บวกเท่ากับ 1
        COUNT_UNIT += 1

    # เก็บผลหารระหว่าง GPAX กับ COUNT_UNIT ไว้ใน RES_GPAX
    RES_GPAX = float(GPAX) / float(COUNT_UNIT)
    # นำ RES_GPAX มาทำให้เหลือทศนิยม 2 ตำแหน่ง เก็บไว้ใน NEW_GPAX
    NEW_GPAX = '%.2f' % RES_GPAX
    
    # render seventhTerm.html แสดงข้อมูลวิชา หน่วยกิต และเกรด ของแต่ละวิชา
    # ที่ได้ทำการคำนวณไว้ พร้อมแสดง GPA ในเทอมนี้ และแสดง GPAX
    return render(request, 'seventhTerm.html', {'dataterm7':seventh_dataterm,
                                              'GPARES':DATA_GPA,
                                              'res_GPAX': NEW_GPAX})

# แสดง วิชา หน่วยกิต เกรด ของแต่ละวิชา พร้อม GPA ในเทอม 8 และ GPAX 
def eight_term(request):
    # เก็บ GPA ไว้ใน DATA_GPA
    DATA_GPA = GPA.objects.all()
    # เก็บ วิชา หน่วยกิต และเกรด ไว้ใน dataterm_1
    eighth_dataterm = Term8.objects.all()
    # ให้ค่า COUNT_UNIT เป็น 0
    COUNT_UNIT = 0

    # ถ้าความยาวของ DATA_GPA เป็น 0
    if len(DATA_GPA) == 0:
        # ให้สร้าง GPA ตั้งแต่เทอมแรกจนถึงเทอมสุดท้าย โดยค่าแรกของแต่ละเทอมเป็น 0
        GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0,
                           GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )

    # loop สำหรับ i ใน dataGPA
    for i in DATA_GPA:
        # เก็บผลรวมของ GPA term 1 - GPA term 8 ไว้ใน GPAX
        GPAX = ( float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4)
               + float(i.GPA_5) + float(i.GPA_6) + float(i.GPA_7) + float(i.GPA_8) )
    
    # ถ้า GPAX มีค่ามากกว่า 0.0
    if GPAX > 0.0:
        # loop สำหรับ unit ใน DATA_GPA
        for unit in DATA_GPA:

            # ถ้า GPA ในเทอม 1 ไม่เท่ากับ 0 
            if unit.GPA_1 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 2 ไม่เท่ากับ 0 
            if unit.GPA_2 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1

            # ถ้า GPA ในเทอม 3 ไม่เท่ากับ 0 
            if unit.GPA_3 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 4 ไม่เท่ากับ 0 
            if unit.GPA_4 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 5 ไม่เท่ากับ 0 
            if unit.GPA_5 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 6 ไม่เท่ากับ 0 
            if unit.GPA_6 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 7 ไม่เท่ากับ 0 
            if unit.GPA_7 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
            
            # ถ้า GPA ในเทอม 8 ไม่เท่ากับ 0 
            if unit.GPA_8 != "0" :
                # ให้ COUNT_UNIT บวกเท่ากับ 1
                COUNT_UNIT += 1
    
    # other
    else:
        # ให้ COUNT_UNIT บวกเท่ากับ 1
        COUNT_UNIT += 1

    # เก็บผลหารระหว่าง GPAX กับ COUNT_UNIT ไว้ใน RES_GPAX
    RES_GPAX = float(GPAX) / float(COUNT_UNIT)
    # นำ RES_GPAX มาทำให้เหลือทศนิยม 2 ตำแหน่ง เก็บไว้ใน NEW_GPAX
    NEW_GPAX = '%.2f' % RES_GPAX
    
    # render eightTerm.html แสดงข้อมูลวิชา หน่วยกิต และเกรด ของแต่ละวิชา
    # ที่ได้ทำการคำนวณไว้ พร้อมแสดง GPA ในเทอมนี้ และแสดง GPAX
    return render(request, 'eightTerm.html', {'dataterm8':eighth_dataterm,
                                              'GPARES':DATA_GPA,
                                              'res_GPAX': NEW_GPAX})

# แสดงรูป flow
def picture_of_flow(request):
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
