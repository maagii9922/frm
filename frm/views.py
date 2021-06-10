from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Hereglegch
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .forms import NameForm,ContactForm
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, get_connection



@csrf_exempt
def contact(request,pk):
    # submitted = False
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #          cd = form.cleaned_data
    #          # assert False
    #     # return HttpResponseRedirect('/thanks?submitted=True')
    #     return HttpResponseRedirect('/contact?submitted=True')
    # else:
    #     form = ContactForm()
    #     if 'submitted' in request.GET:
    #          submitted = True
 
    # return render(request,'index.html',{'form': form, 'submitted': submitted})

    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            blog = get_object_or_404(Hereglegch, pk=pk)
            Hereglegch.objects.create(
            #    blog = blog,
            #    name = cd.name,
            #    code = cd.code
            text=request.POST[]
           )
             # assert False
            # con = get_connection('django.core.mail.backends.console.EmailBackend')
            # send_mail(
            #      cd['subject'],
            #      cd['message'],
            #      cd.get('email', 'noreply@example.com'),
            #      ['siteowner@example.com'],
            #      connection=con
            #  )
            # return HttpResponseRedirect('/thanks?submitted=True')
    else:
         form = ContactForm()
         if 'submitted' in request.GET:
             submitted = True
 
    return render(request, 'index.html', {'form': form, 'submitted': submitted})

def get_name(request):
    if request.method == 'GET':
        dd =  request.session.get('err_msg')
        ee =  request.session.get('formData') 
        print(ee)
        form = NameForm()  
        if (ee is not None):
            form = NameForm({"your_name": ee + "asdf"}) 
        return render(request, 'index.html', {'form': form, 'err_msg':dd})
    elif request.method == 'POST':     
        # print(request.POST)   
        # print(request.POST['your_name'])
        # print(request.POST['your_name1'])
        # print(request.POST['your_name2'])
        # print(request.POST['your_name3'])
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponse('/thanks/')
            # return HttpResponseRedirect('/get_name/')\
            # print(form.cleaned_data['your_name'])
            # request.session['err_msg'] = "aldaaa"
            # request.session['formData'] = form.cleaned_data['your_name']
            # # form.err_msg = "asdfads"
            # return HttpResponseRedirect('/get_name/')\

def thanks(request):

    return HttpResponse('thanks')


# # def index(request):
# #     latest_question_list = Question.objects.order_by('-pub_date')[:5]
# #     output = ', '.join([q.question_text for q in latest_question_list])
# #     return HttpResponse(output)

# # def index(request):
# #     latest_question_list = Question.objects.order_by('-pub_date')[:5]
# #     template = loader.get_template('index.html')
# #     context = {
# #         'latest_question_list': latest_question_list,
# #     }
# #     return HttpResponse(template.render(context, request))

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'detail.html', {'question': question})

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'index.html', context)

# # def detail(request, question_id):
# #     return HttpResponse("You're looking at question %s." % question_id)

# # def results(request, question_id):
# #     response = "You're looking at the results of question %s."
# #     return HttpResponse(response % question_id)


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'results.html', {'question': question})

# # def vote(request, question_id):
# #     return HttpResponse("You're voting on question %s." % question_id)
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('results', args=(question.id,)))