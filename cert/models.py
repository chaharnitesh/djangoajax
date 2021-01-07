from django.db import models

# Create your models here.
class CertificateRecipient(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField()
    image = models.ImageField('Certificate Image', upload_to='images')
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)

