from .models import Shortener
import random 
from string import ascii_letters


def checker(randon_link):
    return Shortener.objects.filter(shortened_link=random_link)









def redirector(request,str):
    connect_url='localhost:8000/'+str
    try:
        redirect_url = Shortener.objects.filter(shortened_link=connect_url).values('original_link').first()
        print(redirect_url)
        # original_link= redirect_url['original_link']
        print(redirect_url['original_link'])
    except:
        pass
    # return HttpResponse(original_link)
    return HttpResponse('hi')




















# def random_link():
#         host='www.oli.ve'
#         random_links = host+'/'+''.join(random.sample(ascii_letters,6))
#         while True:
#             if random_links in Shortener.objects.filter(shortened_link=random_links):
#                 random_links = host+'/'+''.join(random.sample(ascii_letters,6))
#             else:
#                 break 
#         return random_links
    








# ---------------Test---------------------------

# return_list=[]

# for i in range(10000000):
#     return_link=random_link('google.com',host,database)
#     return_list.append(return_link)

# return_set=set(return_list)
# print('the length of original list:' ,len(return_list))
# print('the length of original set:' ,len(return_set))

