from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView , DetailView
from .models import Post
from .models import Post1
from .models import Dish
from .models import Menu1
from .models import Menu2

# Create your views here.
rests = [

	{
		'Name': 'Phillys',
		'Location': 'DHA sector Z',
		'Cuisines' : 'FASTfood',
		'Price Range' : '1',
		'Ratings' :'Very Good',

		
	},

	{

		'Name': 'Jammin Java',
		'Location':'LUMS',
		'Cuisines' : 'FASTfood',
		'Price Range' : '1',
		'Ratings' :'Very Good',
		
	}


]

def home(request):
	
	return render(request, 'blog/home.html') 

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'}) 

def login(request):
	return render(request, 'blog/login.html', {'title': 'Login'})

#def restaurants(request):
#	context = {
#		'posts': posts
#	}
#	return render(request, 'blog/restaurants.html', context)


def restaurants(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/restaurants.html', context)

def restaurants1(request):
	context1 = {
		'rests': Post1.objects.all()
	}
	return render(request, 'blog/tester.html', context1)
def menu(request):
	context2={
	'dishes':Menu2.objects.all(),
	'rests':Post1.objects.all()
	}
	

	return render(request, 'blog/menu.html',context2)
def menuO(request):
	context2={
	'dishes':Menu2.objects.all(),
	'rests':Post1.objects.all()
	}
	

	return render(request, 'blog/menuO.html',context2)
def menuH(request):
	context2={
	'dishes':Menu2.objects.all(),
	'rests':Post1.objects.all()
	}
	

	return render(request, 'blog/menuH.html',context2)
def menuS(request):
	context2={
	'dishes':Menu2.objects.all(),
	'rests':Post1.objects.all()
	}
	

	return render(request, 'blog/menuS.html',context2)
def menuK(request):
	context2={
	'dishes':Menu2.objects.all(),
	'rests':Post1.objects.all()
	}
	

	return render(request, 'blog/menuK.html',context2)
def menuD(request):
	context2={
	'dishes':Menu2.objects.all(),
	'rests':Post1.objects.all()
	}
	

	return render(request, 'blog/menuD.html',context2)

def menuI(request):
	context2={
	'dishes':Menu2.objects.all(),
	'rests':Post1.objects.all()
	}
	

	return render(request, 'blog/menuI.html',context2)

def menuboot(request):
	context2={
	'dishes':Menu1.objects.all(),
	'rests':Post1.objects.all()
	}
	

	return render(request, 'blog/menubootstrap.html',context2)


class PostListView(ListView):
	model=Post
	template_name='blog/restaurants.html'
	context_object_name='posts'
	paginate_by=7

class PostDetailView(DetailView):
	model=Post

class PostListView1(ListView):
	model=Post1
	template_name='blog/tester.html'
	context_object_name='rests'
	paginate_by=7

class PostDetailView1(DetailView):
	model=Post1
	template_name='blog/rest_detail.html'



