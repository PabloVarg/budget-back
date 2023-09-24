from django.db import models


class Movement(models.Model):
    class Meta:
        ordering = ("-effective_date",)

    class Nature(models.IntegerChoices):
        INCOME = (0, "income")
        EXPENSE = (1, "expense")
        INVESTMENT = (2, "investment")

    WHOLE_SIZE = 9
    DECIMAL_SIZE = 2

    nature = models.PositiveSmallIntegerField(choices=Nature.choices)
    effective_date = models.DateField()
    category = models.TextField()
    description = models.TextField(null=True, blank=True)
    amount = models.DecimalField(
        max_digits=WHOLE_SIZE + DECIMAL_SIZE, decimal_places=DECIMAL_SIZE
    )
