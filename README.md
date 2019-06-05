<img align="right" height="150" src="https://datenworks.com/img/logomarca_datenworks_principal.png">

# Development Code challenge!

Welcome to Datenworks code challenge for developers, this challenge will guide you through a development of a data wrangling application, to check and fix points in a geoshape.

## Problem

Suppose that we're working on a digital transformation for a big retailer. This retailer wants to serve its customers through an e-commerce and then send those clients to the nearest store to check for their bought product (size and specifications) or to withdraw the order.

But, to have those stores available and know its coverage area (to match which store attend that region), we need to register those areas in a database, and ensure that they're valid and working.

### Well, let's try to solve this problem!

## About the Challenge

We'll need your help to create a script that reads the [JSON](files/samples.json), validate and fix (if needed).

The JSON have a format similar to

```javascript
{
  "stores": [ 
    {
        "id": "759f8ef3-d005-4e2c-85cf-f68e026e252f", 
        "coverageArea": { 
          "type": "MultiPolygon", 
          "coordinates": [
            [[[30, 20], [45, 40], [10, 40], [30, 20]]], 
            [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]]
          ]
        },
        "address": { 
          "type": "Point",
          "coordinates": [-46.57421, -21.785741]
        }
    }
  ]
}
```

The sample have the following rules:

- The `address` is defined by the format [`GeoJSON Point`](https://en.wikipedia.org/wiki/GeoJSON)
- All the  `coverageArea` are defined using [`GeoJSON MultiPolygon`](https://en.wikipedia.org/wiki/GeoJSON) 

### 1. Tech Requirements, Docs and Deploy:

* Your project must be **cross-platform**;
* Write a documentation to explain how to execute it;

## Evaluation Method

Your code will be under review of the Datenworks Engineering team.

What we will consider on this evaluation:
- **Performance**
- **Unit and Integration Tests**
- **Ease of maintenance and deployment**
- **Isolation of responsibilities**
- **Software Engineering concerns (cohesion, reusability, etc)**

Feel free to implement it the way you feel more confortable :)

GOOD LUCK!
