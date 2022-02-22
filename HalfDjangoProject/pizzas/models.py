from django.db import models


class Pizza(models.Model):
	name = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Topping(models.Model):
	name = models.TextField()
	pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

	def __str__(self):
		if len(self.name) > 50:
			return f"{self.name}..."
		else:
			return self.name