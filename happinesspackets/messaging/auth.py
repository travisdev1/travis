from mozilla_django_oidc.auth import OIDCAuthenticationBackend

class OIDC(OIDCAuthenticationBackend):
    def create_user(self, claims):
        user = super(OIDC, self).create_user(claims)
        user.username = claims.get('nickname', '')
        user.email = claims.get('email', '')
        try:
            user.first_name = claims.get('name', '')
        except:
            user.first_name = user.username
        user.save()
        return user
