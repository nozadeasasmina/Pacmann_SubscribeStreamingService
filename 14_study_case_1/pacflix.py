from tabulate import tabulate
class PacflixUser:
    # Data User
    data_user = {
        1: ["Rosy", "Basic Plan", 12, 'rosy-123'],
        2: ["Anton", "Standard Plan", 9, 'anton-123'],
        3: ["Agus", "Basic Plan", 1, 'agus-123'],
        4: ["Budi", "Premium Plan", 5, 'budi-123'],
        5: ["Shania", "Basic Plan", 6, 'shania-123']
    }

    # data plan benefit
    data_plan = [
        ['Bisa stream', 'True', 'True', 'True'],
        ['Bisa download', 'True', 'True', 'True'],
        ['Kualitas SD', 'True', 'True', 'True'],
        ['Kualitas HD', 'False', 'True', 'True'],
        ['Kualitas UHD', 'False', 'False', 'True'],
        ['Number of device', '1', '2', '4'],
        ['Jenis konten', '3rd party movie only', 'Basic plan content + Sport',
         'Basic plan content + Standart Plan + PacFlix Original Series'],
        ['Harga', '120000', '160000', '200000']
    ]
    plan_name = ['Service', 'Basic Plan', 'Standart Plan', 'Premium Plan']
    plan_benefit = tabulate(data_plan, headers=plan_name, tablefmt='simple')
    def __init__(self, username, current_plan, duration, code_referal):
        self.username = username
        self.current_plan = current_plan
        self.duration = duration
        self.code_referal = code_referal

    def check_benefit(self):
        '''
        show all plan and their benefit
        '''
        print('Plan dan benefit dari Pacflix\n')
        print(self.plan_benefit)

    def check_plan(self):
        '''
        check current plan of user and the benefit
        '''
        if self.current_plan:
            print(f"Saat ini Anda berlangganan {self.current_plan} selama {self.duration} bulan")
            print('dengan benefit\n')
            idx_current_plan = self.plan_name.index(self.current_plan)
            plan_user = [self.plan_name[0],self.plan_name[idx_current_plan]]
            benefit_user = [[row[0],row[idx_current_plan]] for row in self.data_plan]
            plan_benefit_user = tabulate(benefit_user,plan_user)
            print(plan_benefit_user)
        else:
            print('Anda belum berlangganan')
    def upgrade_plan(self,new_plan):
        '''
        func untuk upgrade plan
        input: (str) new plan
        '''
        #check apakah sudah memiliki current plan dan new plan  berada diatas dari current plan
        if self.current_plan is not None and new_plan in self.plan_name:
            idx_current_plan = self.plan_name.index(self.current_plan)
            idx_new_plan = self.plan_name.index(new_plan)
            if idx_new_plan>idx_current_plan:
                #check jika durasi > 12 bulan maka mendapat diskon
                if (self.duration > 12):
                    total = (self.data_plan[-1][idx_new_plan])*0.05 #row terakhir dari kolom index new plan
                else:
                    total = (self.data_plan[-1][idx_new_plan])
                print(f'Anda dapat melakukan upgrade ke {new_plan} dengan harga sebesar Rp {total}')
            else:
                print('Anda tidak bisa downgrade plan')
        elif self.current_plan is None:
            print('Anda belum berlangganan')
        else:
            print('Plan yang anda ajukan tidak ada. \nSilahkan memilih dari plan berikut\n')
            print(self.plan_benefit)

    def pick_plan(self, new_plan, codereferal):
        '''
        func untuk new user memilih plan
        input:
        - (str) new_plan
        - (str) code_referal
        '''
        self.duration = 1
        self.current_plan = new_plan
        self.code_referal = f'{self.username}-123'

        #list kode referal dan user name
        list_code_referal = [code[-1] for code in self.data_user.values()]
        list_username = [code[0] for code in self.data_user.values()]

        # check apakah user sudah menjadi member
        if self.username in list_username:
            print('Anda sudah member')
        else:
            #check apakah plan ada di data
            if new_plan in self.plan_name:
                #check apakah bisa mendapat diskon dnegan kode referal atau tidak
                idx_plan = self.plan_name.index(new_plan)
                if codereferal in list_code_referal:
                    totals = ((self.data_plan[-1][idx_plan]) - (self.data_plan[-1][idx_plan] * 0.04))
                else:
                    totals = self.data_plan[-1][idx_plan]
                print(f'Subscribe {new_plan} dengan pembayaran sebesar Rp {totals}')
            else:
                print('Plan tidak tersedia')