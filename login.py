from django.contrib.auth import authenticate, login, logout

user = User.objects.filter(email=email, is_active=True).first()

if user:
    utilisateur_auth = authenticate(username=user.username, password=password)

    if utilisateur_auth:
        login(request, utilisateur_auth)

        redirect("/")
    else:
        message = "Vos identifiants ne sont pas correctes."
