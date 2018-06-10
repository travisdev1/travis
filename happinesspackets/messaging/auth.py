from mozilla_django_oidc.auth import OIDCAuthenticationBackend

class OIDC(OIDCAuthenticationBackend):
    def create_user(self, claims):
        user = super(MyOIDCAB, self).create_user(claims)
        user.first_name = claims.get('name', '')
        user.username = claims.get('nickname', '')
        user.email = claims.get('email', '')
        user.save()
        return user
