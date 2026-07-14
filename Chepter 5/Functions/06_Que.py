def discount_Price(original_Price,discount_Percentage):
    discount_Amout = (discount_Percentage / 100) * original_Price
    final = original_Price - discount_Amout
    print(f"You will discount_Rs : {discount_Percentage}")
    print(f"Final amount is {final}")
discount_Price(100,50)
