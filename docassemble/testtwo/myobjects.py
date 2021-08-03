from docassemble.base.util import *

__all__ = ['Asset', 'Debt', 'AssetList', 'DebtList', 'Assets', 'Debts', 'Disclosure', 'asset_types', 'debt_types']

asset_types = ['savings account', 'checking account', 'real estate', 'other']
debt_types = ['credit card', 'mortgage', 'auto loan', 'other']

class Asset(DAObject):
    pass

class Debt(DAObject):
    def init(self, *pargs, **kwargs):
        self.initializeAttribute('debtor', Person)
        super().init(*pargs, **kwargs)

class AssetList(DAList):
    complete_attribute='complete'
    object_type = Asset 
    def total(self):
        return sum(y.amount for y in self)

class DebtList(DAList):
    complete_attribute='complete'
    object_type = Debt
    def total(self):
        return sum(y.amount for y in self)

class Assets(DADict):
    object_type = AssetList
    def total(self):
        return sum(self[asset_type].total() for asset_type in asset_types)

class Debts(DADict):
    object_type = DebtList
    def total(self):
        return sum(self[debt_type].total() for debt_type in debt_types)

class Disclosure(DAObject):
    def init(self, *pargs, **kwargs):
        self.initializeAttribute('assets', Assets)
        self.initializeAttribute('debts', Debts)
        super().init(*pargs, **kwargs)
    def net_worth(self):
        return self.assets.total() - self.debts.total()

