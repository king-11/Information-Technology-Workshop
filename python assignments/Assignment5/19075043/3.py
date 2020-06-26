#!/usr/bin/env python
# coding: utf-8

# In[16]:


item_names = ["Chicken Strips", "French Fries  ", "Hamburger     ",
              "Hotdog        ", "Large Drink   ", "Medium Drink  ",
              "Milk Shake    ", "Salad         ", "Small Drink   "]
item_prices = [3.50, 2.50, 4.00, 3.50, 1.75, 1.50, 2.25, 3.75, 1.25]


# In[17]:


print('Menu:')
for i in range(1, 10):
    print(f"{i}. {item_names[i - 1]} - ${item_prices[i - 1]}")


# In[18]:


order_number = 1


# In[24]:


while True:
    order = input("\nPlace your order (0 to exit): ")
    if order == '0':
        break
    total = 0
    index = 1
    print(f"\nYour order with order number {order_number} is:")
    for i in range(1, 10):
        count = order.count(str(i))
        if count:
            print(f"{index}.{item_names[i-1]}\t${item_prices[i-1]}*{count}")
            total += item_prices[int(i) - 1]*count
            index += 1
    print(f"Your order costs ${total}\n")
    order_number += 1


# In[20]:


print("Hope you enjoyed our services...")


# In[7]:





# In[ ]:




