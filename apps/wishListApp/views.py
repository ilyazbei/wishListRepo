from django.shortcuts import render, redirect
from django.contrib import messages
from ..loginApp.models import User
from .models import Wishlist


# Create your views here.
def index(request):

    if not 'user_id' in request.session:
        messages.error(request, 'Must be logged in to continue!')
        return redirect('users:index')

    user = User.objects.get(id=request.session['user_id'])
    context = {
        'wishList': user.wishlists.all(),
        'othersWishlist': Wishlist.objects.exclude(users=user),
        'user': user
    }
    return render(request, "wishListApp/index.html", context)

def create(request):
    return render(request, "wishListApp/create.html")

def newItem(request):
    if request.method == "POST":
        userID = request.session['user_id']
        responseFromModel = Wishlist.objects.newItem(request.POST, userID)

        if responseFromModel['status']:
            # created a user, send to success page

            return redirect('wishList:index')
        # failed validations send messages to client
        else:
            for error in responseFromModel['errors']:
                messages.error(request, error)
            return redirect('wishList:index')

    return redirect("wishList:index")

def show(request, id):
    wish_id = id
    context = {
        "itemInfo" : Wishlist.objects.get(id=id),
        "otherUsersList" : User.objects.filter(wishlists__id=wish_id)
    }
    return render(request, "wishListApp/show.html", context)

def delete(request, id):
    if request.method == "POST":
        Wishlist.objects.get(id=id).delete()
    return redirect("wishList:index")

def add(request, id):
    wish = Wishlist.objects.get(id=request.POST['wish_id'])
    user = User.objects.get(id=request.session['user_id'])
    user.wishlists.add(wish)
    return redirect("wishList:index")

def remove(request, id):
    if request.method == "POST":
        user = User.objects.get(id=request.session['user_id'])
        item = Wishlist.objects.get(id=id)
        item.users.remove(user)
    return redirect("wishList:index")
