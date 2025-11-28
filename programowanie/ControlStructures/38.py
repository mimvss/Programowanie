# Write a program that checks whether a given person is a good influencer, that is, whether the person has at least two of the following
# accounts: Facebook, Twitter or Instagram. Use logical type variables: facebook, twitter, instagram, the value of which indicates
# whether the person has an account on the social networking site

answer_f = input("Does influencer has a facebook account? (Y/N): ").lower()
if answer_f == 'y':
    Facebook = True
else:
    Facebook = False

answer_i = input("Does influencer has an Instagram account? (Y/N): ").lower()
if answer_i == 'y':
    Instagram = True
else:
    Instagram = False

answer_t = input("Does influencer has a Twitter account? (Y/N): ").lower()
if answer_t == 'y':
    Twitter = True
else:
    Twitter = False

count = Facebook + Twitter + Instagram
if count >= 2:
    print(f'Facebook: {Facebook}')
    print(f'Instagram: {Instagram}')
    print(f'Twitter: {Twitter}')
    print('Good influencer')
else:
    print(f'Facebook: {Facebook}')
    print(f'Instagram: {Instagram}')
    print(f'Twitter: {Twitter}')
    print('Bad influencer')