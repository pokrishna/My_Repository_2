from django.shortcuts import render,get_object_or_404
from testapp.models import Post,Comments
from django.http import HttpResponse,Http404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
from django.core.mail import send_mail
from .forms import EmailSendForm,CommentForm
from django.views.generic import ListView
class PostListView(ListView):
    model=Post
    paginate_by=2

def post_list_view(request):
    post=Post.objects.all()
    paginator=Paginator(post,3)
    page_number=request.GET.get('page')
    try:
        post=paginator.page(page_number)
    except PageNotAnInteger:
        post=paginator.page(1)
    except EmptyPage:
        post=paginator.page(paginator.num_pages)
    return render(request,'testapp/post_list.html',{'post_list':post})


def post_detail_view(request,year,month,day,post):
    print("it is in post_detal_view")
    try:
        post=get_object_or_404(Post,slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
    except Http404:
        return HttpResponse("<h1>Post is in Draft ,Not yet Published</h1>")
    if post != None:
        print("it is valid post")
    else:
        print("not a valid post")
    return render(request,'testapp/post_details_views.html',{'post':post})

def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent=False
    if request.method=="POST":
        form=EmailSendForm(reqest.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='{}({}) recommands you to read "{}"'.format(cd['name'],cd['email'],post.title)
            post_url=request.bild_absolute_url(post.get_absolute_url())
            message='Read Post At:\n {} \n\n{}\'s comments:\n{}'.format(post_url,cd['name'],cd['comments'])
            send_mail(subject,message,'jap.krishna@gmail.com',[cd['to']])
            sent=True
    else:
        form=EmailSendForm()
    return render(request,'testapp/sharebymail.html',{'form':form,'post':post,'sent':sent})

def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            print(new_comment.body)
            new_comment.post=post
            new_comment.save()
            print(new_comment)
            csubmit=True
    else:
        form=CommentForm()
    return render(request,'testapp/post_details_views.html',{'post':post,'form':form,'csubmit':csubmit,'comments':comments})
