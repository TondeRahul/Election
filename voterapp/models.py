# # Register api

# from django.db import models
# from django.contrib.auth.hashers import make_password


# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)  
#     user_name = models.CharField(max_length=100)
#     user_phone = models.CharField(max_length=20)
#     user_password = models.CharField(max_length=256)

#     def save(self, *args, **kwargs):        
        
#         if self.user_password:
#             self.user_password = make_password(self.user_password)
#         super().save(*args, **kwargs)

#     class Meta:
#         db_table = 'tbl_user'


# ##########################################################

# working code

from django.db import models
from django.contrib.auth.hashers import make_password



class Voter(models.Model):
    voter_id = models.IntegerField(primary_key=True,default=0)
    voter_name = models.CharField(max_length=255)
    voter_parent_name = models.CharField(max_length=255)
    voter_house_number = models.CharField(max_length=255)
    voter_age = models.CharField(max_length=255)
    voter_gender = models.CharField(max_length=255)
    voter_town_id = models.IntegerField()
    voter_booth_id = models.IntegerField()

    class Meta:
        db_table = 'tbl_voter'

class Booth(models.Model):
    booth_id = models.IntegerField(primary_key=True, default=0)
    booth_name = models.CharField(max_length=255)
    booth_town_id = models.IntegerField()

    class Meta:
        db_table = 'tbl_booth'

class Town(models.Model):
    town_id = models.IntegerField(primary_key=True, default=0)
    town_name = models.CharField(max_length=255)
    town_panchayat_samiti_id = models.IntegerField()

    class Meta:
        db_table = 'tbl_town'



# # rigister api

from django.db import models
from django.contrib.auth.hashers import make_password


class User(models.Model):
    user_id = models.AutoField(primary_key=True)  
    user_name = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=20)
    user_password = models.CharField(max_length=256)

    def save(self, *args, **kwargs):        
        
        if self.user_password:
            self.user_password = make_password(self.user_password)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'tbl_user'



# # Get voters api

class Voter(models.Model):
    voter_name = models.CharField(max_length=100)
    town_name = models.CharField(max_length=100)
    booth_name = models.CharField(max_length=100)

    class Meta:
        managed = False 


# # Panchayat_samiti api

class PanchayatSamiti(models.Model):
    panchayat_samiti_id = models.IntegerField(primary_key=True, default=0)
    panchayat_samiti_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_panchayat_samiti'


# # ZP api

class ZP(models.Model):
    zp_id = models.IntegerField(primary_key=True, default=0)
    zp_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_zp'