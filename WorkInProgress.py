#6.14
###
#
facebook = input('Do you have facebook? (True/False): ')
twitter = input('Do you have twitter? (True/False): ')
instagram = input('Do you have instagram? (True/False): ')
if int(facebook == True) + int(twitter == True) + int(instagram == True) >= 2:
    print('You are a good influencer!')