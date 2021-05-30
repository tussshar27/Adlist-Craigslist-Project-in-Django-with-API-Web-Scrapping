import requests
from django.shortcuts import render
from requests.compat import quote_plus  #insert percentageNumber automatically between the space of two words in url. eg, 'python tutor' = 'python+tutor'.
from bs4 import BeautifulSoup
from . import models


BASE_CRAIGSLIST_URL = 'https://mumbai.craigslist.org/d/for-sale/search/sss?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'

# Create your views here.
def home(request):
    return render(request,'my_app/home.html')

def new_search(request):
    search = request.POST.get('search')
    # print(quote_plus(search))
    models.Search.objects.create(search=search) #shortcut method for saving in database of user input from front-end
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))  #format means insertion
    print(final_url)
    response = requests.get(final_url)
    data0 = response.text
    soup = BeautifulSoup(data0, 'html.parser')

    post_listings = soup.find_all('li', {'class': 'result-row'})        #retriving all the lists
   
    final_postings = []  #initializing empty list
    
    # post_title = post_listings[0].find(class_= 'result-title').text     #retriving 1st list title
    # post_url = post_listings[0].find('a').get('href')       #retriving 1st list href 
    # post_price = post_listings[0].find(class_= 'result-price').text     #retriving 1st list price #found the class name 'result-price' from the main website.
    
    for post in post_listings:
        post_title = post.find(class_= 'result-title').text    
        post_url = post.find('a').get('href')      
        if  post.find(class_= 'result-price').text: #if price is present in that list
            post_price = post.find(class_= 'result-price').text     #found the class name 'result-price' from the main website.
        else:   #if price is not present in that list
            post_price = 'N/A'

        if post.find(class_ ='result-image').get('data-ids'):
            post_image_id = post.find(class_ ='result-image').get('data-ids').split(',')[0].split(':')[1]   #0 means getting the 1st pic id of each particular list data, 1 means getting the 2nd data from list
            post_image_url = BASE_IMAGE_URL.format(post_image_id)   #format means insertion
            print(post_image_url)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'

        final_postings.append((post_title, post_url, post_price, post_image_url))

    # print(post_title)
    # print(post_url)
    # print(post_price)
    
    data = {
        'search': search,
        'final_postings': final_postings,
    }
    return render(request, 'my_app/new_search.html', data)

def about(request):
    return render(request,'my_app/about.html')

def contact(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    desc = request.POST.get('desc')

    models.Contact.objects.create(username=username, email=email, subject=subject, desc=desc) #shortcut method for saving in database of user input from front-end

    return render(request,'my_app/contact.html')