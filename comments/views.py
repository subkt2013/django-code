from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.shortcuts import redirect
from django.contrib import messages
from .forms import CommentForm
from .models import Comment
 
# Create your views here.
 
# def index(request):
#     return HttpResponse("Hello, world. You're at the comments index.")

#template_name省略できる　https://qiita.com/igm/items/24e9c5431d0e8fba0700
class CommentIndexView(ListView):
  model = Comment
  template_name = 'comments/comment_list.html'
  queryset = Comment.objects.order_by('-updated_at')
  paginate_by = 10

class ShowCommentView(DetailView):
  model = Comment
  template_name = 'comments/comment_detail.html'

class CreateCommentView(CreateView):
  model = Comment
  template_name = 'comments/comment_form.html'
  form_class = CommentForm
  success_url = reverse_lazy('comments:index')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['page_title'] = 'コメントの投稿'
    context['form_name'] = 'コメントの投稿'
    context['button_label'] = 'コメントを投稿する'
    return context

  def form_valid(self, form):
    self.object = comment = form.save()
    messages.success(self.request, 'コメントを投稿しました')
    return redirect(self.get_success_url())

class UpdateCommentView(UpdateView):
    model = Comment
    template_name = 'comments/comment_form.html'
    form_class = CommentForm
    success_url = reverse_lazy('comments:index')

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['page_title'] = 'コメントの更新'
      context['form_name'] = 'コメントの更新'
      context['button_label'] = 'コメントを更新する'
      return context

    def form_valid(self, form):
      self.object = comment = form.save()
      messages.success(self.request, 'コメントを更新しました')
      return redirect(self.get_success_url())


class DeleteCommentView(DeleteView):
    model = Comment
    success_url = reverse_lazy('comments:index')
    template_name = 'comments/comment_confirm_delete.html'
    def delete(self, request, *args, **kwargs):
      self.object = comment = self.get_object()
      comment.delete()
      messages.success(self.request, 'コメントを削除しました')
      return redirect(self.get_success_url())