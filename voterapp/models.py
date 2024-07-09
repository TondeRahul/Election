# working code

# voter api

# from django.db import models

# class Voterlist(models.Model):
#     voter_id = models.AutoField(primary_key=True)
#     voter_name = models.CharField(max_length=255)
#     voter_parent_name = models.CharField(max_length=255)
#     voter_house_number = models.CharField(max_length=255)
#     voter_age = models.CharField(max_length=255)
#     voter_gender = models.CharField(max_length=255)
#     voter_town_id = models.IntegerField()
#     voter_booth_id = models.IntegerField()
#     voter_contact_number = models.IntegerField()
#     voter_cast = models.CharField(max_length=255)

#     class Meta:
#         db_table = 'tbl_voter'

# class Booth(models.Model):
#     booth_id = models.AutoField(primary_key=True)
#     booth_name = models.CharField(max_length=255)
#     booth_town_id = models.IntegerField()

#     class Meta:
#         db_table = 'tbl_booth'

# class Town(models.Model):
#     town_id = models.AutoField(primary_key=True)
#     town_name = models.CharField(max_length=255)
#     town_panchayat_samiti_id = models.IntegerField()

#     class Meta:
#         db_table = 'tbl_town'



# # # rigister api

# from django.db import models
# from django.contrib.auth.hashers import make_password


# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)  
#     user_name = models.CharField(max_length=100)
#     user_phone = models.CharField(max_length=20)
#     user_password = models.CharField(max_length=256)
#     user_firm_id = models.IntegerField()
#     user_booth_id = models.IntegerField()

#     def save(self, *args, **kwargs):        
        
#         if self.user_password:
#             self.user_password = make_password(self.user_password)
#         super().save(*args, **kwargs)

#     class Meta:
#         db_table = 'tbl_user'



# # # Get voters api

# class Voter(models.Model):
#     voter_name = models.CharField(max_length=100)
#     town_name = models.CharField(max_length=100)
#     booth_name = models.CharField(max_length=100)

#     class Meta:
#         managed = False 


# # # Panchayat_samiti api

# class PanchayatSamiti(models.Model):
#     panchayat_samiti_id = models.AutoField(primary_key=True)
#     panchayat_samiti_name = models.CharField(max_length=255)
#     panchayat_samiti_zp_id = models.IntegerField()

#     class Meta:
#         db_table = 'tbl_panchayat_samiti'


# # # ZP api

# class ZP(models.Model):
#     zp_id = models.AutoField(primary_key=True)
#     zp_name = models.CharField(max_length=255)
#     zp_state_id = models.IntegerField()


#     class Meta:
#         db_table = 'tbl_zp'


# # # vidhansabha api

# class Vidhansabha(models.Model):
#     vidhansabha_id = models.AutoField(primary_key=True)
#     vidhansabha_name = models.CharField(max_length=255)

#     class Meta:
#         db_table = 'tbl_vidhansabha'


# # # state api

# class State(models.Model):
#     state_id = models.AutoField(primary_key=True)
#     state_name = models.CharField(max_length=255)

#     class Meta:
#         db_table = 'tbl_state'

# # firm login and firm register

# from django.db import models

# class Firm(models.Model):
#     firm_id = models.AutoField(primary_key=True)
#     firm_name = models.CharField(max_length=255, unique=True)
#     firm_contact_number = models.CharField(max_length=15)
#     firm_password = models.CharField(max_length=255)

#     class Meta:
#         db_table = 'tbl_firm'


# # Religion api

# class Religion(models.Model):
#     religion_id = models.AutoField(primary_key=True)
#     religion_name = models.CharField(max_length=255)

#     class Meta:
#         db_table = 'tbl_religion'
        

# # Favour non-favour api

# class Favour_non_favour(models.Model):
#     favour_id = models.AutoField(primary_key=True)
#     favour_type = models.CharField(max_length=255)

#     class Meta:
#         db_table = 'tbl_favour'


from django.db import models

