
class Category:

    def __init__(self, name: str):
        self.ledger = []
        self.name = name
    
    def deposit(self, amount, desc: str = ''):
        if type(amount) == int: amount = str(amount) + '.00'
        self.ledger.append({'amount': str(amount), 'description': desc})
    
    def withdraw(self, amount, desc: str = ''):
        if self.check_funds(amount):
            if type(amount) == int: amount = str(amount) + '.00'
            self.ledger.append({'amount': '-' + str(amount), 'description': desc})
            return True
        
        return False
    
    def get_withdrawals(self):
        withdrawals = [float(record['amount']) for record in self.ledger if float(record['amount']) < 0]
        return sum(withdrawals)

    def get_balance(self):
        balance = sum([float(tran['amount']) for tran in self.ledger])
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
                desc = desc[:23]
                space = self.calc_space(desc, amount)
                result += desc
                result += space
                result += amount
                result += '\n'
            
            # print(tran)
        
        total = self.get_balance()
        result += f'Total: {total}'

        return result
        


def get_perc(values: list):
    total = sum(values)
    # print('Withdrawals:' + str(values))
    # print('Total:' + str(total))
    perc = []
    for value in values:
        perc.append(round((value / total)*100, -1))
    return perc





def create_spend_chart(categories):
    result = 'Percentage spent by category\n'
    names = [category.name for category in categories]
    withdrawals = [category.get_withdrawals() for category in categories]
    perc = get_perc(withdrawals)
    # print('Perc:' + str(perc))
    next_line = '          \n'
    result += '100|' + next_line

    for number in range(90, 9, -10):
        result += ' ' + str(number) + '|'
        o_index = [1, 4, 7]
        line = [' ' for _ in range(10)]
        if number <= max(perc):
            for index in range(len(perc)):
                if number <= perc[index]:
                    line[o_index[index]] = 'o'

        result += ''.join(line) + '\n'
    result += '  0|' + ' o  o  o ' + '\n'
    result += '    ----------'

    # for index in range(max(names, len)):


    return result
        




