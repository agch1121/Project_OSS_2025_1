import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.monthly_budget = 0

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def set_monthly_budget(self):
        try:
            budget = int(input("월 예산을 입력하세요 (원): "))
            if budget <= 0:
                print("올바른 금액을 입력해주세요.\n")
                return
            self.monthly_budget = budget
            print(f"월 예산이 {budget}원으로 설정되었습니다.\n")
        except ValueError:
            print("잘못된 금액입니다.\n")

    def get_current_month_total(self):
        current_month = datetime.date.today().strftime("%Y-%m")
        month_expenses = [e for e in self.expenses if e.date.startswith(current_month)]
        return sum(e.amount for e in month_expenses)

    def get_remaining_days_in_month(self):
        today = datetime.date.today()
        if today.month == 12:
            next_month = datetime.date(today.year + 1, 1, 1)
        else:
            next_month = datetime.date(today.year, today.month + 1, 1)
        return (next_month - today).days

    def show_budget_status(self):
        if self.monthly_budget == 0:
            print("설정된 예산이 없습니다. 먼저 예산을 설정해주세요.\n")
            return

        current_total = self.get_current_month_total()
        remaining_budget = self.monthly_budget - current_total
        usage_rate = (current_total / self.monthly_budget) * 100
        remaining_days = self.get_remaining_days_in_month()

        print("\n=== 예산 현황 ===")
        print(f"월 예산: {self.monthly_budget:,}원")
        print(f"사용 금액: {current_total:,}원")
        print(f"남은 예산: {remaining_budget:,}원")
        print(f"사용률: {usage_rate:.1f}%")
        
        # 진행률 별표로 표시
        if usage_rate <= 25:
            status_text = "[*---] 25% 이하"
        elif usage_rate <= 50:
            status_text = "[**--] 50% 이하"
        elif usage_rate <= 75:
            status_text = "[***-] 75% 이하"
        else:
            status_text = "[****] 75% 초과"
        
        print(f"진행률: {status_text}")
        
        if remaining_days > 0:
            daily_average = remaining_budget / remaining_days if remaining_budget > 0 else 0
            print(f"남은 일수: {remaining_days}일")
            print(f"일평균 가능 지출: {daily_average:,.0f}원")
        
        # 상태에 따른 메시지
        if usage_rate >= 100:
            print("경고: 예산을 초과했습니다!")
        elif usage_rate >= 80:
            print("주의: 예산의 80%를 사용했습니다.")
        elif usage_rate >= 50:
            print("알림: 예산의 절반을 사용했습니다.")
        else:
            print("상태: 예산 사용이 양호합니다.")
        
        print()

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")