class Voterlist(models.Model):
    voter_id = models.AutoField(primary_key=True)
    voter_name = models.CharField(max_length=255)
    voter_parent_name = models.CharField(max_length=255)
    voter_house_number = models.CharField(max_length=255)
    voter_age = models.CharField(max_length=255)
    voter_gender = models.CharField(max_length=255)
    voter_town_id = models.IntegerField()
    voter_booth_id = models.IntegerField()
    voter_contact_number = models.IntegerField()
    voter_cast = models.CharField(max_length=255)
    voter_favour_id = models.IntegerField()
    voter_constituency_id = models.IntegerField()

    class Meta:
        db_table = 'tbl_voter'


class Booth(models.Model):
    booth_id = models.AutoField(primary_key=True)
    booth_name = models.CharField(max_length=255)
    booth_town_id = models.IntegerField()

    class Meta:
        db_table = 'tbl_booth'
        unique_together = ('booth_name', 'booth_town_id')

class Town(models.Model):
    town_id = models.AutoField(primary_key=True)
    town_name = models.CharField(max_length=255)
    town_panchayat_samiti_id = models.IntegerField()

    class Meta:
        db_table = 'tbl_town'
        unique_together = ('town_name', 'town_panchayat_samiti_id')




# # register api

from django.contrib.auth.hashers import make_password

class User(models.Model):
    user_id = models.AutoField(primary_key=True)  
    user_name = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=20)
    user_password = models.CharField(max_length=256)
    user_town_user_id = models.IntegerField()
    user_booth_id = models.IntegerField()

    def save(self, *args, **kwargs):        
        
        if self.user_password:
            self.user_password = make_password(self.user_password)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'tbl_user'



# # Get_voters api

class Voter(models.Model):
    voter_id = models.AutoField(primary_key=True)
    voter_name = models.CharField(max_length=100)
    # voter_contact_number = models.CharField(max_length=20)
    # voter_cast = models.CharField(max_length=255)
    booth_name = models.CharField(max_length=100)
    town_name = models.CharField(max_length=100)
    voter_contact_number = models.CharField(max_length=20)
    booth_id = models.IntegerField()  


    class Meta:
        managed = False 



# # Panchayat_samiti api

class PanchayatSamiti(models.Model):
    panchayat_samiti_id = models.AutoField(primary_key=True)
    panchayat_samiti_name = models.CharField(max_length=255)
    panchayat_samiti_zp_id = models.IntegerField()

    class Meta:
        db_table = 'tbl_panchayat_samiti'
        unique_together = ('panchayat_samiti_name', 'panchayat_samiti_zp_id')



# # ZP api

class ZP(models.Model):
    zp_id = models.AutoField(primary_key=True)
    zp_name = models.CharField(max_length=255)
    zp_state_id = models.IntegerField()

    class Meta:
        db_table = 'tbl_zp'
        unique_together = ('zp_name', 'zp_state_id')


# # vidhansabha api

class Vidhansabha(models.Model):
    vidhansabha_id = models.AutoField(primary_key=True)
    vidhansabha_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_vidhansabha'


# # state api

class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_state'



# politician login and politician register

from django.db import models
from django.contrib.auth.hashers import make_password

class Politician(models.Model):
    politician_id = models.AutoField(primary_key=True)
    politician_name = models.CharField(max_length=255, unique=True)
    politician_contact_number = models.CharField(max_length=15)
    politician_password = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_politician'

    def save(self, *args, **kwargs):
        self.politician_password = make_password(self.politician_password)
        super(Politician, self).save(*args, **kwargs)

        

# Religion api

class Religion(models.Model):
    religion_id = models.AutoField(primary_key=True)
    religion_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_religion'
        

# Favour non-favour api

class Favour_non_favour(models.Model):
    favour_id = models.AutoField(primary_key=True)
    favour_type = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_favour'
        unique_together = ('favour_id', 'favour_type')


# user_town login and user_town register

from django.db import models

class Town_user(models.Model):
    town_user_id = models.AutoField(primary_key=True)
    town_user_name = models.CharField(max_length=255, unique=True)
    town_user_contact_number = models.CharField(max_length=15)
    town_user_password = models.CharField(max_length=255)
    town_user_town_id = models.IntegerField()
    town_user_politician_id = models.IntegerField()

    class Meta:
        db_table = 'tbl_town_user'

# constituency wise voter api

class Constituency(models.Model):
    constituency_id = models.AutoField(primary_key=True)
    constituency_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_constituency'


