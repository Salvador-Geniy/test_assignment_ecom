from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class CategoryModel(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey(to='self', on_delete=models.PROTECT, null=True, blank=True,
                            related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = ['parent', 'name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class GoodModel(models.Model):
    category = models.ForeignKey(to=CategoryModel, on_delete=models.PROTECT, related_name='goods')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Good'
        verbose_name_plural = 'Goods'

    def __str__(self):
        return self.name


class ImageModel(models.Model):
    good = models.ForeignKey(to=GoodModel, on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to='goods_images')
    short_description = models.CharField(max_length=150, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.good.name


class GoodVariations(models.Model):
    name = models.CharField(max_length=100)
    goods = models.ManyToManyField(to=GoodModel)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Variation'
        verbose_name_plural = 'Variations'

    def __str__(self):
        return self.name

