customer = {'name':'Godiya', 'order_amount':'25000','loyalty_card':True,'is_student':False}
print(customer['order_amount'])
print(customer['is_student'])
print(customer['order_amount'])
print(customer['loyalty_card'])
order_amount = 25000
discount = 0
if customer['loyalty_card']:
   discount += 10
if customer['order_amount'] > '20000':
   if customer['loyalty_card']:
      discount += 5
   else:
      print('free drink')
if customer['is_student']:
   discount += 5 
discount_cal = discount / 100 * order_amount
customer.update({'discount':discount, 'discoun_cal':discount_cal, 'amount_to_pay':order_amount-discount_cal})
print(customer)
order_summary = customer
print(order_summary)
