# swagger-client
ProductSearch Api

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v4
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://developer.digikey.com/support](https://developer.digikey.com/support)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import dk_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import dk_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import dk_api_client
from dk_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeySecurity
configuration = dk_api_client.Configuration()
configuration.api_key['X-DIGIKEY-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-DIGIKEY-Client-Id'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2ApplicationSecurity
configuration = dk_api_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = dk_api_client.ProductSearchApi(dk_api_client.ApiClient(configuration))
product_number = 'product_number_example' # str | The product to retrieve substitutions for.
x_digikey_client_id = 'x_digikey_client_id_example' # str | The Client Id for your App.
x_digikey_locale_site = 'x_digikey_locale_site_example' # str | Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. (optional)
x_digikey_locale_language = 'x_digikey_locale_language_example' # str | Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. (optional)
x_digikey_locale_currency = 'x_digikey_locale_currency_example' # str | Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. (optional)
x_digikey_customer_id = 'x_digikey_customer_id_example' # str | Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. (optional)

try:
    # Retrieve Associations for a given product
    api_response = api_instance.associations(product_number, x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSearchApi->associations: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.digikey.com/products/v4*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ProductSearchApi* | [**associations**](docs/ProductSearchApi.md#associations) | **GET** /search/{productNumber}/associations | Retrieve Associations for a given product
*ProductSearchApi* | [**categories**](docs/ProductSearchApi.md#categories) | **GET** /search/categories | Returns all Product Categories. Category Id can be used in KeywordRequestDto.Filters.TaxonomyIds to restrict a  keyword search to a given category
*ProductSearchApi* | [**categories_by_id**](docs/ProductSearchApi.md#categories_by_id) | **GET** /search/categories/{categoryId} | Returns Category for given Id. Category Id can be used in KeywordRequestDto.Filters.TaxonomyIds to restrict a  keyword search to a given category
*ProductSearchApi* | [**digi_reel_pricing**](docs/ProductSearchApi.md#digi_reel_pricing) | **GET** /search/{productNumber}/digireelpricing | Calculate the DigiReel pricing for the given DigiKeyProductNumber and RequestedQuantity
*ProductSearchApi* | [**keyword_search**](docs/ProductSearchApi.md#keyword_search) | **POST** /search/keyword | KeywordSearch can search for any product in the Digi-Key catalog.
*ProductSearchApi* | [**manufacturers**](docs/ProductSearchApi.md#manufacturers) | **GET** /search/manufacturers | Returns all Product Manufacturers. ManufacturersId can be used in KeywordRequestDto.Filters.ManufacturerIds to  restrict a keyword search to a given Manufacturer
*ProductSearchApi* | [**media**](docs/ProductSearchApi.md#media) | **GET** /search/{productNumber}/media | Retrieve all media for a given product
*ProductSearchApi* | [**package_type_by_quantity**](docs/ProductSearchApi.md#package_type_by_quantity) | **GET** /search/packagetypebyquantity/{productNumber} | Provide a product number and quantity to receive product information such as pricing, available quantity, and the  best  packaging type for the requested quantity of the product.  For example, given a requested quantity larger than a standard reel, this will return information about the  standard tape and reel as well as either cut tape or DKR depending on the provided preference.  Made for Cut Tape, Tape and Reel, and Digi-Reel products only. Other packaging types can be searched for, but  results may vary.  Locale information is required in the headers for accurate pricing and currencies. Locale defaults to United  States.
*ProductSearchApi* | [**product_details**](docs/ProductSearchApi.md#product_details) | **GET** /search/{productNumber}/productdetails | Retrieve detailed product information including real time pricing and availability.
*ProductSearchApi* | [**recommended_products**](docs/ProductSearchApi.md#recommended_products) | **GET** /search/{productNumber}/recommendedproducts | Returns a list of recommended products for the given Product number.
*ProductSearchApi* | [**substitutions**](docs/ProductSearchApi.md#substitutions) | **GET** /search/{productNumber}/substitutions | Retrieve Substitutions for a given product


## Documentation For Models

 - [BaseFilterV3](docs/BaseFilterV3.md)
 - [BaseProduct](docs/BaseProduct.md)
 - [BreakPrice](docs/BreakPrice.md)
 - [CategoriesResponse](docs/CategoriesResponse.md)
 - [Category](docs/Category.md)
 - [CategoryNode](docs/CategoryNode.md)
 - [CategoryResponse](docs/CategoryResponse.md)
 - [Classifications](docs/Classifications.md)
 - [DKProblemDetails](docs/DKProblemDetails.md)
 - [Description](docs/Description.md)
 - [DigiReelPricing](docs/DigiReelPricing.md)
 - [FilterId](docs/FilterId.md)
 - [FilterOptions](docs/FilterOptions.md)
 - [FilterOptionsRequest](docs/FilterOptionsRequest.md)
 - [FilterValue](docs/FilterValue.md)
 - [IsoSearchLocale](docs/IsoSearchLocale.md)
 - [KeywordRequest](docs/KeywordRequest.md)
 - [KeywordResponse](docs/KeywordResponse.md)
 - [Manufacturer](docs/Manufacturer.md)
 - [ManufacturerInfo](docs/ManufacturerInfo.md)
 - [ManufacturersResponse](docs/ManufacturersResponse.md)
 - [MediaLinks](docs/MediaLinks.md)
 - [MediaResponse](docs/MediaResponse.md)
 - [PackageType](docs/PackageType.md)
 - [PackageTypeByQuantityProduct](docs/PackageTypeByQuantityProduct.md)
 - [PackageTypeByQuantityResponse](docs/PackageTypeByQuantityResponse.md)
 - [Parameter](docs/Parameter.md)
 - [ParameterFilterOptionsResponse](docs/ParameterFilterOptionsResponse.md)
 - [ParameterFilterRequest](docs/ParameterFilterRequest.md)
 - [ParameterValue](docs/ParameterValue.md)
 - [ParametricCategory](docs/ParametricCategory.md)
 - [PriceBreak](docs/PriceBreak.md)
 - [Product](docs/Product.md)
 - [ProductAssociations](docs/ProductAssociations.md)
 - [ProductAssociationsResponse](docs/ProductAssociationsResponse.md)
 - [ProductDetails](docs/ProductDetails.md)
 - [ProductStatusV3](docs/ProductStatusV3.md)
 - [ProductSubstitute](docs/ProductSubstitute.md)
 - [ProductSubstitutesResponse](docs/ProductSubstitutesResponse.md)
 - [ProductSummary](docs/ProductSummary.md)
 - [ProductVariation](docs/ProductVariation.md)
 - [Recommendation](docs/Recommendation.md)
 - [RecommendedProduct](docs/RecommendedProduct.md)
 - [RecommendedProductsResponse](docs/RecommendedProductsResponse.md)
 - [Series](docs/Series.md)
 - [Supplier](docs/Supplier.md)
 - [TopCategory](docs/TopCategory.md)
 - [TopCategoryNode](docs/TopCategoryNode.md)


## Documentation For Authorization


## apiKeySecurity

- **Type**: API key
- **API key parameter name**: X-DIGIKEY-Client-Id
- **Location**: HTTP header

## oauth2ApplicationSecurity

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: N/A


## Author

dl_Agile_Team_B2B_API@digikey.com

