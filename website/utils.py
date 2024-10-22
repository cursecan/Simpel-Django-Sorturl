from django.utils.crypto import get_random_string


from string import ascii_letters



def generate_code(instance, length=6, chars=ascii_letters):
    new_code = get_random_string(length, chars)

    if (instance.__class__.objects.filter(code=new_code).exists()):
        return generate_code(instance)
    
    return new_code