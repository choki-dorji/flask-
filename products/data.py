def get_products(category=None, search_query=None):
    products = [
        {
            "id": "1",
            "name": "Product 1",
            "description": "Description of Product 1",
            "price": 100,
            "category": "daisy",
            "image_uri": "static/images/daisy1.jpg",
            "start": 5,
            "quantity": 10
        },
        {
            "id": "2",
            "name": "Product 2",
            "description": "Description of Product 2",
            "price": 200,
            "category": "rose",
            "image_uri": "static/images/rose3.jpg",
            "start": 4,
            "quantity": 20
        },
        {
            "id": "3",
            "name": "Product 3",
            "description": "Description of Product 3",
            "price": 300,
            "category": "orchid",
            "image_uri": "static/images/orchid1.jpg",
            "start": 3,
            "quantity": 30
        },
        {
            "id": "4",
            "name": "Product 4",
            "description": "Description of Product 4",
            "price": 400,
            "category": "daisy",
            "image_uri": "static/images/daisy4.jpg",
            "start": 4,
            "quantity": 40
        },
        {
            "id": "5",
            "name": "Product 5",
            "description": "Description of Product 5",
            "price": 500,
            "category": "rose",
            "image_uri": "static/images/rose3.jpg",
            "start": 5,
            "quantity": 50
        },
        {
            "id": "6",
            "name": "Product 6",
            "description": "Description of Product 6",
            "price": 600,
            "category": "daisy",
            "image_uri": "static/images/daisy2.jpg",
            "start": 3,
            "quantity": 60
        },
        {
            "id": "7",
            "name": "Product 7",
            "description": "Description of Product 7",
            "price": 700,
            "category": "orchid",
            "image_uri": "static/images/orchid2.jpg",
            "start": 5,
            "quantity": 70
        },
        {
            "id": "8",
            "name": "Product 8",
            "description": "Description of Product 8",
            "price": 800,
            "category": "orchid",
            "image_uri": "static/images/orchid3.jpg",
            "start": 5,
            "quantity": 80
        },
        {
            "id": "9",
            "name": "Product 9",
            "description": "Description of Product 9",
            "price": 900,
            "category": "rose",
            "image_uri": "static/images/rose1.jpg",
            "start": 5,
            "quantity": 90
        },
        {
            "id": "10",
            "name": "Product 10",
            "description": "Description of Product 10",
            "price": 1000,
            "category": "rose",
            "image_uri": "static/images/rose5.jpg",
            "start": 4,
            "quantity": 100
        },
        {
            "id": "11",
            "name": "Product 11",
            "description": "Description of Product 11",
            "price": 1100,
            "category": "daisy",
            "image_uri": "static/images/daisy3.jpg",
            "start": 5,
            "quantity": 110
        },
        {
            "id": "12",
            "name": "Product 12",
            "description": "Description of Product 12",
            "price": 1200,
            "category": "rose",
            "image_uri": "static/images/rose7.jpg",
            "start": 5,
            "quantity": 120
        },
        {
            "id": "13",
            "name": "Product 13",
            "description": "Description of Product 13",
            "price": 1300,
            "category": "rose",
            "image_uri": "static/images/rose8.jpg",
            "start": 5,
            "quantity": 130
        },
        {
            "id": "14",
            "name": "Product 14",
            "description": "Description of Product 14",
            "price": 1400,
            "category": "rose",
            "image_uri": "static/images/rose10.jpg",
            "start": 5,
            "quantity": 140
        },
        {
            "id": "15",
            "name": "Product 15",
            "description": "Description of Product 15",
            "price": 1500,
            "category": "daisy",
            "image_uri": "static/images/daisy4.jpg",
            "start": 5,
            "quantity": 150
        },
        {
            "id": "16",
            "name": "Product 16",
            "description": "Description of Product 16",
            "price": 1600,
            "category": "orchid",
            "image_uri": "static/images/orchid3.jpg",
            "start": 5,
            "quantity": 160
        },
        {
            "id": "17",
            "name": "Product 17",
            "description": "Description of Product 17",
            "price": 1700,
            "category": "rose",
            "image_uri": "static/images/f1.png",
            "start": 5,
            "quantity": 170
        },
        {
            "id": "18",
            "name": "Product 18",
            "description": "Description of Product 18",
            "price": 1800,
            "category": "orchid",
            "image_uri": "static/images/orchid5.jpg",
            "start": 5,
            "quantity": 180
        },
        {
            "id": "19",
            "name": "Product 19",
            "description": "Description of Product 19",
            "price": 1900,
            "category": "daisy",
            "image_uri": "static/images/daisy1.jpg",
            "start": 5,
            "quantity": 190
        },
        {
            "id": "20",
            "name": "Product 20",
            "description": "Description of Product 20",
            "price": 2000,
            "category": "rose",
            "image_uri": "static/images/rose5.jpg",
            "start": 5,
            "quantity": 200
        }
    ]
    if category:
        products = [ product for product in products if product["category"] == category]
    
    if search_query:
          products = [product for product in products if search_query.lower() in product['name'].lower() or search_query.lower() in product['description'].lower()]
    return products
