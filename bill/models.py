from django.db import models

# Create your models here.
class Order(models.Model):
	bill_id = models.CharField(max_length=250,default=0)	
	total_amount = models.FloatField(default=0)
	#date=models.dateField(blank=True, null=True)
	date = models.DateTimeField(blank=True, null=True)

	def publish(self):

		self.date = timezone.now()
		self.save()

	def __str__(self):
		return self.bill_id



class Order_detail(models.Model):

	bill_id= models.ForeignKey('bill.Order', related_name='Order_details')
	item_no=models.FloatField(default=0)
	item_name= models.CharField(max_length=250,default=0)
	quantity_no=models.FloatField(default=0)
	price=models.FloatField(default=0)
	
	def publish(self):
      
		self.save()

	def __str__(self):
		return self.item_name

