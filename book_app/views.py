from django.shortcuts import render , redirect , get_object_or_404
from django.views.generic  import CreateView,UpdateView,DeleteView,ListView
from .models import Post_data , User ,Author_Profile ,Reader_Profile , Comment
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import author_data ,Reader_data
from . forms import UpdateUserForm,UpdateProfileForm ,Reader_UpdateUserForm,Reader_UpdateProfileForm ,CommentForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .decorators import author_required,reader_required
from django.utils.decorators import method_decorator

# Create your views here.
def Home(request):
    return render(request,'book_app/home.html')

@login_required(login_url='login')
def single_post(request,pk):
    data = Post_data.objects.filter(id=pk)
    context = {'data':data,'legend':'Updating the Data'}
    return render(request,'book_app/Spost.html',context)

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post_data
    login_url = '/Author/login/'
    fields = ['title','category','Review']
    template_name = 'book_app/post_form.html'

    # def form_valid(self,form):
    #     form.instance.date= self.time.time()
    #     return super().form_valid(form)

    # def form_valid(self,form):
    #     form.instance.author= self.request.user
    #     return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post_data
    login_url = '/Author/login/'
    context_object_name = 'data'
    fields = ['title','category','Review']
    template_name = 'book_app/post_update_form.html'

    def form_valid(self,form):
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post_data
    login_url = '/Author/login/'
    success_url = '/CreatePost/'

@method_decorator([login_required, author_required], name='dispatch')
class PostListView(LoginRequiredMixin,ListView):
    model = Post_data
    login_url = '/Author/login/'
    context_object_name = 'data'
    template_name = 'book_app/postjobs.html'
    # ordering = ['-date1']
    paginate_by = 4



#----------------------------------------------------------------------------------------------------------------------#
#Login and Logout and Registration
#----------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def Author_profile(request):
    return render(request, 'book_app/profile.html')

def Author_login(request):

    next=''
    if request.GET:
        next = request.GET['next']

    if request.method == 'POST':
        user1 = request.POST.get('username')
        pass1 = request.POST.get('password')

        user = authenticate(request,username=user1,password=pass1)

        if user is not None:
            login(request,user)

            if next == "":
                return redirect('list_post')
            else :
                return redirect(next)

    form = AuthenticationForm()
    context={'form':form,'legend' : "Login NOW" }
    return render(request,'book_app/login.html',context)


def register(request):
    try :
        if request.method=='POST':
            form = author_data(request.POST)
            if form.is_valid():
                form.save()
                user1 = form.cleaned_data.get("username")
                messages.success(request, f"Account is  created for {user1}")
                return redirect("login")
            else :
                form = author_data()
                context={'form':form,'legend':'Invalid Fields'}
                return render(request, 'book_app/signup.html', context)

        form = author_data()
        context = {'form': form, 'legend' : "Register Today"}

        return render(request, 'book_app/signup.html', context )


    except User.profile.RelatedObjectDoesNotExist:
        Author_Profile.objects.create(user=request.user)

    except Exception as e:
        print(e , type(e))

#----------------------------------------------------------------------------------------------------------------------#
#profile Updation
#----------------------------------------------------------------------------------------------------------------------#

@login_required(login_url='login')
def Author_upprofileup(request):
    try :
        if request.method == 'POST':
            user_form = UpdateUserForm(request.POST, instance=request.user)
            profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save(commit=True)
                profile_form.save(commit=True)
                messages.success(request, 'Your profile is updated successfully')
                return redirect(to='profile')
        else:
            user_form = UpdateUserForm(instance=request.user)
            profile_form = UpdateProfileForm(instance=request.user.profile)

        return render(request, 'book_app/updateprofile.html', {'user_form': user_form, 'profile_form': profile_form})

    except User.profile.RelatedObjectDoesNotExist:
        Author_Profile.objects.create(user=request.user)

    except Exception as e:
        print(e, type(e))

@login_required(login_url='login')
def MyPosts(request):
    My_post_data = Post_data.objects.filter(author=request.user)

    if My_post_data.exists():
        value="1"
    else :
        empty_message = "CREATE YOUR FIRST REVIEW POST"
        value = "2"

    context = {'My_post_data': My_post_data , "value":value }
    return render(request,"book_app/Myposts.html",context)
