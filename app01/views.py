from django.shortcuts import HttpResponse, render,redirect


def login(request):
    error_msg = ""
    if request.method == "POST":
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        print(email, password)
        if email == "333@qq.com" and password == "123":
            return redirect("http://www.163.com")
        else:
            error_msg = "邮箱或密码错误"
    return render(request, "login.html", {"error": error_msg})