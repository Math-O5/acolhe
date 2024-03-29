from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class User(AbstractUser):
	is_anfitriao = models.BooleanField('anfitriao user', default=False)
	is_acolhido = models.BooleanField('acolhido user', default=False)
	foto = models.ImageField(upload_to="uploads/user/", default="defaultUser.png")

class Acolhido(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='acolhido')
    nome = models.CharField(max_length=120)
    contato = models.CharField(max_length=11)
    descricao = models.TextField()
    vagas = models.PositiveIntegerField(default=1)
    achou_moradia = models.BooleanField(default=False)
    # email

class Anfitriao(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='anfitriao')
    nome = models.CharField(max_length=120)
    contato = models.CharField(max_length=11)
    # email

class Local(models.Model):
	anfitriao = models.ForeignKey(Anfitriao, on_delete=models.CASCADE, related_name='anfitriao')
	acolhido = models.ForeignKey(Acolhido, on_delete=models.SET_NULL, null=True, related_name='anfitriao')
	cidade = models.CharField(max_length=120)
	bairro = models.CharField(max_length=120)
	rua = models.CharField(max_length=120)
	numero = models.PositiveIntegerField()
	vagas = models.PositiveIntegerField(default=1)
	descricao = models.TextField()
	status_list = [("OCUPADO", 'ocupado'), ("DISPONIVEL", 'disponível'), ("SOLICITADO", 'solicitado')]
	status = models.CharField(max_length=20, choices=status_list, default="DISPONIVEL")
	publicado_date = models.DateTimeField(blank=True, null=True)
	foto = models.ImageField(upload_to="uploads/local/", default="defaultLugar.png")
	# inicio_estadia
	# termino_estadia
	# tipo
	def __str__(self):
		return self.cidade

class Comment(models.Model):
    local = models.ForeignKey('acolhe.Local', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
	
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	print('****', created)
	if instance.is_acolhido:
		Acolhido.objects.get_or_create(user = instance)
	elif instance.is_anfitriao:
		Anfitriao.objects.get_or_create(user = instance)
    
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	print('_-----')	
	# print(instance.internprofile.bio, instance.internprofile.location)
	if instance.is_acolhido:
		instance.acolhido.save()
	if instance.is_anfitriao:
		instance.anfitriao.save()