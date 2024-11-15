import instaloader

ig=instaloader.Instaloader()

profile=instaloader.Profile.from_username(ig.context , 'priya_raviraina')

print(profile.business_category_name)
print(profile.username)
print(profile.blocked_by_viewer)
print(profile.followed_by_viewer)
print(profile.followers)
print(profile.get_followees)
print(profile.is_private)
print(profile.followees)
print(profile.is_verified)
print(profile.external_url)
print(profile.full_name)
print(profile.biography_hashtags)
print(profile.mediacount)
print(profile.userid)
profiled = profile.get_followees()
print(profiled)

print(profile.get_followers())



# profile_pic_url = profile.get_profile_pic_url()
# print(profile_pic_url)
# print(profile.biography)


# similar_accounts_generator = profile.get_similar_accounts()

# # Iterate over the similar accounts
# for similar_account in similar_accounts_generator:
#     print(similar_account)