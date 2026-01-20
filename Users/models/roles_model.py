import secrets
from django.db import models


class Role(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name="Nombre de rol"
    )
    slug = models.SlugField(
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="¿Está activo?"
    )

    class Meta:
        db_table = "roles"
        verbose_name = "Rol de usuario"
        verbose_name_plural = "Roles de usuarios"
        ordering = ("name",)

    def __str__(self):
        return f"Role: {self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            prov = secrets.token_hex(8)
            while Role.objects.filter(slug=prov).exists():
                prov = secrets.token_hex(8)
            self.slug = prov
        super().save(*args, **kwargs)
