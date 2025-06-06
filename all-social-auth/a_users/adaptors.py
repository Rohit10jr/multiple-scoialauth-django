from django.shortcuts import resolve_url
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.models import EmailAddress

from django.contrib.auth import get_user_model
User = get_user_model()

class CustomAccoutnAdaptor(DefaultAccountAdapter):
    def get_signup_redirect_url(self, request):
        return resolve_url("profle-onboarding")

class SocialAccountAdaptor(DefaultSocialAccountAdapter):
    def prescoial_login(self, request, sociallogin):
        email = sociallogin.account.extra_data.get("email")

        if not email:
            return 
        
        if not sociallogin.is_existing:
            existing_user = User.objects.filter(email=email).first()
            if existing_user:
                sociallogin.connect(request, existing_user)

        if sociallogin.is_existing:
            user = sociallogin.user
            email_address, created = EmailAddress.objects.get_or_create(user=user, email= email)

            if not email_address.verified:
                email_address.verified =True
                email_address.save()

    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        email = user.email
        email_address, created = EmailAddress.objects.get_or_create(user=user, email=email)
        
        if not email_address.verified:
            email_address.verified =True
            email_address.save()

        return user

