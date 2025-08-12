class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20) 
    country = models.CharField(max_length=100) 