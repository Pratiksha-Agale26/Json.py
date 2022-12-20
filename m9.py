# Apki pass ek shopping name ki ek dictionary hai
import json
d={"shopping_list":{ "chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",} }
# shopping=open("my_shop.json","w")
# y=json.dump(d,shopping,indent=5)
with open("my_shop.json","w") as f:
    data=json.dump(d,f,indent=5)
item=input("which item you want")
quantity=int(input("quantity of item you want"))
with open("text.json","r") as f:
    data=json.load(f)
    for x,y in data.items():
        if item in y:
            for a,b in y.items():
                if item==a:
                    if (quantity)<=int(b):
                        b1=int(b)-quantity
                        y[a]=b1
                    else:
                        d=quantity-int(b)
                        y[a]=d
        else:
            y[item]=str(quantity)
        print(data)

