
class Category:

    def __init__(self, name: str):
        self.ledger = []
        self.name = name
    
    def deposit(self, amount: float, desc: str = ''):
        self.ledger.append({'amount': amount, 'description': desc})
    
    def withdraw(self, amount: float, desc: str = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': desc})
            return True
        
        return False

    def get_balance(self):
        balance = sum([tran['amount'] for tran in self.ledger])
        return balance

    def transfer(self, amount: int, category):
        if self.withdraw(amount, f'Transfer to {category.name}'):
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        
        return False

    def check_funds(self, amount: float):
        balance = self.get_balance()
        return amount < balance

    def title(self):
        result = ''
        stars = ''
        star_count = round((30 - len(self.name))/2)
        for _ in range(star_count):
            stars += '*'
        result += stars
        result += self.name
        result += stars
        result += '\n'

        return result
    
    def calc_space(self, desc, amount):
        space = ''
        space_count = 30 - (len(desc) + len(amount))
        for _ in range(space_count):
            space += ' '
        return space
    
    def __str__(self):
        result = ''
        result += self.title()
        for tran in self.ledger:
            desc = tran['description']
            amount = str(tran['amount'])
            if len(desc) < 23:
                space = self.calc_space(desc, amount)
                result += desc
                result += space
                result += amount
                result += '\n'
            else:
                pass
        



food = Category('Food')
print(food)

# def create_spend_chart(categories):



