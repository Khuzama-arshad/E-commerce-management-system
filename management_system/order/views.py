from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import CheckoutForm
from .models import Order, OrderItem
from product.models import Product

# Create your views here.
@login_required
def checkout(request):
    cart = request.session.get("cart", {})

    if not cart:
        messages.warning(request, "Your cart is empty.")
        return redirect("cart")

    if request.method == "POST":
        form = CheckoutForm(request.POST)

        if form.is_valid():

            order = Order.objects.create(
                user=request.user,
                user_name=form.cleaned_data["user_name"],
                email=form.cleaned_data["email"],
                phone=form.cleaned_data["phone"],
                address=form.cleaned_data["address"],
                city=form.cleaned_data["city"],
                status="pending",
            )

            for product_id, item in cart.items():
                product = get_object_or_404(Product, id=product_id)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item["quantity"],
                )

            order.calculate_total_price()
            order.save()

            request.session["cart"] = {}
            request.session.modified = True

            return redirect("order_confirmation", order_id=order.id)

    else:
        form = CheckoutForm()

    total = sum(item["price"] * item["quantity"] for item in cart.values())

    context = {
        "form": form,
        "cart_items": cart,
        "total": total,
    }

    return render(request, "order/order_checkout.html", context)

@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order/order_confirmation.html', {'order': order})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order/order_detail.html', {'order': order})

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'order/order_list.html', {'orders': orders})