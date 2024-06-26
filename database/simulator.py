from event_system.events.add_item import AddItemRequest
from event_system.events.remove_item import RemoveItemRequest
from event_system.events.update_item import UpdateItemRequest
from items.item_factory import WarehouseItemFactory

"""
Sends request to the database before application start.
"""
class Simulator(object):
    
    def __init__(self) -> None:
        pass
    
    
    def run(self):
        for p in self.product_data:
            item = WarehouseItemFactory().create_new_item_from_tuple(p)
            AddItemRequest(item).post()

    product_data = [
        ("Apple", 1.99, 100, "Food"),
        ("Tropicana Orange Juice", 2.49, 50, "Drink"),
        ("Dell XPS 13 Laptop", 999.99, 20, "Electronics"),
        ("Nike Dri-FIT T-shirt", 19.99, 200, "Clothing"),
        ("Starbucks Coffee", 5.99, 80, "Drink"),
        ("Chiquita Banana", 0.99, 150, "Food"),
        ("Samsung Galaxy S21 Smartphone", 799.99, 30, "Electronics"),
        ("Levi's 501 Original Fit Jeans", 29.99, 100, "Clothing"),
        ("Kellogg's Corn Flakes", 3.49, 120, "Food"),
        ("Coca-Cola", 1.49, 200, "Drink"),
        ("Sony WH-1000XM4 Headphones", 349.99, 15, "Electronics"),
        ("Adidas Ultra Boost Running Shoes", 129.99, 75, "Clothing"),
        ("Ben & Jerry's Chocolate Fudge Brownie Ice Cream", 4.99, 40, "Food"),
        ("Pepsi", 1.29, 180, "Drink"),
        ("HP Pavilion 15.6-inch Laptop", 649.99, 25, "Electronics"),
        ("Under Armour HeatGear Compression T-shirt", 24.99, 150, "Clothing"),
        ("McCormick Ground Black Pepper", 2.99, 90, "Food"),
        ("Red Bull Energy Drink", 2.99, 100, "Drink"),
        ("Apple AirPods Pro", 249.99, 40, "Electronics"),
        ("Ralph Lauren Polo Shirt", 49.99, 80, "Clothing"),
        ("Ferrero Rocher Hazelnut Chocolates", 9.99, 60, "Food"),
        ("Gatorade Sports Drink", 1.99, 120, "Drink"),
        ("Microsoft Surface Pro 7", 899.99, 20, "Electronics"),
        ("Calvin Klein Boxer Briefs", 34.99, 100, "Clothing"),
        ("Campbell's Chicken Noodle Soup", 1.49, 150, "Food"),
        ("Minute Maid Orange Juice", 2.99, 70, "Drink"),
        ("LG 55-inch OLED TV", 1499.99, 10, "Electronics"),
        ("Gap 1969 Original Fit Jeans", 39.99, 60, "Clothing"),
        ("Nutella Hazelnut Spread", 5.49, 80, "Food"),
        ("Arizona Iced Tea", 0.99, 200, "Drink"),
        ("Fitbit Versa 3 Smartwatch", 229.99, 35, "Electronics"),
        ("Hanes ComfortSoft Tagless T-shirt", 12.99, 200, "Clothing"),
        ("Kraft Macaroni & Cheese", 1.99, 100, "Food"),
        ("Sprite", 1.29, 150, "Drink"),
        ("Google Nest Mini", 49.99, 30, "Electronics"),
        ("Puma Essentials Sweatpants", 44.99, 70, "Clothing"),
        ("Quaker Oats Old Fashioned Oatmeal", 3.99, 80, "Food"),
        ("Aquafina Bottled Water", 0.99, 300, "Drink"),
        ("Amazon Echo Dot (4th Gen)", 49.99, 40, "Electronics"),
        ("The North Face Resolve 2 Jacket", 89.99, 50, "Clothing"),
        ("Barilla Spaghetti Pasta", 1.79, 120, "Food"),
        ("Coca-Cola Zero Sugar", 1.49, 180, "Drink"),
        ("Canon EOS Rebel T7 DSLR Camera", 499.99, 15, "Electronics"),
        ("Hollister Skinny Jeans", 59.99, 40, "Clothing"),
        ("Heinz Tomato Ketchup", 2.49, 100, "Food"),
        ("Ocean Spray Cranberry Juice", 3.49, 60, "Drink"),
        ("Apple iPad Air (4th Gen)", 599.99, 20, "Electronics"),
        ("Lululemon Align Leggings", 98.00, 30, "Clothing"),
        ("Kellogg's Frosted Flakes Cereal", 3.99, 80, "Food"),
        ("Monster Energy Drink", 2.49, 120, "Drink"),
        ("Sony PlayStation 5", 499.99, 10, "Electronics"),
        ("H&M Hoodie", 29.99, 80, "Clothing"),
        ("Skippy Creamy Peanut Butter", 4.99, 70, "Food"),
        ("Snapple Lemon Iced Tea", 1.99, 90, "Drink"),
        ("Nintendo Switch", 299.99, 20, "Electronics"),
        ("Abercrombie & Fitch Skinny Jeans", 79.99, 30, "Clothing"),
        ("Kellogg's Rice Krispies Treats", 3.49, 100, "Food"),
        ("Mountain Dew", 1.29, 150, "Drink"),
        ("Bose QuietComfort 35 II Headphones", 299.99, 25, "Electronics"),
        ("Hollister Logo Graphic T-shirt", 24.99, 120, "Clothing"),
        ("Pepperidge Farm Goldfish Crackers", 1.99, 200, "Food"),
        ("Vitaminwater", 1.79, 100, "Drink"),
        ("Fitbit Charge 4 Fitness Tracker", 129.99, 40, "Electronics"),
        ("American Eagle Skinny Jeans", 49.95, 50, "Clothing"),
        ("Jif Creamy Peanut Butter", 3.99, 60, "Food"),
        ("Starbucks Frappuccino", 2.99, 90, "Drink"),
        ("Samsung 65-inch QLED TV", 2199.99, 10, "Electronics"),
        ("Under Armour Tech Polo Shirt", 39.99, 60, "Clothing"),
        ("Kellogg's Pop-Tarts", 2.49, 80, "Food"),
        ("Canada Dry Ginger Ale", 1.29, 150, "Drink"),
        ("Apple Watch Series 6", 399.99, 30, "Electronics"),
        ("Old Navy Slim-Fit Jeans", 29.99, 70, "Clothing"),
        ("Campbell's Cream of Mushroom Soup", 1.49, 120, "Food"),
        ("Rockstar Energy Drink", 2.49, 100, "Drink"),
        ("Amazon Fire TV Stick 4K", 49.99, 25, "Electronics"),
        ("Nike Sportswear Tech Fleece Hoodie", 99.99, 40, "Clothing"),
        ("Betty Crocker Chocolate Chip Cookie Mix", 2.49, 80, "Food"),
        ("Minute Maid Lemonade", 2.99, 60, "Drink"),
        ("Microsoft Xbox Series X", 499.99, 15, "Electronics"),
        ("Adidas Originals Superstar Shoes", 80.00, 50, "Clothing"),
        ("Kraft Velveeta Shells & Cheese", 2.99, 80, "Food"),
        ("Arizona Green Tea", 0.99, 150, "Drink"),
        ("Sony WH-CH710N Wireless Headphones", 179.99, 35, "Electronics"),
        ("Tommy Hilfiger Classic Fit Polo Shirt", 49.50, 80, "Clothing"),
        ("General Mills Lucky Charms Cereal", 3.49, 100, "Food"),
        ("Sobe Elixir", 1.49, 100, "Drink"),
        ("Apple MacBook Pro 13-inch", 1299.99, 20, "Electronics"),
        ("Wrangler Regular Fit Jeans", 19.99, 80, "Clothing"),
        ("Campbell's Tomato Soup", 1.49, 150, "Food"),
        ("Monster Rehab Tea + Lemonade Energy Drink", 2.49, 90, "Drink"),
        ("Samsung Galaxy Watch Active 2", 249.99, 30, "Electronics"),
        ("Hollister Classic Straight Jeans", 59.99, 40, "Clothing")
        ]