###user profile

def build_profile(first, last, **user_info):
    """building a profile"""
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile('spike', 'spiegel',
                             location='mars',
                             field='bounty hunter')
print(user_profile)