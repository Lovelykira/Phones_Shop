from app.models import *

Client.objects.all().delete()
Manufacturer.objects.all().delete()
PhoneModel.objects.all().delete()
Product.objects.all().delete()
Order.objects.all().delete()
OrderItem.objects.all().delete()

Client.objects.create(name="Arthur", surname="King", phone_num="1111111")
Client.objects.create(name="Ada", surname="Bezarius", phone_num="2222222")
Client.objects.create(name="Light", surname="Yagami", phone_num="3333333")
Client.objects.create(name="Agatha", surname="Christie", phone_num="44444444")
Client.objects.create(name="Waffle", surname="House", phone_num="5555555")

Manufacturer.objects.create(name="Apple", address="Main St. 76/15", phone_num="122 22 21", site="www.apple.com")
Manufacturer.objects.create(name="Microsoft", address="Cool Av. 9/11", phone_num="233 33 32", site="www.micros.com")
Manufacturer.objects.create(name="Lenovo", address="Hop's St. 5/51", phone_num="344 44 43", site="www.lenovo.com")

PhoneModel.objects.create(name="iPhone 5s", manufacturer_id=1, OS="iOS", CPU=1.3, core_num=2, sim_card_num=1, megapixels_num=8)
PhoneModel.objects.create(name="iPhone 6", manufacturer_id=1, OS="iOS", CPU=1.4, core_num=2, sim_card_num=1, megapixels_num=8)
PhoneModel.objects.create(name="iPhone SE", manufacturer_id=1, OS="iOS", CPU=1.8, core_num=2, sim_card_num=1, megapixels_num=12)
PhoneModel.objects.create(name="Microsoft Lumia 640", manufacturer_id=2, OS="MSWin", CPU=1.2, core_num=4, sim_card_num=2, megapixels_num=8)
PhoneModel.objects.create(name="Lenovo Vibe", manufacturer_id=3, OS="Android", CPU=1.5, core_num=8, sim_card_num=2, megapixels_num=13)
PhoneModel.objects.create(name="Lenovo P70", manufacturer_id=3, OS="Android", CPU=1.9, core_num=8, sim_card_num=2, megapixels_num=13)
PhoneModel.objects.create(name="Lenovo C2", manufacturer_id=3, OS="Android", CPU=1, core_num=4, sim_card_num=2, megapixels_num=8)

Product.objects.create(name="iPhone 5S Silver", p_model_id=1, price=8499, in_stock=15)
Product.objects.create(name="iPhone 5S White", p_model_id=1, price=16999, in_stock=8)
Product.objects.create(name="Apple iPhone 6 Space Gray", p_model_id=2, price=16699, in_stock=20)
Product.objects.create(name="Apple iPhone 6 White", p_model_id=2, price=17699, in_stock=10)
Product.objects.create(name="Apple iPhone SE Silver", p_model_id=3, price=16999, in_stock=10)
Product.objects.create(name="Windows Lumia 640 DS Black", p_model_id=4, price=3399, in_stock=100)
Product.objects.create(name="Windows Lumia 640 DS White", p_model_id=4, price=4399, in_stock=3)
Product.objects.create(name="Lenovo C2 White", p_model_id=7, price=2999, in_stock=1)
Product.objects.create(name="Lenovo C2 Black", p_model_id=7, price=2999, in_stock=1)
Product.objects.create(name="Lenovo P70 Blue", p_model_id=6, price=4199, in_stock=5)
Product.objects.create(name="Lenovo P70 Red", p_model_id=6, price=4399, in_stock=5)
Product.objects.create(name="Lenovo Vibe k5 Plus", p_model_id=5, price=4999, in_stock=10)
Product.objects.create(name="Lenovo Vibe k5 Champaine Gold", p_model_id=5, price=4199, in_stock=12)

Order.objects.create(client_id_id=1)
Order.objects.create(client_id_id=2)
Order.objects.create(client_id_id=3)
Order.objects.create(client_id_id=4)
Order.objects.create(client_id_id=5)
Order.objects.create(client_id_id=1)
Order.objects.create(client_id_id=2)

OrderItem.objects.create(order_id=1, product_id=1, quantity=1)
OrderItem.objects.create(order_id=1, product_id=2, quantity=1)
OrderItem.objects.create(order_id=2, product_id=3, quantity=2)
OrderItem.objects.create(order_id=2, product_id=4, quantity=2)
OrderItem.objects.create(order_id=3, product_id=5, quantity=1)
OrderItem.objects.create(order_id=4, product_id=6, quantity=1)
OrderItem.objects.create(order_id=5, product_id=7, quantity=1)
OrderItem.objects.create(order_id=5, product_id=1, quantity=1)
OrderItem.objects.create(order_id=1, product_id=8, quantity=10)
OrderItem.objects.create(order_id=1, product_id=9, quantity=10)
OrderItem.objects.create(order_id=1, product_id=10, quantity=10)
OrderItem.objects.create(order_id=1, product_id=11, quantity=10)
OrderItem.objects.create(order_id=5, product_id=11, quantity=1)
OrderItem.objects.create(order_id=4, product_id=10, quantity=1)
