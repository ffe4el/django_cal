from .views import get_recipt, get_budget
from .models import Budget

# 지출 총 금액
def sum(total_sum):
    response_data = get_recipt()
    total_sum += response_data['amount']
    return total_sum

# 총 예산 받아오기
def budget():
    budget = get_budget()
    total_budget = budget[0]
    return total_budget


