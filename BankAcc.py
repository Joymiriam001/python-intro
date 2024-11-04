class BankAccount:
    def __init__(self, name, branch, accountNo):
        self.name = name
        self.branch = branch
        self.accountNo = accountNo

class teacherAccount(BankAccount):
    def __init__(self, teacherName, teacherBranch, teacherAccountNo, teacherId):
        super().__init__(name=teacherName, branch=teacherBranch, accountNo=teacherAccountNo)
        self.teacherId = teacherId


joyAccount= BankAccount("Joymiriam", "Westlands", 676568888546)

print(f"Account Name: {joyAccount.name}, Account Branch: {joyAccount.branch}, Account No: {joyAccount.accountNo}")

teacherAccount= teacherAccount("Joe","Kilimani", "88822229999", "T79727x")

print(f"Account Name: {teacherAccount.name}, Account Branch: {teacherAccount.branch}, Account No: {teacherAccount.accountNo}, teacherId: {teacherAccount.teacherId}")
