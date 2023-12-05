from django.db import models
from restaurantApi.models import Items, Users

# Create your models here.
class Orders(models.Model):
    o_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, models.DO_NOTHING, blank=True, null=True, related_name='user_order')
    items = models.ForeignKey(Items, models.DO_NOTHING, blank=True, null=True, related_name='order_item')
    status = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'
