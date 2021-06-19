# Instructions

Commands:

```
sam build
```

```
sam deploy --guided
```

POST Request Body:

```
create product body
{
    "productCategory":"Electronics",
    "productName":"Kindle",
    "productDescription":"Lauda lasun",
    "productPrice": 20,
    "productPriceCurrency":"USD",
    "productAttributes": {}
}

update product body
{
    "product_id":"737d75f2-33d5-4377-b25f-dee9dfbebf76",
    "productCategory":"Electronics",
    "productName":"Kindle",
    "productDescription":"Lauda lasun",
    "productPrice": 20,
    "productPriceCurrency":"USD",
    "productAttributes": {}
}
```