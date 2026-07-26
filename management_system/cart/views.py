from django.shortcuts import get_object_or_404, redirect , render
from product.models import Product
# Create your views here.
# def Cart(request):
#     cart_items = request.session.get("cart", {})
#     subtotal = sum(item["price"] * item["quantity"] for item in cart_items.values())
#     return render(request, 'cart.html', {'cart_items': cart_items, 'subtotal': subtotal})
def Cart(request):
    cart_items = request.session.get("cart", {})

    subtotal = 0

    for item in cart_items.values():
        item["price"] = float(item["price"])  # Convert price to float
        item["total"] = item["price"] * item["quantity"]
        subtotal += item["total"]

    return render(request, "cart.html", {
        "cart_items": cart_items,
        "subtotal": subtotal,
    })

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Get cart from session
    cart = request.session.get("cart", {})

    product_id = str(product.id)

    if product_id in cart:
        cart[product_id]["quantity"] += 1
    else:
        cart[product_id] = {
            "name": product.name,
            "price": float(product.price),
            "image": product.image.url,
            "quantity": 1,
        }

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")