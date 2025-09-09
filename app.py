import streamlit as st
import pandas as pd

# --- Page Configuration ---
st.set_page_config(
    page_title="McDonald's India Macro Calculator",
    page_icon="🍔",
    layout="wide"
)

# --- Data Loading & Preparation ---
# All 200+ menu items from your original HTML are included here.
menu_data = [
    # type: burgers/wraps
    { "name": "McVeggie Burger", "type": "burgers/wraps", "category": "Regular Menu", "calories": 402.05, "protein": 10.24, "fat": 13.83, "carbs": 56.54, "sugar": 7.9, "sodium": 706.13 },
    { "name": "Dosa Masala Burger", "type": "burgers/wraps", "category": "Regular Menu", "calories": 340.23, "protein": 5.66, "fat": 12.39, "carbs": 51.52, "sugar": 12.68, "sodium": 710.54 },
    { "name": "Aloo Tikki Burger", "type": "burgers/wraps", "category": "Regular Menu", "calories": 339.52, "protein": 8.5, "fat": 11.31, "carbs": 50.27, "sugar": 7.05, "sodium": 545.34 },
    { "name": "McSpicy Paneer Burger", "type": "burgers/wraps", "category": "Regular Menu", "calories": 652.76, "protein": 20.29, "fat": 39.45, "carbs": 52.33, "sugar": 8.35, "sodium": 1074.58 },
    { "name": "McSpicy Paneer Wrap", "type": "burgers/wraps", "category": "Regular Menu", "calories": 674.68, "protein": 20.96, "fat": 39.1, "carbs": 59.27, "sugar": 3.5, "sodium": 1087.46 },
    { "name": "Schezwan Veg Burger", "type": "burgers/wraps", "category": "Regular Menu", "calories": 286.09, "protein": 6.13, "fat": 8.47, "carbs": 46.33, "sugar": 7.88, "sodium": 515.87 },
    { "name": "Butter Paneer Grilled Burger", "type": "burgers/wraps", "category": "Regular Menu", "calories": 382.26, "protein": 12.85, "fat": 17.15, "carbs": 44.12, "sugar": 8.78, "sodium": 900.37 },
    { "name": "Veg Maharaja Mac", "type": "burgers/wraps", "category": "Regular Menu", "calories": 832.67, "protein": 24.17, "fat": 37.94, "carbs": 93.84, "sugar": 11.52, "sodium": 1529.22 },
    { "name": "Chicken McGrill Burger", "type": "burgers/wraps", "category": "Regular Menu", "calories": 274.17, "protein": 13.19, "fat": 8.52, "carbs": 36.18, "sugar": 6.28, "sodium": 543.33 },
    { "name": "Butter Chicken Grilled Burger", "type": "burgers/wraps", "category": "Regular Menu", "calories": 357.01, "protein": 17.06, "fat": 14.41, "carbs": 39.76, "sugar": 6.55, "sodium": 919.59 },
    { "name": "McEgg Burger", "type": "burgers/wraps", "category": "Regular Menu", "calories": 265.0, "protein": 12.0, "fat": 10.0, "carbs": 31.0, "sugar": 5.0, "sodium": 675.0 },
    { "name": "McChicken Burger", "type": "burgers/wraps", "category": "Regular Menu", "calories": 400.8, "protein": 15.66, "fat": 15.7, "carbs": 47.98, "sugar": 5.53, "sodium": 766.33 },
    { "name": "Filet-o-Fish Burger", "type": "burgers/wraps", "category": "Regular Menu", "calories": 348.11, "protein": 15.44, "fat": 14.16, "carbs": 38.85, "sugar": 5.58, "sodium": 530.54 },
    { "name": "McSpicy Chicken Burger", "type": "burgers/wraps", "category": "Regular Menu", "calories": 451.92, "protein": 21.46, "fat": 19.36, "carbs": 46.08, "sugar": 5.88, "sodium": 928.52 },
    { "name": "McSpicy Chicken Wrap", "type": "burgers/wraps", "category": "Regular Menu", "calories": 567.19, "protein": 23.74, "fat": 26.89, "carbs": 57.06, "sugar": 2.52, "sodium": 1152.38 },
    { "name": "Chicken Maharaja Mac", "type": "burgers/wraps", "category": "Regular Menu", "calories": 689.12, "protein": 34.0, "fat": 36.69, "carbs": 55.39, "sugar": 8.92, "sodium": 1854.71 },
    { "name": "Corn & Cheese Veg Burger", "type": "burgers/wraps", "category": "Regular Menu", "calories": 512.17, "protein": 15.3, "fat": 30.73, "carbs": 40.53, "sugar": 7.65, "sodium": 1087.45 },
    { "name": "Green Chilli Aloo Naan", "type": "burgers/wraps", "category": "Regular Menu", "calories": 359.21, "protein": 7.91, "fat": 15.08, "carbs": 46.36, "sugar": 2.73, "sodium": 579.6 },
    { "name": "McSpicy Premium Chicken Burger", "type": "burgers/wraps", "category": "Regular Menu", "calories": 622.25, "protein": 31.49, "fat": 34.65, "carbs": 43.6, "sugar": 6.07, "sodium": 1014.88 },
    { "name": "Chicken Kebab Burger", "type": "burgers/wraps", "category": "Regular Menu", "calories": 230.95, "protein": 9.07, "fat": 9.32, "carbs": 31.06, "sugar": 3.84, "sodium": 410.78 },
    { "name": "McEgg Burger for Happy Meal", "type": "burgers/wraps", "category": "Regular Menu", "calories": 290.42, "protein": 12.45, "fat": 12.27, "carbs": 32.89, "sugar": 4.89, "sodium": 757.91 },
    { "name": "Veg McMuffin", "type": "burgers/wraps", "category": "Breakfast Menu", "calories": 305.35, "protein": 10.22, "fat": 11.78, "carbs": 38.06, "sugar": 3.02, "sodium": 604.63 },
    { "name": "Double Cheese McMuffin", "type": "burgers/wraps", "category": "Breakfast Menu", "calories": 273.78, "protein": 17.08, "fat": 9.58, "carbs": 29.27, "sugar": 2.5, "sodium": 773.69 },
    { "name": "Spicy Egg McMuffin", "type": "burgers/wraps", "category": "Breakfast Menu", "calories": 276.27, "protein": 11.49, "fat": 13.01, "carbs": 27.27, "sugar": 2.63, "sodium": 773.69 },
    { "name": "Sausage McMuffin", "type": "burgers/wraps", "category": "Breakfast Menu", "calories": 281.44, "protein": 16.25, "fat": 10.81, "carbs": 28.62, "sugar": 2.38, "sodium": 742.6 },
    { "name": "Sausage McMuffin with egg", "type": "burgers/wraps", "category": "Breakfast Menu", "calories": 290.42, "protein": 22.46, "fat": 15.04, "carbs": 28.87, "sugar": 2.61, "sodium": 804.04 },
    { "name": "Egg McMuffin", "type": "burgers/wraps", "category": "Breakfast Menu", "calories": 283.46, "protein": 14.05, "fat": 12.31, "carbs": 28.12, "sugar": 2.39, "sodium": 619.31 },
    { "name": "Triple Cheese Burger Chicken", "type": "burgers/wraps", "category": "Gourmet Menu", "calories": 457.64, "protein": 24.43, "fat": 22.85, "carbs": 37.45, "sugar": 7.64, "sodium": 1395.77 },
    { "name": "Triple Cheese Burger Veg", "type": "burgers/wraps", "category": "Gourmet Menu", "calories": 524.59, "protein": 19.54, "fat": 33.16, "carbs": 37.45, "sugar": 7.99, "sodium": 1124.27 },
    { "name": "McCheese Burger Veg", "type": "burgers/wraps", "category": "Gourmet Menu", "calories": 671.9, "protein": 14.99, "fat": 49.72, "carbs": 56.24, "sugar": 7.99, "sodium": 1153.99 },
    { "name": "McCheese Burger Chicken", "type": "burgers/wraps", "category": "Gourmet Menu", "calories": 617.2, "protein": 27.37, "fat": 43.56, "carbs": 27.11, "sugar": 10.01, "sodium": 1749.04 },
    { "name": "McSpicy Premium Veg Burger", "type": "burgers/wraps", "category": "Gourmet Menu", "calories": 534.71, "protein": 22.44, "fat": 39.21, "carbs": 45.0, "sugar": 7.57, "sodium": 1446.87 },
    { "name": "Chicken By Mac", "type": "burgers/wraps", "category": "Gourmet Menu", "calories": 660.18, "protein": 28.34, "fat": 41.54, "carbs": 59.63, "sugar": 9.92, "sodium": 1449.26 },
    # type: chicken
    { "name": "4 Piece Chicken McNuggets", "type": "chicken", "category": "Regular Menu", "calories": 169.68, "protein": 10.03, "fat": 9.54, "carbs": 10.5, "sugar": 0.32, "sodium": 313.25 },
    { "name": "6 Piece Chicken McNuggets", "type": "chicken", "category": "Regular Menu", "calories": 254.52, "protein": 15.04, "fat": 14.3, "carbs": 15.74, "sugar": 0.48, "sodium": 469.87 },
    { "name": "9 Piece Chicken McNuggets", "type": "chicken", "category": "Regular Menu", "calories": 381.77, "protein": 22.56, "fat": 21.46, "carbs": 23.62, "sugar": 0.72, "sodium": 704.81 },
    { "name": "20 Piece Chicken McNuggets", "type": "chicken", "category": "Regular Menu", "calories": 806.1, "protein": 47.6, "fat": 46.9, "carbs": 49.88, "sugar": 1.7, "sodium": 1490.0 },
    { "name": "3 piece Chicken Strips", "type": "chicken", "category": "Regular Menu", "calories": 248.85, "protein": 15.25, "fat": 12.77, "carbs": 17.83, "sugar": 0.0, "sodium": 715.83 },
    { "name": "5 piece Chicken Strips", "type": "chicken", "category": "Regular Menu", "calories": 411.09, "protein": 25.43, "fat": 20.54, "carbs": 29.7, "sugar": 0.0, "sodium": 1193.05 },
    { "name": "Cheesy Veg Nuggets (6pc)", "type": "chicken", "category": "Gourmet Menu", "calories": 382.02, "protein": 13.03, "fat": 20.28, "carbs": 31.19, "sugar": 6.55, "sodium": 279.71 },
    { "name": "Cheesy Veg Nuggets (9pc)", "type": "chicken", "category": "Gourmet Menu", "calories": 599.01, "protein": 13.55, "fat": 36.1, "carbs": 53.71, "sugar": 0.86, "sodium": 1219.19 },
    # type: fries
    { "name": "Regular Fries", "type": "fries", "category": "Regular Menu", "calories": 224.59, "protein": 3.38, "fat": 10.39, "carbs": 27.08, "sugar": 0.39, "sodium": 153.15 },
    { "name": "Medium Fries", "type": "fries", "category": "Regular Menu", "calories": 317.92, "protein": 4.79, "fat": 14.7, "carbs": 38.34, "sugar": 0.55, "sodium": 216.79 },
    { "name": "Large Fries", "type": "fries", "category": "Regular Menu", "calories": 449.17, "protein": 6.76, "fat": 20.77, "carbs": 54.16, "sugar": 0.77, "sodium": 306.29 },
    { "name": "Regular Wedges", "type": "fries", "category": "Regular Menu", "calories": 280.65, "protein": 5.44, "fat": 9.79, "carbs": 42.79, "sugar": 0.48, "sodium": 487.76 },
    { "name": "Large Wedges", "type": "fries", "category": "Regular Menu", "calories": 381.78, "protein": 7.53, "fat": 13.55, "carbs": 54.44, "sugar": 0.66, "sodium": 675.35 },
    { "name": "Hash Brown", "type": "fries", "category": "Breakfast Menu", "calories": 140.29, "protein": 1.03, "fat": 7.32, "carbs": 15.63, "sugar": 0.32, "sodium": 276.26 },
    # type: Carbonated Drinks
    { "name": "Small Coca-Cola", "type": "Carbonated Drinks", "category": "Beverages Menu", "calories": 109.56, "protein": 0.0, "fat": 0.0, "carbs": 27.39, "sugar": 27.39, "sodium": 21.17 },
    { "name": "Medium Coca-Cola", "type": "Carbonated Drinks", "category": "Beverages Menu", "calories": 151.36, "protein": 0.0, "fat": 0.0, "carbs": 37.84, "sugar": 37.84, "sodium": 29.24 },
    { "name": "Large Coca-Cola", "type": "Carbonated Drinks", "category": "Beverages Menu", "calories": 217.36, "protein": 0.0, "fat": 0.0, "carbs": 54.34, "sugar": 54.34, "sodium": 41.99 },
    { "name": "Small Fanta Orange", "type": "Carbonated Drinks", "category": "Beverages Menu", "calories": 129.48, "protein": 0.0, "fat": 0.0, "carbs": 32.37, "sugar": 32.37, "sodium": 55.53 },
    { "name": "Medium Fanta Orange", "type": "Carbonated Drinks", "category": "Beverages Menu", "calories": 178.88, "protein": 0.0, "fat": 0.0, "carbs": 44.72, "sugar": 44.72, "sodium": 76.71 },
    { "name": "Large Fanta Orange", "type": "Carbonated Drinks", "category": "Beverages Menu", "calories": 256.88, "protein": 0.0, "fat": 0.0, "carbs": 64.22, "sugar": 64.22, "sodium": 110.16 },
    { "name": "Small Sprite", "type": "Carbonated Drinks", "category": "Beverages Menu", "calories": 119.52, "protein": 0.0, "fat": 0.0, "carbs": 29.88, "sugar": 29.88, "sodium": 2.02 },
    { "name": "Medium Sprite", "type": "Carbonated Drinks", "category": "Beverages Menu", "calories": 165.12, "protein": 0.0, "fat": 0.0, "carbs": 41.28, "sugar": 41.28, "sodium": 2.79 },
    { "name": "Large Sprite", "type": "Carbonated Drinks", "category": "Beverages Menu", "calories": 237.12, "protein": 0.0, "fat": 0.0, "carbs": 59.28, "sugar": 59.28, "sodium": 4.0 },
    { "name": "Coke Zero Can", "type": "Carbonated Drinks", "category": "Beverages Menu", "calories": 0.1, "protein": 0.0, "fat": 0.0, "carbs": 0.0, "sugar": 0.0, "sodium": 24.75 },
    { "name": "Coke Float", "type": "Carbonated Drinks", "category": "Beverages Menu", "calories": 138.76, "protein": 1.52, "fat": 1.75, "carbs": 29.22, "sugar": 28.23, "sodium": 44.53 },
    { "name": "Fanta Float", "type": "Carbonated Drinks", "category": "Beverages Menu", "calories": 151.56, "protein": 1.52, "fat": 1.75, "carbs": 32.42, "sugar": 31.43, "sodium": 66.61 },
    { "name": "Sprite Float", "type": "Carbonated Drinks", "category": "Beverages Menu", "calories": 145.16, "protein": 1.52, "fat": 1.75, "carbs": 30.82, "sugar": 29.83, "sodium": 47.09 },
    # type: McCafe Drinks
    { "name": "Cold Coffee", "type": "McCafe Drinks", "category": "Beverages Menu", "calories": 301.1, "protein": 9.75, "fat": 11.15, "carbs": 40.2, "sugar": 37.5, "sodium": 175.0 },
    { "name": "Cold Coffee Float", "type": "McCafe Drinks", "category": "Beverages Menu", "calories": 270.05, "protein": 5.91, "fat": 7.18, "carbs": 45.44, "sugar": 36.18, "sodium": 173.59 },
    { "name": "Iced Tea", "type": "McCafe Drinks", "category": "Beverages Menu", "calories": 242.52, "protein": 1.08, "fat": 0.12, "carbs": 59.28, "sugar": 58.08, "sodium": 16.68 },
    { "name": "Masala Chai Regular", "type": "McCafe Drinks", "category": "Beverages Menu", "calories": 110.04, "protein": 0.62, "fat": 2.04, "carbs": 22.31, "sugar": 21.83, "sodium": 60.51 },
    { "name": "Masala Chai Cutting", "type": "McCafe Drinks", "category": "Beverages Menu", "calories": 65.46, "protein": 0.33, "fat": 1.05, "carbs": 13.66, "sugar": 13.05, "sodium": 30.58 },
    { "name": "Minute Maid Pulpy Orange Can", "type": "McCafe Drinks", "category": "Beverages Menu", "calories": 156.0, "protein": 0.0, "fat": 0.0, "carbs": 39.0, "sugar": 36.66, "sodium": 1.0 },
    { "name": "Chocolate Milk Shake", "type": "McCafe Drinks", "category": "Beverages Menu", "calories": 96.0, "protein": 6.53, "fat": 0.6, "carbs": 16.5, "sugar": 16.0, "sodium": 100.0 },
    { "name": "Hot Black Coffee", "type": "McCafe Drinks", "category": "Regular Menu", "calories": 6.8, "protein": 0.0, "fat": 0.0, "carbs": 1.7, "sugar": 0.0, "sodium": 0.0 },
    { "name": "Cappuccino (S)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 136.39, "protein": 7.97, "fat": 7.18, "carbs": 9.98, "sugar": 6.14, "sodium": 111.86 },
    { "name": "Cappuccino (R)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 206.5, "protein": 11.81, "fat": 10.8, "carbs": 15.52, "sugar": 9.25, "sodium": 159.26 },
    { "name": "Cappuccino (L)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 216.15, "protein": 10.91, "fat": 12.01, "carbs": 15.86, "sugar": 9.49, "sodium": 156.09 },
    { "name": "Latte (S)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 128.71, "protein": 7.37, "fat": 5.93, "carbs": 11.47, "sugar": 5.06, "sodium": 110.21 },
    { "name": "Latte (R)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 194.65, "protein": 11.09, "fat": 9.61, "carbs": 15.95, "sugar": 7.56, "sodium": 157.03 },
    { "name": "Latte (L)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 190.03, "protein": 9.1, "fat": 10.42, "carbs": 15.06, "sugar": 8.09, "sodium": 134.29 },
    { "name": "Flat White (S)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 89.98, "protein": 4.14, "fat": 5.14, "carbs": 6.89, "sugar": 4.41, "sodium": 63.64 },
    { "name": "Flat White (R)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 105.24, "protein": 5.41, "fat": 6.06, "carbs": 7.66, "sugar": 5.33, "sodium": 78.4 },
    { "name": "Flat White (L)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 201.47, "protein": 12.08, "fat": 14.02, "carbs": 17.38, "sugar": 12.41, "sodium": 170.87 },
    { "name": "Americano (S)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 6.31, "protein": 1.2, "fat": 0.07, "carbs": 0.22, "sugar": 0.0, "sodium": 2.78 },
    { "name": "Americano (R)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 10.69, "protein": 1.84, "fat": 0.18, "carbs": 0.43, "sugar": 0.0, "sodium": 4.21 },
    { "name": "Americano (L)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 11.01, "protein": 1.61, "fat": 0.24, "carbs": 0.58, "sugar": 0.0, "sodium": 4.75 },
    { "name": "Mocha (S)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 221.59, "protein": 8.64, "fat": 7.03, "carbs": 30.94, "sugar": 13.63, "sodium": 88.97 },
    { "name": "Mocha (R)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 331.42, "protein": 12.85, "fat": 8.86, "carbs": 50.08, "sugar": 20.63, "sodium": 160.31 },
    { "name": "Mocha (L)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 244.0, "protein": 8.99, "fat": 9.91, "carbs": 29.08, "sugar": 18.12, "sodium": 105.97 },
    { "name": "Espresso", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 6.38, "protein": 0.65, "fat": 0.09, "carbs": 0.75, "sugar": 0.6, "sodium": 0.06 },
    { "name": "Macchiato", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 44.9, "protein": 1.91, "fat": 1.9, "carbs": 5.05, "sugar": 2.24, "sodium": 23.92 },
    { "name": "Babychino", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 143.0, "protein": 5.87, "fat": 4.38, "carbs": 19.42, "sugar": 15.42, "sodium": 107.21 },
    { "name": "Hot Chocolate (S)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 229.08, "protein": 7.7, "fat": 7.17, "carbs": 32.49, "sugar": 22.49, "sodium": 169.43 },
    { "name": "Hot Chocolate (R)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 387.39, "protein": 11.01, "fat": 13.07, "carbs": 55.43, "sugar": 40.99, "sodium": 274.64 },
    { "name": "Hot Chocolate (L)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 357.29, "protein": 11.87, "fat": 12.84, "carbs": 47.96, "sugar": 36.43, "sodium": 249.41 },
    { "name": "Premium Dark Hot Chocolate", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 214.21, "protein": 6.15, "fat": 8.15, "carbs": 28.73, "sugar": 13.27, "sodium": 68.26 },
    { "name": "Double Dark Hot Chocolate", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 255.78, "protein": 6.87, "fat": 9.43, "carbs": 34.81, "sugar": 1.35, "sodium": 70.26 },
    { "name": "English Breakfast (S)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 9.93, "protein": 0.56, "fat": 0.28, "carbs": 1.4, "sugar": 0.0, "sodium": 13.84 },
    { "name": "English Breakfast (R)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 11.75, "protein": 0.66, "fat": 0.33, "carbs": 1.65, "sugar": 0.0, "sodium": 16.37 },
    { "name": "English Breakfast (L)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 16.97, "protein": 0.96, "fat": 0.48, "carbs": 2.28, "sugar": 0.0, "sodium": 22.52 },
    { "name": "Moroccon Mint Green Tea (S)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 9.93, "protein": 0.81, "fat": 0.28, "carbs": 1.4, "sugar": 0.0, "sodium": 14.44 },
    { "name": "Moroccon Mint Green Tea (R)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 7.39, "protein": 0.49, "fat": 0.33, "carbs": 1.65, "sugar": 0.0, "sodium": 17.09 },
    { "name": "Moroccon Mint Green Tea (L)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 10.21, "protein": 0.68, "fat": 0.46, "carbs": 2.28, "sugar": 0.0, "sodium": 24.54 },
    { "name": "Strawberry Green Tea (S)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 9.93, "protein": 0.42, "fat": 0.28, "carbs": 1.65, "sugar": 0.0, "sodium": 17.59 },
    { "name": "Strawberry Green Tea (R)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 8.42, "protein": 0.49, "fat": 0.33, "carbs": 1.65, "sugar": 0.0, "sodium": 23.76 },
    { "name": "Strawberry Green Tea (L)", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 11.48, "protein": 0.68, "fat": 0.46, "carbs": 2.28, "sugar": 0.0, "sodium": 23.76 },
    { "name": "Lemon Ice Tea 10 oz", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 121.05, "protein": 0.27, "fat": 0.17, "carbs": 29.53, "sugar": 29.28, "sodium": 9.01 },
    { "name": "Strawberry Ice Tea 10 oz", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 94.69, "protein": 0.16, "fat": 0.16, "carbs": 23.19, "sugar": 20.27, "sodium": 9.72 },
    { "name": "Green Apple Ice Tea 10 oz", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 94.85, "protein": 0.24, "fat": 0.19, "carbs": 23.17, "sugar": 20.29, "sodium": 9.81 },
    { "name": "Iced Coffee 10 oz", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 165.34, "protein": 4.36, "fat": 3.26, "carbs": 29.59, "sugar": 19.94, "sodium": 48.01 },
    { "name": "Cold Coffee Frappe 10 oz", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 331.17, "protein": 4.96, "fat": 14.72, "carbs": 47.02, "sugar": 35.09, "sodium": 189.63 },
    { "name": "Mocha Frappe 10 oz", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 335.96, "protein": 5.49, "fat": 14.01, "carbs": 47.55, "sugar": 36.57, "sodium": 233.52 },
    { "name": "Chocolate Oreo Frappe 10 oz", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 481.11, "protein": 6.03, "fat": 18.91, "carbs": 70.01, "sugar": 55.14, "sodium": 139.97 },
    { "name": "Chocolate Shake 10 oz", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 255.31, "protein": 7.44, "fat": 6.12, "carbs": 44.07, "sugar": 37.08, "sodium": 166.75 },
    { "name": "Mango Smoothie 10 oz", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 219.99, "protein": 4.39, "fat": 5.74, "carbs": 38.28, "sugar": 28.72, "sodium": 88.46 },
    { "name": "Mixed Berry Smoothie 10 oz", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 235.43, "protein": 3.33, "fat": 2.64, "carbs": 51.09, "sugar": 43.05, "sodium": 59.07 },
    { "name": "Raw Mango Cooler 10 oz", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 102.38, "protein": 0.12, "fat": 0.04, "carbs": 25.18, "sugar": 23.13, "sodium": 55.67 },
    { "name": "Mix Berry Cooler 10 oz", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 103.93, "protein": 0.1, "fat": 0.08, "carbs": 25.56, "sugar": 24.62, "sodium": 66.72 },
    { "name": "American Mud Pie Shake", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 389.1, "protein": 9.47, "fat": 11.38, "carbs": 60.78, "sugar": 48.78, "sodium": 9.29 },
    { "name": "Chocolate Shake", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 467.67, "protein": 3.78, "fat": 9.99, "carbs": 90.66, "sugar": 76.95, "sodium": 279.39 },
    { "name": "Strawberry Shake", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 452.34, "protein": 3.57, "fat": 6.66, "carbs": 94.53, "sugar": 68.58, "sodium": 264.36 },
    { "name": "Vanilla Shake", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 402.21, "protein": 4.02, "fat": 10.05, "carbs": 73.92, "sugar": 61.62, "sodium": 277.44 },
    { "name": "Vanilla Oreo Shake", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 554.25, "protein": 13.29, "fat": 17.49, "carbs": 85.92, "sugar": 65.55, "sodium": 393.66 },
    { "name": "Banana Strawberry Shake", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 463.35, "protein": 3.03, "fat": 8.67, "carbs": 93.3, "sugar": 59.61, "sodium": 269.1 },
    { "name": "Sweet Lime Cooler", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 150.78, "protein": 0.38, "fat": 0.13, "carbs": 37.02, "sugar": 24.99, "sodium": 253.92 },
    { "name": "Peach Iced Tea", "type": "McCafe Drinks", "category": "McCafe Menu", "calories": 157.22, "protein": 0.83, "fat": 0.03, "carbs": 38.4, "sugar": 23.68, "sodium": 15.78 },
    # type: McCafe Desserts
    { "name": "Soft Serve Cone", "type": "McCafe Desserts", "category": "Desserts Menu", "calories": 85.73, "protein": 1.99, "fat": 1.82, "carbs": 15.23, "sugar": 10.68, "sodium": 40.78 },
    { "name": "McSwirl ChocoDip", "type": "McCafe Desserts", "category": "Desserts Menu", "calories": 160.14, "protein": 2.71, "fat": 7.14, "carbs": 20.92, "sugar": 15.39, "sodium": 51.31 },
    { "name": "McSwirl ButterScotch Dip", "type": "McCafe Desserts", "category": "Desserts Menu", "calories": 181.2, "protein": 2.82, "fat": 8.11, "carbs": 22.18, "sugar": 16.87, "sodium": 39.67 },
    { "name": "Regular Soft Serve Hot Fudge", "type": "McCafe Desserts", "category": "Desserts Menu", "calories": 121.64, "protein": 2.25, "fat": 4.02, "carbs": 19.11, "sugar": 17.07, "sodium": 65.56 },
    { "name": "Medium Soft Serve Hot Fudge", "type": "McCafe Desserts", "category": "Desserts Menu", "calories": 197.45, "protein": 3.49, "fat": 6.87, "carbs": 30.42, "sugar": 27.01, "sodium": 110.39 },
    { "name": "Regular Soft Serve Strawberry", "type": "McCafe Desserts", "category": "Desserts Menu", "calories": 100.99, "protein": 1.54, "fat": 1.77, "carbs": 19.78, "sugar": 17.66, "sodium": 34.51 },
    { "name": "Medium Soft Serve Strawberry", "type": "McCafe Desserts", "category": "Desserts Menu", "calories": 156.14, "protein": 2.05, "fat": 2.36, "carbs": 31.77, "sugar": 28.2, "sodium": 48.28 },
    { "name": "Regular Soft Serve Brownie Hot Fudge", "type": "McCafe Desserts", "category": "Desserts Menu", "calories": 205.26, "protein": 3.2, "fat": 5.45, "carbs": 35.26, "sugar": 20.75, "sodium": 100.89 },
    { "name": "Medium Soft Serve Brownie Hot Fudge", "type": "McCafe Desserts", "category": "Desserts Menu", "calories": 311.39, "protein": 4.65, "fat": 7.46, "carbs": 55.24, "sugar": 27.94, "sodium": 146.4 },
    { "name": "Small McFlurry Oreo", "type": "McCafe Desserts", "category": "Desserts Menu", "calories": 116.36, "protein": 2.05, "fat": 3.7, "carbs": 18.69, "sugar": 14.49, "sodium": 80.73 },
    { "name": "Regular McFlurry Oreo", "type": "McCafe Desserts", "category": "Desserts Menu", "calories": 209.39, "protein": 3.58, "fat": 6.81, "carbs": 33.42, "sugar": 25.35, "sodium": 150.9 },
    { "name": "Small McFlurry ChocoCrunch", "type": "McCafe Desserts", "category": "Desserts Menu", "calories": 155.19, "protein": 2.62, "fat": 5.39, "carbs": 23.67, "sugar": 17.36, "sodium": 57.8 },
    { "name": "Regular McFlurry ChocoCrunch", "type": "McCafe Desserts", "category": "Desserts Menu", "calories": 703.17, "protein": 10.99, "fat": 19.68, "carbs": 117.78, "sugar": 66.93, "sodium": 295.89 },
    { "name": "Small Black Forest", "type": "McCafe Desserts", "category": "Desserts Menu", "calories": 268.3, "protein": 4.4, "fat": 6.4, "carbs": 47.9, "sugar": 40.5, "sodium": 126.0 },
    { "name": "Regular Black Forest", "type": "McCafe Desserts", "category": "Desserts Menu", "calories": 398.1, "protein": 6.9, "fat": 10.6, "carbs": 68.5, "sugar": 58.7, "sodium": 194.4 },
    { "name": "Medium Blackforest", "type": "McCafe Desserts", "category": "Desserts Menu", "calories": 200.08, "protein": 3.61, "fat": 5.27, "carbs": 33.91, "sugar": 25.04, "sodium": 100.29 },
    { "name": "Nutella Filled Cookie", "type": "McCafe Desserts", "category": "McCafe Menu", "calories": 271.02, "protein": 3.46, "fat": 15.95, "carbs": 25.48, "sugar": 2.45, "sodium": 191.52 },
    { "name": "Vanilla Muffin", "type": "McCafe Desserts", "category": "McCafe Menu", "calories": 325.52, "protein": 2.76, "fat": 15.95, "carbs": 42.73, "sugar": 18.73, "sodium": 301.62 },
    { "name": "Double Chocochips Muffin", "type": "McCafe Desserts", "category": "Regular Menu", "calories": 341.68, "protein": 5.13, "fat": 17.28, "carbs": 40.13, "sugar": 29.44, "sodium": 254.92 },
    { "name": "Vanilla Chocochips Muffin", "type": "McCafe Desserts", "category": "Regular Menu", "calories": 329.29, "protein": 4.48, "fat": 15.46, "carbs": 40.13, "sugar": 29.6, "sodium": 254.92 },
    # type: Condiments
    { "name": "Mustard Dipping Sauce", "type": "Condiments", "category": "Condiments", "calories": 81.18, "protein": 0.52, "fat": 5.57, "carbs": 7.24, "sugar": 6.66, "sodium": 221.32 },
    { "name": "BBQ Dipping Sauce", "type": "Condiments", "category": "Condiments", "calories": 54.89, "protein": 0.26, "fat": 0.49, "carbs": 12.36, "sugar": 7.65, "sodium": 113.23 },
    { "name": "Chilli Sauce", "type": "Condiments", "category": "Condiments", "calories": 7.0, "protein": 0.0, "fat": 0.0, "carbs": 1.7, "sugar": 1.7, "sodium": 55.0 },
    { "name": "Tomato Ketchup Sachets", "type": "Condiments", "category": "Condiments", "calories": 10.0, "protein": 0.0, "fat": 0.0, "carbs": 2.5, "sugar": 2.0, "sodium": 78.8 },
    { "name": "Cheese Slice Extra", "type": "Condiments", "category": "Condiments", "calories": 51.03, "protein": 3.06, "fat": 3.99, "carbs": 0.72, "sugar": 0.54, "sodium": 178.95 },
    { "name": "Milk Tub Creamer", "type": "Condiments", "category": "Condiments", "calories": 14.0, "protein": 0.5, "fat": 1.0, "carbs": 0.8, "sugar": 0.8, "sodium": 7.0 },
    { "name": "Peri-Peri Spice Mix", "type": "Condiments", "category": "Condiments", "calories": 12.0, "protein": 0.3, "fat": 0.23, "carbs": 2.2, "sugar": 0.5, "sodium": 26.5 },
    { "name": "Sugar Sachet", "type": "Condiments", "category": "Condiments", "calories": 20.0, "protein": 0.0, "fat": 0.0, "carbs": 5.0, "sugar": 5.0, "sodium": 0.0 },
    # type: Others
    { "name": "Pizza Puff", "type": "Others", "category": "Regular Menu", "calories": 228.21, "protein": 5.45, "fat": 11.44, "carbs": 24.79, "sugar": 2.73, "sodium": 390.74 },
    { "name": "Ghee Rice with McSpicy Fried Chicken 1pc", "type": "Others", "category": "Regular Menu", "calories": 720.3, "protein": 20.91, "fat": 29.2, "carbs": 77.47, "sugar": 3.28, "sodium": 2399.41 },
    { "name": "L1 Coffee with milk", "type": "Others", "category": "Regular Menu", "calories": 35.8, "protein": 1.0, "fat": 1.2, "carbs": 5.4, "sugar": 0.0, "sodium": 54.6 },
    { "name": "Hot Cake with maple syrup", "type": "Others", "category": "Breakfast Menu", "calories": 432.09, "protein": 8.6, "fat": 18.38, "carbs": 68.01, "sugar": 25.72, "sodium": 619.74 },
    { "name": "Schweppes Packaged Water", "type": "Others", "category": "Beverages Menu", "calories": 0.0, "protein": 0.0, "fat": 0.0, "carbs": 0.0, "sugar": 0.0, "sodium": 3.0 },
    { "name": "Pineapple Fruit Bowl", "type": "Others", "category": "Condiments", "calories": 65.7, "protein": 0.5, "fat": 0.1, "carbs": 15.6, "sugar": 14.5, "sodium": 1.6 }
]
# Convert to a Pandas DataFrame for easier manipulation
df = pd.DataFrame(menu_data)
df_numeric_cols = ['calories', 'protein', 'fat', 'carbs', 'sugar', 'sodium']
for col in df_numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)


# --- State Management ---
# Initialize session state for meal if it doesn't exist
if 'meal' not in st.session_state:
    st.session_state.meal = {}  # Using a dictionary: { 'item_name': quantity }

# --- Helper Functions for Meal Management ---
def add_to_meal(item_name):
    st.session_state.meal[item_name] = st.session_state.meal.get(item_name, 0) + 1

def remove_from_meal(item_name):
    if item_name in st.session_state.meal:
        st.session_state.meal[item_name] -= 1
        if st.session_state.meal[item_name] <= 0:
            del st.session_state.meal[item_name]

def clear_meal():
    st.session_state.meal = {}

# --- Custom CSS for Styling ---
st.markdown("""
<style>
    /* Reduce top padding */
    .st-emotion-cache-1y4p8pa {
        padding-top: 2rem;
    }
    .st-emotion-cache-16txtl3 {
        padding-top: 2rem;
    }
    /* Style for the calorie breakdown bar */
    .macro-bar-container {
        display: flex; height: 25px; border-radius: 8px;
        overflow: hidden; margin-top: 0.5rem;
        background-color: #e0e0e0;
    }
    .macro-bar {
        height: 100%; color: white; text-align: center;
        font-size: 0.8rem; font-weight: bold; line-height: 25px;
        transition: width 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)


# --- UI Layout ---

# Header Section
st.markdown("<h1 style='text-align: center;'>McDonald's <span style='color: #FFC72C;'>India</span> Macro Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic;'>Made by Suneet, cheat meal connoisseur</p>", unsafe_allow_html=True)
st.markdown("---")

# Main Dashboard (Your Meal & Targets) is split into two columns
col_dashboard, col_targets = st.columns([1.5, 1])

with col_dashboard:
    st.subheader("🍔 Your Cheat Meal")
    
    if not st.session_state.meal:
        st.info("Your meal is empty. Add items from the menu below!")
    else:
        # Calculate totals
        total_macros = {key: 0.0 for key in df_numeric_cols}
        for name, quantity in st.session_state.meal.items():
            item_data = df[df['name'] == name].iloc[0]
            for col in df_numeric_cols:
                total_macros[col] += item_data[col] * quantity
        
        # Display current meal items with +/- buttons for quantity adjustment
        for name, quantity in st.session_state.meal.items():
            col1, col2, col3, col4 = st.columns([4, 1, 1, 1])
            with col1: st.write(f"**{name}**")
            with col2: st.write(f"Qty: {quantity}")
            # Use unique keys for buttons to prevent conflicts
            with col3: st.button("➖", key=f"dec_{name}", on_click=remove_from_meal, args=[name])
            with col4: st.button("➕", key=f"inc_{name}", on_click=add_to_meal, args=[name])
        
        st.markdown("---")
        st.subheader("🔥 Total Macros")
        
        # Totals Grid using st.metric for a card-like look
        c1, c2, c3 = st.columns(3)
        c1.metric(label="Calories (kCal)", value=f"{total_macros['calories']:.0f}")
        c2.metric(label="Protein (g)", value=f"{total_macros['protein']:.1f}")
        c3.metric(label="Carbs (g)", value=f"{total_macros['carbs']:.1f}")
        
        c4, c5, c6 = st.columns(3)
        c4.metric(label="Fat (g)", value=f"{total_macros['fat']:.1f}")
        c5.metric(label="Sugar (g)", value=f"{total_macros['sugar']:.1f}")
        c6.metric(label="Sodium (mg)", value=f"{total_macros['sodium']:.0f}")

        # Calorie Breakdown Bar
        st.write("**Calorie Breakdown:**")
        protein_cal = total_macros['protein'] * 4
        carbs_cal = total_macros['carbs'] * 4
        fat_cal = total_macros['fat'] * 9
        total_macro_calories = protein_cal + carbs_cal + fat_cal

        if total_macro_calories > 0:
            p_pct = (protein_cal / total_macro_calories) * 100
            c_pct = (carbs_cal / total_macro_calories) * 100
            f_pct = (fat_cal / total_macro_calories) * 100
            
            # Displaying the bar with HTML for custom styling
            st.markdown(f"""
            <div class="macro-bar-container">
                <div class="macro-bar" style="width: {p_pct}%; background-color: #3498db;">{p_pct:.0f}%</div>
                <div class="macro-bar" style="width: {c_pct}%; background-color: #f1c40f;">{c_pct:.0f}%</div>
                <div class="macro-bar" style="width: {f_pct}%; background-color: #e74c3c;">{f_pct:.0f}%</div>
            </div>
            <div style="display: flex; justify-content: center; gap: 1.5rem; margin-top: 0.5rem; font-size: 0.9rem;">
                <span style="color:#3498db">■ Protein</span>
                <span style="color:#f1c40f">■ Carbs</span>
                <span style="color:#e74c3c">■ Fat</span>
            </div>
            """, unsafe_allow_html=True)
        st.write("") # Spacer
        st.button("Clear Meal", on_click=clear_meal, use_container_width=True, type="primary")

with col_targets:
    st.subheader("🎯 Daily Macro Targets")
    calories_target = st.number_input("Calories Target (kCal)", min_value=0, value=2000, step=50)
    protein_target = st.number_input("Protein Target (g)", min_value=0, value=150, step=5)
    
    # Update progress bars only if a meal has been started
    if st.session_state.meal:
        calories_pct = (total_macros['calories'] / calories_target) if calories_target > 0 else 0
        protein_pct = (total_macros['protein'] / protein_target) if protein_target > 0 else 0
        
        st.write("Calories Progress")
        st.progress(min(calories_pct, 1.0), text=f"{total_macros['calories']:.0f} / {calories_target}")

        st.write("Protein Progress")
        st.progress(min(protein_pct, 1.0), text=f"{total_macros['protein']:.1f}g / {protein_target}g")

st.markdown("---")

# Menu Items Section
st.header("📋 Menu Items")

# Filtering and Sorting Controls
search_query = st.text_input("Search for an item...", placeholder="e.g., McSpicy Paneer")
sort_options = {
    "Default": None, "Calories ↑": ("calories", True), "Calories ↓": ("calories", False),
    "Protein ↑": ("protein", True), "Protein ↓": ("protein", False),
    "Carbs ↑": ("carbs", True), "Carbs ↓": ("carbs", False),
    "Fat ↑": ("fat", True), "Fat ↓": ("fat", False),
}
sort_by = st.selectbox("Sort by:", options=list(sort_options.keys()))

categories = ["All"] + sorted(list(df['type'].unique()))
selected_categories = st.multiselect("Filter by category:", options=categories, default=["All"])


# Apply filters to the DataFrame
filtered_df = df.copy()
if search_query:
    filtered_df = filtered_df[filtered_df['name'].str.contains(search_query, case=False, na=False)]
if "All" not in selected_categories:
    filtered_df = filtered_df[filtered_df['type'].isin(selected_categories)]
if sort_options[sort_by]:
    col, asc = sort_options[sort_by]
    filtered_df = filtered_df.sort_values(by=col, ascending=asc)


# Display Menu Items in a Dynamic Grid
if not filtered_df.empty:
    cols = st.columns(3) # Create a 3-column layout
    for i, item in enumerate(filtered_df.to_dict('records')):
        col = cols[i % 3] # Cycle through the columns
        with col.container(border=True):
            st.markdown(f"**{item['name']}**")
            st.caption(f"{item['type']} | {item['category']}")
            
            # Use columns for a compact macro display
            macro_cols = st.columns(2)
            macro_cols[0].markdown(f"🔥 **{item['calories']:.0f}** kCal")
            macro_cols[0].markdown(f"💪 **{item['protein']:.1f}** g")
            macro_cols[1].markdown(f"🍞 **{item['carbs']:.1f}** g")
            macro_cols[1].markdown(f"🥑 **{item['fat']:.1f}** g")
            
            st.button("Add to Meal", key=item['name'], on_click=add_to_meal, args=[item['name']], use_container_width=True)
else:
    st.warning("No items match your search criteria.")