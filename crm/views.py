from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.shortcuts import render

from .models import Customer

from django.views.generic import ListView, DetailView, TemplateView, DeleteView, CreateView, UpdateView

#home----
class IndexView(TemplateView):
    template_name = 'crm/index.html'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            ctx["recent_customers"] = (
                Customer.objects.filter(owner=self.request.user)
                .order_by("-created_at")[:5]
            )
        else:
            ctx["recent_customers"] = []
        return ctx
#list----
class CustomerListView(ListView):
    model = Customer
    template_name = 'crm/customer_list.html'
    context_object_name = 'customers'
    paginate_by = 10

    def get_queryset(self):
        return Customer.objects.filter(is_active=True).order_by('-created_at')

#detail----
class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'crm/customer_detail.html'
    context_object_name = 'customer'

#delete-----
class CustomerDeleteView(DeleteView):
    model = Customer
    templatename = 'crm/customer_delete.html'
    success_url = reverse_lazy('crm:customer_list')

    # 自分のレコードだけ削除できるように制限  #ここではじかれた時の処理を追加する
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
    
#create----
class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'crm/customer_create.html'
    fields = ('name','company','email','phone','status','owner','note',)
    success_url = reverse_lazy('crm:customer_list')

#update----
class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'crm/customer_update.html'
    fields = ('name','company','email','phone','status','owner','note',)
    success_url = reverse_lazy('crm:customer_list')
