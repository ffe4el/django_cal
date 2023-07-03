from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name="카테고리명", max_length=24)

    def __str__(self):
        return self.name

class Recipt(models.Model):
    device_id = models.IntegerField(verbose_name="디바이스ID")
    # user = models.ForeignKey('user.User', verbose_name="유저", on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, verbose_name="카테고리", on_delete=models.CASCADE)
    # year = models.IntegerField(verbose_name="결제년", null=True)
    # month = models.IntegerField(verbose_name="결제월", null=True)
    store = models.CharField(verbose_name="영업점", max_length=125)
    address = models.CharField(verbose_name="주소", max_length=125)
    amount = models.IntegerField(verbose_name="결제금액")

# class Product(models.Model):
#     recipt = models.ForeignKey(Recipt, related_name='list',on_delete=models.CASCADE)
#     name = models.CharField(verbose_name="상품명", max_length=24)
#     amount = models.IntegerField(null=True)
#     price = models.IntegerField(null=True)


class Budget(models.Model):
    device_id = models.CharField(verbose_name="디바이스ID", max_length=125, unique=True)
    living_expenses = models.IntegerField(verbose_name="생활비 예산", default=0)

    # total_spending = models.IntegerField(verbose_name="현재 사용 금액",default=0)  # 총 지출 금액 필드
    # living_expenses = models.IntegerField(verbose_name="생활비 예산",default=0)  # 생활비 예산 필드
    # # after_budget = models.IntegerField(verbose_name="생활비 잔여 금액")
    #
    # def update_total_spending(self, amount):
    #     self.total_spending += amount
    #     self.save()
    #
    # def update_living_expenses(self, amount):
    #     self.living_expenses = amount
    #     self.save()

