from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name="login.html"
    success_url=reverse_lazy("inicio")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy("inicio"))
        return super().dispatch(request, *args, **kwargs)
    

    def form_valid(self,form):
        login(self.request,form.get_user())
        return HttpResponseRedirect(self.success_url)

class RegisterView(FormView):
    form_class = UserCreationForm
    template_name="register.html"
    success_url=reverse_lazy("inicio")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy("inicio"))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
      form.save()
      return HttpResponseRedirect(reverse_lazy("login"))
