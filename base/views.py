from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Task, Note
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class Weblogin(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class Webregister(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Webregister, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(Webregister, self).get(*args, **kwargs)


class Weblogout(LogoutView):

    def get_next_page(self):
        return reverse_lazy('login')


class Tasklist(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)

        context['search_input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('home')


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['user', 'title', 'description', 'complete']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.assigned_by = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['user', 'title', 'description', 'complete']
    success_url = reverse_lazy('home')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('home')


class Notelist(LoginRequiredMixin, ListView):
    paginate_by = 5
    model = Note
    context_object_name = 'notes'
    template_name = 'base/note_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['notes'] = context['notes'].filter(user=self.request.user)
        context['notes'] = self.model.objects.all()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['notes'] = context['notes'].filter(name__icontains=search_input)

        context['search_input'] = search_input
        return context


class NoteDetail(LoginRequiredMixin, DetailView):
    model = Note
    context_object_name = 'notes'
    success_url = reverse_lazy('note_list')
    template_name = 'base/note_detail.html'


class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['name', 'note']
    success_url = reverse_lazy('note_list')
    template_name = 'base/note_create.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(NoteCreate, self).form_valid(form)


class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    fields = '__all__'
    success_url = reverse_lazy('note_list')
    template_name = 'base/note_delete.html'


class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['name', 'note']
    success_url = reverse_lazy('note_list')
    template_name = 'base/note_update.html'
