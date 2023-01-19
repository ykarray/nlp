import re
chat1='Hello, I am having an issue with my order # 412-8899'
chat2=' I have a problem with my order number 412889912'
chat3='My order 412889912 is having an issue, I was charged 300$ when online it says 280$'
chat4='my email: azer@gmail.com'
pattern = '\d' #one number
matches=re.findall(pattern, chat2)
print('\d ,',matches)
pattern = '\d12' #[any number+12]
matches=re.findall(pattern, chat2)
print('\d12 ,',matches)
pattern = '\d{3}-\d{4}' #[tow numbers]
matches=re.findall(pattern, chat1)
print('\d{3}-\d{4} ,',matches)
pattern = '\d{3}-\d{4}|\d12' #[|mean or]
matches=re.findall(pattern, chat1)
print('\d{3}-\d{4}|\d12 ,',matches)
pattern = '\d12|\d{3}-\d{4}' #[|mean or]
matches=re.findall(pattern, chat1)
print('\d12|\d{3}-\d{4},',matches)

pattern = '\d{3}\$' 
matches=re.findall(pattern, chat3)
print('\d{3}\$ ,',matches)
pattern = '[a-z0-9A-Z_]*@[a-z0-9A-Z_]*.[a-z0-9A-Z_]*' #get the email
matches=re.findall(pattern, chat4)
print('[a-z0-9A-Z_]*@[a-z0-9A-Z_]*.[a-z0-9A-Z_]* ,',matches)
pattern = 'order[^\d]*([0-9]*)' #extracting the order number using ()
matches=re.findall(pattern, chat3)
print('order[^\d]*([0-9]*) ,',matches)