#----------------------------------------------------------------------------------------------------------------------#
#Reader , Signup , login , updation
#----------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def Reader_profile(request):
    return render(request, 'book_app/Reader/profile.html')

def Reader_login(request):

    next=''
    if request.GET:
        next = request.GET['next']

    if request.method == 'POST':
        user1 = request.POST.get('username')
        pass1 = request.POST.get('password')

        user = authenticate(request,username=user1,password=pass1)

        if user is not None:
            login(request,user)

            if next == "":
                return redirect('Reader_list_post')
            else :
                return redirect(next)

    form = AuthenticationForm()
    context={'form':form,'legend' : "LOGIN NOW" }
    return render(request,'book_app/Reader/login.html',context)


def Reader_register(request):
    try :
        if request.method=='POST':
            form = Reader_data(request.POST)
            if form.is_valid():
                form.save()
                user1 = form.cleaned_data.get("username")
                messages.success(request, f"Account is  created for {user1}")
                return redirect("Reader_login")
            else :
                form = Reader_data()
                context={'form':form,'legend':'Invalid Fields'}
                return render(request, 'book_app/Reader/signup.html', context)

        form = Reader_data()
        context = {'form': form, 'legend' : "Register Today"}

        return render(request, 'book_app/Reader/signup.html', context )


    except User.profile.RelatedObjectDoesNotExist:
        Reader_Profile.objects.create(user=request.user)

    except Exception as e:
        print(e , type(e))

@login_required(login_url='login')
def Reader_upprofileup(request):
    try :
        if request.method == 'POST':
            user_form = Reader_UpdateUserForm(request.POST, instance=request.user)
            profile_form = Reader_UpdateProfileForm(request.POST, request.FILES,
                                                       instance=request.user.Reader_profile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save(commit=True)
                profile_form.save(commit=True)
                messages.success(request, 'Your profile is updated successfully')
                return redirect(to='Reader_profile')
        else:
            user_form = Reader_UpdateUserForm(instance=request.user)
            profile_form = Reader_UpdateProfileForm(instance=request.user.Reader_profile)

        return render(request, 'book_app/Reader/updateprofile.html', {'user_form': user_form, 'profile_form': profile_form})

    except User.profile.RelatedObjectDoesNotExist:
        Reader_Profile.objects.create(user=request.user)

    except Exception as e:
        print(e, type(e))

@login_required(login_url='login')
def Reader_single_post(request,pk):
    data = Post_data.objects.filter(id=pk)
    context = {'data':data,'legend':'Updating the Data'}
    return render(request,'book_app/Reader/Spost.html',context)

@method_decorator([login_required, reader_required], name='dispatch')
class Reader_PostListView(LoginRequiredMixin,ListView):
    model = Post_data
    login_url = '/Reader/login/'
    context_object_name = 'data'
    template_name = 'book_app/Reader/postjobs.html'
    # ordering = ['-date1']
    paginate_by = 4

#----------------------------------------------------------------------------------------------------------------------#
#Comment for each Posts
#----------------------------------------------------------------------------------------------------------------------#

@login_required(login_url='login')
def Comment(request,pk,*args, **kwargs):
    form = CommentForm()
    post = Post_data.objects.filter(id=pk)[0]
    #comment = post.comments.all()
    if request.method=='POST':
        form = CommentForm(request.POST,request.FILES )
        if form.is_valid():
            mark1=form.save(commit=False)
            mark1.post = get_object_or_404(Post_data,id=pk)
            mark1.author =request.user
            form.save()


    context = {'form': form, 'post': post}
    return render(request,'book_app/Reader/post_comment.html', context)

def Comment_Author(request,pk,*args, **kwargs):
    form = CommentForm()
    post = Post_data.objects.filter(id=pk)[0]
    #comment = post.comments.all()
    if request.method=='POST':
        form = CommentForm(request.POST,request.FILES )
        if form.is_valid():
            mark1=form.save(commit=False)
            mark1.post = get_object_or_404(Post_data,id=pk)
            mark1.author =request.user
            form.save()


    context = {'form': form, 'post': post}
    return render(request,'book_app/post_comment.html', context)