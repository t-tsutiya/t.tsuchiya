from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from.forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
from .forms import GPTQuestionForm
from django.urls import reverse_lazy
from openai import OpenAI


class ContactView(FormView):

    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('koukaapp:contact')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ: {}'.format(title)
        message = \
            '送信者名: {0}\n メールアドレス: {1}\n タイトル: {2}\n メッセージ: {3}'\
            .format(name,email,title,message)
        from_email = 'taichiearth759@gmail.com'    #admin@example.com
        to_list = ['taichiearth759@gmail.com']
        message = EmailMessage(subject=subject,body=message,from_email=from_email,to=to_list,)
        message.send()
        messages.success(self.request, 'お問い合わせは正常に送信されました。')
        return super().form_valid(form)

class IndexView(TemplateView):
    template_name = 'index.html'

class Index2View(TemplateView):
    template_name = 'index2.html'

class Index3View(TemplateView):
    template_name = 'index3.html'

class HeartView(FormView):
    name = 'add'

class GPTView(FormView):
    template_name = 'gpt.html'
    form_class = GPTQuestionForm
    success_url= reverse_lazy('koukaapp.gpttest')

    def post(self, request, *args, **kwargs):
        
        client = OpenAI(api_key = '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') #インスタンス化
        form_data = request.POST.get('question')

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",    #使うモデルの指定
        messages=[
            {"role": "system", "content": "あなたは標準的な会話ができるアシスタントです"},
            {"role": "user", "content": form_data}
        ]
        )

        
        return render(request,'gpt.html', {'answer_data':completion.choices[0].message.content,
                                           'form': self.form_class})
    

from django.views.generic import ListView
from .models import BlogPost
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'orderby_records'
    queryset = BlogPost.objects.order_by('posted_at')