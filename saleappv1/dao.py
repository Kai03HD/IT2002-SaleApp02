def load_categories():
    return [{
            'id': 1,
            'name': 'mobile'
    },{
        'id': 1,
        'name': 'tablet'
    }]
def load_products(kw=None):
    products=[{
        'id': 1,
        'name': "Iphone 15",
        'price': "2000000",
        'image': "https://www.google.com/url?sa=i&url=https%3A%2F%2Fhoanghamobile.com%2Fdien-thoai-di-dong%2Fapple-iphone-15-pro-128gb-chinh-hang-vn-a&psig=AOvVaw2t1nYlu5XdNX9ffvqYfXDN&ust=1698217856584000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCNC-9dKQjoIDFQAAAAAdAAAAABA8",
    },{
        'id': 1,
        'name': "Ipad 15",
        'price': "2000000",
        'image': "https://www.google.com/url?sa=i&url=https%3A%2F%2Fhoanghamobile.com%2Fdien-thoai-di-dong%2Fapple-iphone-15-pro-128gb-chinh-hang-vn-a&psig=AOvVaw2t1nYlu5XdNX9ffvqYfXDN&ust=1698217856584000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCNC-9dKQjoIDFQAAAAAdAAAAABA8",
    },{
        'id': 1,
        'name': "Iphone 15",
        'price': "2000000",
        'image': "https://www.google.com/url?sa=i&url=https%3A%2F%2Fhoanghamobile.com%2Fdien-thoai-di-dong%2Fapple-iphone-15-pro-128gb-chinh-hang-vn-a&psig=AOvVaw2t1nYlu5XdNX9ffvqYfXDN&ust=1698217856584000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCNC-9dKQjoIDFQAAAAAdAAAAABA8",
    },{
        'id': 1,
        'name': "Iphone 15",
        'price': "2000000",
        'image': "https://www.google.com/url?sa=i&url=https%3A%2F%2Fhoanghamobile.com%2Fdien-thoai-di-dong%2Fapple-iphone-15-pro-128gb-chinh-hang-vn-a&psig=AOvVaw2t1nYlu5XdNX9ffvqYfXDN&ust=1698217856584000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCNC-9dKQjoIDFQAAAAAdAAAAABA8",
        }
    ]
    if kw:
        products = [p for p in products if p['name'].find(kw) >=0 ]
    return products
