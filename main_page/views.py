from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Category, Products, Cart
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .handlers import bot


class CustomLoginView(LoginView):
     template_name = 'registration/login.html'
     redirect_authenticated_user = True
     def get_success_url(self):
          return reverse_lazy('main_page')
# Create your views here.

# def login_page(request):

def main_page(request):
     # собираем все названия продуктов
     product_info=Products.objects.all()
     product_name=[i.product_name for i in product_info]

     # собираем названия категорий
     category_info=Category.objects.all()


     context = {'products': product_info, 'categories': category_info}
     return render(request,'index.html', context)
def get_full_product(request, pk):
     product= Products.objects.get(id=pk)

     context={'product': product}
     return render(request,'exact_product.html',context)
def get_full_category(request, pk):
     category= Category.objects.get(id=pk)
     products=Products.objects.filter(category_name=category)
     context={'products': products}
     return render(request,'exact_category.html',context)
def search_exact_product(request):
     if request.method=='POST':
          get_product=request.POST.get('search_product')

          try:
               exact_product=Products.objects.get(product_name__icontains=get_product)
               return redirect(f'product/{exact_product.id}')

          except:
               return redirect('/')


def add_products_to_user_cart(request, pk):
     if request.method=='POST':
          checker = Products.objects.get(id=pk)

          if checker.product_amount >= int(request.POST.get('pr_count')):
               Cart.objects.create(user_id=request.user.id,
                                   user_product=checker,
                                   user_cart_amount=int(request.POST.get('pr_count'))).save()

               return redirect('/')
          else:
               return redirect(f'/product/{checker.id}')
def user_cart(request):
     cart=Cart.objects.filter(user_id=request.user.id)

     if request.method == 'POST':
          main_text = 'Новый заказ\n\n'
          for i in cart:
               main_text += f'Товар: {i.user_product}\n'\
                            f'Кол-во: {i.user_cart_amount}'
               bot.send_message(142089691, main_text)
               cart.delete()
               return redirect('/')


     return render(request, 'user_cart.html', {'cart': cart})

def delete_exact_user_cart(request, pk):
     product_to_delete=Products.objects.get(id=pk)

     Cart.objects.filter(user_id=request.user.id,
                                        user_product=product_to_delete).delete()

     return redirect('/user_cart')

# def order_user_product(request,models):
#      user_product= models.Cart.objects.filter(user_id=request.user.id)
#      full_order_message=f'Новый заказ:\n\n От {request.user}\n'
#      total_price=0
#      if user_product:
#           for product in user_product:
#                full_order_message +=f'\n{product.user_product}:{product.user_product_amount}шт'
#                total_price +=int(product.user_product_amount)*float(product.user_product.product_price)
#      bot.send_message(....)
#
#      models.Cart.objects.all().delete()
#      return redirect('/products')
