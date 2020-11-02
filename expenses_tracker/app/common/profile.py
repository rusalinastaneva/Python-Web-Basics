from app.models import Profile


def get_profile():
    profile = Profile.objects.all()[0]
    return profile
