import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def search_by_category(self):
        if not self.expenses:
            print("검색할 지출 내역이 없습니다.\n")
            return
        
        # 현재 존재하는 카테고리들 표시
        categories = set(e.category for e in self.expenses)
        print(f"\n현재 등록된 카테고리: {', '.join(categories)}")
        
        search_category = input("검색할 카테고리를 입력하세요: ").strip()
        
        # 해당 카테고리의 지출만 필터링
        filtered_expenses = [e for e in self.expenses if e.category == search_category]
        
        if not filtered_expenses:
            print(f"'{search_category}' 카테고리의 지출 내역이 없습니다.\n")
            return
        
        print(f"\n[{search_category} 카테고리 지출 목록]")
        category_total = 0
        for idx, e in enumerate(filtered_expenses, 1):
            print(f"{idx}. {e}")
            category_total += e.amount
        
        print(f"\n{search_category} 카테고리 총 지출: {category_total}원\n")

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")