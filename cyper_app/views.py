from django.shortcuts import render
from django.db import connection
from django.views.decorators.csrf import csrf_exempt


# الفنشكن المسؤولة على صفحة الترحيب بالمستخدمين
def index(request):
    return render(request, "cyper_app/index.html")


# xss الفنكشن المسؤولة عن ترجيع صفحة ال
def xss_vulnerable(request):
    name = request.GET.get("name", "")
    return render(request, "cyper_app/xss.html", {"name": name})


# sql injection الفنكشن المسؤولة عن ترجيع صفحة ال
def sql_injection(request):
    username = request.GET.get("username", "")
    if username:
        if username.upper().find("DROP") >= 1:
            return render(
                request,
                "cyper_app/sql_injection.html",
                {
                    "message": "مش قلنا ما تجرباش امر الدروب ضروري ما نطلعو رسالة ولا شني :) "
                },
            )
    with connection.cursor() as cursor:
        try:

            cursor.execute(
                f"SELECT username,user_pic FROM cyper_app_user WHERE username = '{username}' "
            )
            result = cursor.fetchall()
        except:
            return render(
                request,
                "cyper_app/sql_injection.html",
                {"message": "تأكد من صحة الكود ال SQL "},
            )
    # Here use ORM to prevent SQL Injection
    # result = User.objects.filter(username__exact=username)
    return render(request, "cyper_app/sql_injection.html", {"users": result})


# CSRF هذي الفنكشن المسؤولة عن صفحة
@csrf_exempt
def csrf_vulnerable(request):
    if request.method == "POST":
        new_password = request.POST.get("new_password", "")
        # Update user's password without proper CSRF protection
        # This is vulnerable to CSRF attacks
        return render(request, "cyper_app/csrf.html", {"message": "Password updated"})
    return render(request, "cyper_app/csrf.html")


# dosهذي الفنشكن المسؤولة عن الثغرة ال
def dos_vulnerable(request):
    # This view is vulnerable to DoS attacks as it performs a computationally expensive operation
    n = int(request.GET.get("n", 10))
    result = 10
    # هنا نديرو في عملية جمع لجميع الاعداد من 0 لعند الرقم الي بدخله المستخدم
    # :) عطلتها باش لما نرفعه على السيرفر ما تقربعونيش
    # result = sum(i for i in range(n))
    # عندكم  local  جربوها

    return render(
        request,
        "cyper_app/dos.html",
        {"result": result, "message": "لرفعه على السيرفر End-point تم تعطيل هذه "},
    )
