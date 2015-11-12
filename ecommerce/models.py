from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, unique=True)
    picture = models.ImageField(upload_to='product/%Y/%m', blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=24, default=0)
    brand = models.ForeignKey(Brand)
    category = models.ForeignKey('Category')
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return "%s (%s) - %s" % (self.title, self.brand.name, self.category.name)


class Category(models.Model):
    name = models.CharField(max_length=128)
    parent = models.ForeignKey("self", related_name="children", blank=True, null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    # Homework
    total_price = models.DecimalField(max_digits=24, decimal_places=2, default=0)
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def add(self, product, quantity=1):
        self.items.add(CartItem(product=product, unit_price=product.price, quantity=quantity))

class CartItem(models.Model):
    # Homework
    cart = models.ForeignKey(Cart, related_name="items")
    product = models.ForeignKey(Product)
    unit_price = models.DecimalField(max_digits=24, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "%s : %d" % (self.product.title, self.quantity)

    @property
    def total_price(self):
        return self.quantity * self.unit_price
