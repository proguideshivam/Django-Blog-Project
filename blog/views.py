from django.shortcuts import render


posts = [
	{
		'authors' : 'Shivam Kushwaha',
		'Title' : 'This is first prost.',
		'Descreption' : 'This IS frist post descreption.',
		'post_date' : '2 Aug 2023',
	},
	{
		'authors' : 'Santosh Kushwaha',
		'Title' : 'This is Second prost.',
		'Descreption' : 'This IS Second post descreption.',
		'post_date' : '2 Sep 2023',
	},
	{
		'authors' : 'Aman Kushwaha',
		'Title' : 'This is Third prost.',
		'Descreption' : 'This IS Third post descreption.',
		'post_date' : '2 Aug 2023',
	}
]
def home(request):
	context = {
		'posts' :posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'about'})
