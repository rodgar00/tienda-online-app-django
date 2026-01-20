from django.conf import settings
from django.db import models

class PaisesChoices(models.TextChoices):
    SPAIN = "ES", "ESPAÑA"
    FRANCE = "FR", "FRANCIA"

class InfoPersonal(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="info_personal"
    )
    document = models.CharField(max_length=20, null=False, blank=False, unique=False, verbose_name="Documento (DNI, NIE, PASAPORTE, OTROS)", help_text="(Obligatorio)"),
    address = models.TextField(null=False, blank=False, verbose_name="Dirección", help_text="(Obligatorio)")
    age = models.PositiveIntegerField(null=False, blank=False, default=18, choices=[(n, n) for n in range(1, 101)], verbose_name="Age", help_text="(Obligatorio)")
    birthday = models.DateField(verbose_name="Fecha de nacimiento", help_text="(Obligatorio)")
    phone = models.CharField(max_length=11, verbose_name="Teléfono", help_text="(Opcional)")
    city = models.ForeignKey("CiudadModel", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Ciudad", help_text="(Obligatorio)")
    country = models.CharField(max_length=3, choices=PaisesChoices.choices, default=PaisesChoices.SPAIN, verbose_name="País", help_text="(Obligatorio)")

    class Meta:
        db_table = "info_personal"
        verbose_name = "Información personal"
        verbose_name_plural = "Datos personales"
        ordering = ("-country",)

    def __str__(self):
        return f"{self.document} - {self.city} / {self.country}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)