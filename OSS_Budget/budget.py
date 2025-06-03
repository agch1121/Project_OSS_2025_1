import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        print("\n날짜 입력 방법을 선택하세요:")
        print("1. 오늘 날짜로 입력")
        print("2. 다른 날짜로 입력")
        
        date_choice = input("선택 > ")
        
        if date_choice == "1":
            date = datetime.date.today().isoformat()
        elif date_choice == "2":
            date = self.get_custom_date()
            if not date:
                print("지출 추가가 취소되었습니다.\n")
                return
        else:
            print("잘못된 선택입니다. 오늘 날짜로 설정합니다.")
            date = datetime.date.today().isoformat()
        
        expense = Expense(date, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def get_custom_date(self):
        while True:
            try:
                print("\n날짜를 입력하세요 (예: 2025-06-04 또는 06-04)")
                date_input = input("날짜 > ").strip()
                
                if not date_input:
                    return None
                
                if len(date_input.split('-')) == 2:
                    current_year = datetime.date.today().year
                    date_input = f"{current_year}-{date_input}"
                
                date_obj = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
                
                if date_obj > datetime.date.today():
                    confirm = input(f"미래 날짜({date_obj})입니다. 계속하시겠습니까? (y/n): ")
                    if confirm.lower() != 'y':
                        continue
                
                return date_obj.isoformat()
                
            except ValueError:
                print("잘못된 날짜 형식입니다. 다시 입력해주세요.")
                retry = input("다시 시도하시겠습니까? (y/n): ")
                if retry.lower() != 'y':
                    return None

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        
        sorted_expenses = sorted(self.expenses, key=lambda e: e.date, reverse=True)
        
        print("\n[지출 목록]")
        for idx, e in enumerate(sorted_expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")