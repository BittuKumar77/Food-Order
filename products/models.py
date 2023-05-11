from django.db import models
import uuid

# Create your models here.

# DRY => Do not repeat yourself

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True) 

    created_at = models.DateField(auto_created=True)
    update_at = models.DateField(auto_created=True)

    class Meta:
        abstract=True

class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    product_slug = models.SlugField(unique=True)
    product_description = models.TextField()
    product_price = models.IntegerField(default=0)
    demo_product_price = models.IntegerField(default=0)

class ProductMetaInformation(BaseModel):
    product = models.OneToOneField(Product,on_delete=models.CASCADE,related_name="meta_information")
    product_quantity = models.CharField(null=True,blank=True)
    product_measuring = models.CharField(max_length=100, null = True , blank=True ,choices=(("KG","KG"),("ML","ML"),("L","L"),(None,None)))
    is_restrict = models.BooleanField(default=False)
    restrict_quantity = models.IntegerField()
    

class ProductImages(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images")
    product_images = models.ImageField(upload_to="products")
    


