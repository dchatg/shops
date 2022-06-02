# -*- coding: utf-8 -*-
"""
Created on Sun May 15 21:49:02 2022

@author: dchat
"""

class Shop():
    
    def __init__(self):
        self.shops = {}
        self.id = 'abc'
        self.password = '123456'
        self.n = 0
        
    '''用于商品信息输入'''
    def add_z(self):
        while True:
            ids = input('请输入商品编号\n')
            name = input('请输入商品名称\n')
            try:
                price = float(input('请输入商品价格\n'))
            except ValueError:
                print('价格格式错误，请重试')
                self.add_z()
                break
            else:
                self.shops[ids] = [ids,name,price]
            print('添加成功')
            flags = input('继续添加？ 结束请输入q \n')
            if flags == 'q':
                self.admin()
                break
            
    '''用于删除商品'''
    def dele(self):
        self.show_z()
        while True:
            det = input('选择需要删除的商品，输入商品编号，输入q结束\n')
            if det == 'q':
                self.admin()
                break
            elif det in self.shops:
                d = input('确定删除？y/n\n')
                if d == 'y':
                    del self.shops[det]
                    print('已删除')
                    self.dele()
                    break
                else:
                    pass
            else:
                print('商品编号错误，请重新输入')
                
    '''用于修改商品'''
    def xq(self):
        self.show_z()
        while True:
            id_s=input('请输入想要修改的商品编号，输入q结束\n')
            if id_s == 'q':
                self.admin()
                break
            elif id_s in self.shops:
                print('查询的商品信息如下 \n商品编号     名称     价格')
                print (f" {self.shops[id_s][0]}          {self.shops[id_s][1]}      {self.shops[id_s][2]}")
                new_id=input('请输入新的商品编号：\n')
                new_name=input('请输入新的商品名：\n')
                try:
                    new_price=float(input('请输入价格：\n'))
                except ValueError:
                    print('价格格式错误，请重试')
                    self.xq()
                    break
                else:
                    self.shops[new_id]=[new_id,new_name,new_price]
                    del self.shops[id_s]
                    print('修改完成')
                    
            else:
                print('商品编号错误，请重新输入')
                
    '''用于查询商品'''
    def find_s(self):
        while True:
            find_id=input('请输入查询的商品编号，输入q结束\n')
            if find_id == 'q':
                self.admin()
                break
            if find_id in self.shops:
                print('查询的商品信息如下 \n商品编号     名称     价格')
                print (f" {self.shops[find_id][0]}          {self.shops[find_id][1]}      {self.shops[find_id][2]}")
            else:
                print('您查找的商品不存在')
            
    '''用于输出商品表'''
    def show_z(self):
        print('商品信息如下 \n商品编号     名称     价格')
        for i in self.shops:
            print (f" {self.shops[i][0]}          {self.shops[i][1]}      {self.shops[i][2]}")
        if self.n == '2':
            self.admin()
            
    '''超市管理主页面'''
    def admin(self):
        while True:
            choice = 0
            print('\n超市管理系统')
            print('1.添加商品')
            print('2.查询商品')
            print('3.显示全部商品')
            print('4.修改商品信息')
            print('5.删除商品')
            print('6.退出系统')
            choice=input('请输入您的选择\n')
            
            if choice == '1':#添加商品
                self.add_z()
                break
            elif choice == '2':#查询商品
                self.find_s()
                break
            elif choice == '3':#显示全部商品
                self.n = '3'
                self.show_z()
                self.admin()
                break
            elif choice == '4':#修改商品信息
                self.n = '4'
                self.xq()
                break
            elif choice == '5':#删除商品信息
                self.n = '5'
                self.dele()
                break
            elif choice == '6':#
                self.login()
                break
            else:
                print('输入错误')
            self.n=choice
            
    '''购物页面'''
    def user(self):
        self.n = 1
        print('欢迎使用超市购物系统')
        print('您可以输入商品编号和购买数量选购商品，输入a结账')
        self.show_z()
        total = 0
        while True:
            num = input("请输入商品编号,结束购物请按a后回车\n")
            if num == 'a':
                if total == 0:
                    print('您本次未购买商品，欢迎下次光临')
                    self.login()
                    break
                else:
                    print(f'本次购物总价为{total}元，谢谢光临')
                    self.login()
                    break
                break
            elif num in self.shops:
                zys = self.shops[num][2]
                try:
                    nums = int(input('请输入购买数量\n'))
                except ValueError:
                    print('输入错误，请重新输入')
                else:
                    total = total + zys*nums
                print(f'当前总价为{total}元')
            else:
                print('商品编号错误，请重新输入')
                
    '''登录选择页面'''
    def login(self):
        print('超市购物系统'.center(30,'='))
        adm = input('购物请按0，登录系统请按1，退出请按e\n')
        if adm == '0':
            self.user()
        elif adm == '1':
            uname = input('请输入用户名：\n')
            if uname == self.id:
                while True:
                    passw = input("请输入用户密码：\n")
                    if passw == self.password:
                        print(f"欢迎使用，{uname}\n")
                        self.admin()
                        break
                    else:
                        print("密码错误，请再试一次")
            else:
                print('用户名错误，请重试')
        elif adm == 'e':
            print('感谢您的使用，期待您的下次光临')
            self.login()
        else:
            print('错误选项')
            self.login()
            
            
            
if __name__ == '__main__':
    shop=Shop()
    shop.login()
                