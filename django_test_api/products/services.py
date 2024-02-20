import requests


def get_products() -> str:

    link = "http://127.0.0.1:8000/products"
    my_req = requests.get(link)
    return my_req.text


def create_product(form) -> str:

    link = "http://127.0.0.1:8000/products"
    values = form.__dict__['cleaned_data']
    my_req = requests.post(link, json=values)

    return my_req.text


def update_product(form, pk: int) -> str:

    link = f"http://127.0.0.1:8000/products?id={pk}"
    values = form.__dict__['cleaned_data']
    my_req = requests.put(link, json=values)

    return my_req.text


def delete_product(pk: int) -> str:

    link = f"http://127.0.0.1:8000/products?id={pk}"
    my_req = requests.delete(link)

    return my_req.text


def get_product(pk: int) -> str:

    link = f"http://127.0.0.1:8000/products/product_id?id={pk}"
    my_req = requests.get(link)
    return my_req.text


def delete_product_all() -> str:

    link = f"http://127.0.0.1:8000/products/delete"
    my_req = requests.delete(link)
    return my_req.text