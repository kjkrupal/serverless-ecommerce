# Instructions

## Basic Architecture
![Basic Architecture](docs/product_service.png?raw=true "Products Service Architecture Diagram")


## Commands

```
sam build
```

```
sam deploy --guided
```

POST Request Body:

```
{
    "productCategory":"Electronics",
    "productName":"Kindle",
    "productDescription":"Lauda lasun",
    "productPrice": 20,
    "productPriceCurrency":"USD",
    "productAttributes": {}
}
```