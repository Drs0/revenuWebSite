from django.contrib.auth.base_user import BaseUserManager

class mailerManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("You have to enter email")
        user = self.model(email = email,**extra_fields)
        user = self.normalize_email(email)
        user.set_password(password)
        user.save(using = self.db)
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault("is_staff" , True)
        extra_fields.setdefault("is_superuser" , True)
        extra_fields.setdefault("is_active" , True)
        return self.create_user(email,password,extra_fields)