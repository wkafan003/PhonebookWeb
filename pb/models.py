from django.db import models


# Create your models here.
class phonebook(models.Model):
    l_name = models.CharField(db_column='l_name', max_length=32, null=True)
    f_name = models.CharField(db_column='f_name', max_length=32, null=True)
    gender = models.CharField(db_column='gender', max_length=10, null=True)
    m_name = models.CharField(db_column='m_name', max_length=32, null=True)
    street = models.ForeignKey('street_table', models.CASCADE, related_name='street', default=1)
    city = models.ForeignKey('city_table', models.CASCADE, related_name='city', default=1)
    email = models.EmailField(db_column='email', null=True)
    b_num = models.IntegerField(db_column='b_num', null=True)
    ap = models.IntegerField(db_column='ap', null=True)
    tel = models.CharField(db_column='tel', max_length=24, null=True)
    job = models.CharField(db_column='job', max_length=32, null=True)
    post = models.CharField(db_column='post', max_length=32, null=True)
    def __str__(self):
        return ("%s %s %s %s") % (self.l_name,self.f_name,self.m_name,self.tel,)
    def Json(self):
        json = dict()
        json['id'] = self.id
        json['l_name'] = self.l_name
        json['f_name'] = self.f_name
        json['m_name'] = self.m_name
        json['gender'] = self.gender
        json['street'] = self.street.s_value
        json['city'] = self.city.c_value
        json['email'] = self.email
        json['b_num'] = self.b_num
        json['ap'] = self.ap
        json['tel'] = self.tel
        json['job'] = self.job
        json['post'] = self.post
        return json


class street_table(models.Model):
    s_value = models.CharField(db_column='s_value', max_length=64, null=True)

    def __str__(self):
        return self.s_value

    def Json(self):
        json = dict()
        json['id'] = self.id
        json['s_value'] = self.s_value

        return json


class city_table(models.Model):
    c_value = models.CharField(db_column='s_value', max_length=64, null=True)

    def __str__(self):
        return self.c_value

    def Json(self):
        json = dict()
        json['id'] = self.id
        json['c_value'] = self.c_value

        return json
