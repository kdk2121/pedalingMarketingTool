#-*- coding: utf-8 -*-

Gp = GrossProfit
MI = Marketing Investment
CLV = Customer Lifetime Value

class Formula:
	def _init_(self):


	def ROI1():
		return (Gp - MI)/MI

	def ROI2():
		return (CLV - MI)/MI 
