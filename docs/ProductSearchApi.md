# dk_api_client.ProductSearchApi

All URIs are relative to *https://api.digikey.com/products/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associations**](ProductSearchApi.md#associations) | **GET** /search/{productNumber}/associations | Retrieve Associations for a given product
[**categories**](ProductSearchApi.md#categories) | **GET** /search/categories | Returns all Product Categories. Category Id can be used in KeywordRequestDto.Filters.TaxonomyIds to restrict a  keyword search to a given category
[**categories_by_id**](ProductSearchApi.md#categories_by_id) | **GET** /search/categories/{categoryId} | Returns Category for given Id. Category Id can be used in KeywordRequestDto.Filters.TaxonomyIds to restrict a  keyword search to a given category
[**digi_reel_pricing**](ProductSearchApi.md#digi_reel_pricing) | **GET** /search/{productNumber}/digireelpricing | Calculate the DigiReel pricing for the given DigiKeyProductNumber and RequestedQuantity
[**keyword_search**](ProductSearchApi.md#keyword_search) | **POST** /search/keyword | KeywordSearch can search for any product in the Digi-Key catalog.
[**manufacturers**](ProductSearchApi.md#manufacturers) | **GET** /search/manufacturers | Returns all Product Manufacturers. ManufacturersId can be used in KeywordRequestDto.Filters.ManufacturerIds to  restrict a keyword search to a given Manufacturer
[**media**](ProductSearchApi.md#media) | **GET** /search/{productNumber}/media | Retrieve all media for a given product
[**package_type_by_quantity**](ProductSearchApi.md#package_type_by_quantity) | **GET** /search/packagetypebyquantity/{productNumber} | Provide a product number and quantity to receive product information such as pricing, available quantity, and the  best  packaging type for the requested quantity of the product.  For example, given a requested quantity larger than a standard reel, this will return information about the  standard tape and reel as well as either cut tape or DKR depending on the provided preference.  Made for Cut Tape, Tape and Reel, and Digi-Reel products only. Other packaging types can be searched for, but  results may vary.  Locale information is required in the headers for accurate pricing and currencies. Locale defaults to United  States.
[**product_details**](ProductSearchApi.md#product_details) | **GET** /search/{productNumber}/productdetails | Retrieve detailed product information including real time pricing and availability.
[**recommended_products**](ProductSearchApi.md#recommended_products) | **GET** /search/{productNumber}/recommendedproducts | Returns a list of recommended products for the given Product number.
[**substitutions**](ProductSearchApi.md#substitutions) | **GET** /search/{productNumber}/substitutions | Retrieve Substitutions for a given product


# **associations**
> ProductAssociationsResponse associations(product_number, x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)

Retrieve Associations for a given product

Works best with a Digi-Key Product number. Some manufacturer product numbers conflict with unrelated products and may not  return the correct product.  Locale information is required in the headers for accurate pricing and currencies. Locale defaults to United  States.

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_number** | **str**| The product to retrieve substitutions for. | 
 **x_digikey_client_id** | **str**| The Client Id for your App. | 
 **x_digikey_locale_site** | **str**| Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. | [optional] 
 **x_digikey_locale_language** | **str**| Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. | [optional] 
 **x_digikey_locale_currency** | **str**| Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. | [optional] 
 **x_digikey_customer_id** | **str**| Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. | [optional] 

### Return type

[**ProductAssociationsResponse**](ProductAssociationsResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categories**
> CategoriesResponse categories()

Returns all Product Categories. Category Id can be used in KeywordRequestDto.Filters.TaxonomyIds to restrict a  keyword search to a given category

### Example
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

try:
    # Returns all Product Categories. Category Id can be used in KeywordRequestDto.Filters.TaxonomyIds to restrict a  keyword search to a given category
    api_response = api_instance.categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSearchApi->categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CategoriesResponse**](CategoriesResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categories_by_id**
> CategoryResponse categories_by_id(category_id)

Returns Category for given Id. Category Id can be used in KeywordRequestDto.Filters.TaxonomyIds to restrict a  keyword search to a given category

### Example
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
category_id = 56 # int | 

try:
    # Returns Category for given Id. Category Id can be used in KeywordRequestDto.Filters.TaxonomyIds to restrict a  keyword search to a given category
    api_response = api_instance.categories_by_id(category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSearchApi->categories_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 

### Return type

[**CategoryResponse**](CategoryResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **digi_reel_pricing**
> DigiReelPricing digi_reel_pricing(product_number, requested_quantity, x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)

Calculate the DigiReel pricing for the given DigiKeyProductNumber and RequestedQuantity

### Example
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
product_number = 'product_number_example' # str | The Digi-Key ProductNumber requested for Digi-Reel price calculation. It must be a  Digi-Key Product number that is for a Digi-Reel pack type.
requested_quantity = 56 # int | The quantity of the product you are looking to create a Digi-Reel with. Must be greater  than 0.
x_digikey_client_id = 'x_digikey_client_id_example' # str | The Client Id for your App.
x_digikey_locale_site = 'x_digikey_locale_site_example' # str | Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. (optional)
x_digikey_locale_language = 'x_digikey_locale_language_example' # str | Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. (optional)
x_digikey_locale_currency = 'x_digikey_locale_currency_example' # str | Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. (optional)
x_digikey_customer_id = 'x_digikey_customer_id_example' # str | Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. (optional)

try:
    # Calculate the DigiReel pricing for the given DigiKeyProductNumber and RequestedQuantity
    api_response = api_instance.digi_reel_pricing(product_number, requested_quantity, x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSearchApi->digi_reel_pricing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_number** | **str**| The Digi-Key ProductNumber requested for Digi-Reel price calculation. It must be a  Digi-Key Product number that is for a Digi-Reel pack type. | 
 **requested_quantity** | **int**| The quantity of the product you are looking to create a Digi-Reel with. Must be greater  than 0. | 
 **x_digikey_client_id** | **str**| The Client Id for your App. | 
 **x_digikey_locale_site** | **str**| Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. | [optional] 
 **x_digikey_locale_language** | **str**| Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. | [optional] 
 **x_digikey_locale_currency** | **str**| Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. | [optional] 
 **x_digikey_customer_id** | **str**| Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. | [optional] 

### Return type

[**DigiReelPricing**](DigiReelPricing.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keyword_search**
> KeywordResponse keyword_search(x_digikey_client_id, includes=includes, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id, body=body)

KeywordSearch can search for any product in the Digi-Key catalog.

### Example
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
x_digikey_client_id = 'x_digikey_client_id_example' # str | The Client Id for your App.
includes = 'includes_example' # str |  (optional)
x_digikey_locale_site = 'x_digikey_locale_site_example' # str | Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. (optional)
x_digikey_locale_language = 'x_digikey_locale_language_example' # str | Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. (optional)
x_digikey_locale_currency = 'x_digikey_locale_currency_example' # str | Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. (optional)
x_digikey_customer_id = 'x_digikey_customer_id_example' # str | Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. (optional)
body = dk_api_client.KeywordRequest() # KeywordRequest |  (optional)

try:
    # KeywordSearch can search for any product in the Digi-Key catalog.
    api_response = api_instance.keyword_search(x_digikey_client_id, includes=includes, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSearchApi->keyword_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_digikey_client_id** | **str**| The Client Id for your App. | 
 **includes** | **str**|  | [optional] 
 **x_digikey_locale_site** | **str**| Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. | [optional] 
 **x_digikey_locale_language** | **str**| Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. | [optional] 
 **x_digikey_locale_currency** | **str**| Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. | [optional] 
 **x_digikey_customer_id** | **str**| Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. | [optional] 
 **body** | [**KeywordRequest**](KeywordRequest.md)|  | [optional] 

### Return type

[**KeywordResponse**](KeywordResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manufacturers**
> ManufacturersResponse manufacturers(x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency)

Returns all Product Manufacturers. ManufacturersId can be used in KeywordRequestDto.Filters.ManufacturerIds to  restrict a keyword search to a given Manufacturer

### Example
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
x_digikey_client_id = 'x_digikey_client_id_example' # str | The Client Id for your App.
x_digikey_locale_site = 'x_digikey_locale_site_example' # str | Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. (optional)
x_digikey_locale_language = 'x_digikey_locale_language_example' # str | Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. (optional)
x_digikey_locale_currency = 'x_digikey_locale_currency_example' # str | Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. (optional)

try:
    # Returns all Product Manufacturers. ManufacturersId can be used in KeywordRequestDto.Filters.ManufacturerIds to  restrict a keyword search to a given Manufacturer
    api_response = api_instance.manufacturers(x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSearchApi->manufacturers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_digikey_client_id** | **str**| The Client Id for your App. | 
 **x_digikey_locale_site** | **str**| Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. | [optional] 
 **x_digikey_locale_language** | **str**| Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. | [optional] 
 **x_digikey_locale_currency** | **str**| Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. | [optional] 

### Return type

[**ManufacturersResponse**](ManufacturersResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **media**
> MediaResponse media(product_number, x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)

Retrieve all media for a given product

### Example
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
product_number = 'product_number_example' # str | 
x_digikey_client_id = 'x_digikey_client_id_example' # str | The Client Id for your App.
x_digikey_locale_site = 'x_digikey_locale_site_example' # str | Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. (optional)
x_digikey_locale_language = 'x_digikey_locale_language_example' # str | Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. (optional)
x_digikey_locale_currency = 'x_digikey_locale_currency_example' # str | Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. (optional)
x_digikey_customer_id = 'x_digikey_customer_id_example' # str | Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. (optional)

try:
    # Retrieve all media for a given product
    api_response = api_instance.media(product_number, x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSearchApi->media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_number** | **str**|  | 
 **x_digikey_client_id** | **str**| The Client Id for your App. | 
 **x_digikey_locale_site** | **str**| Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. | [optional] 
 **x_digikey_locale_language** | **str**| Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. | [optional] 
 **x_digikey_locale_currency** | **str**| Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. | [optional] 
 **x_digikey_customer_id** | **str**| Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. | [optional] 

### Return type

[**MediaResponse**](MediaResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **package_type_by_quantity**
> PackageTypeByQuantityResponse package_type_by_quantity(product_number, requested_quantity, x_digikey_client_id, packaging_preference=packaging_preference, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)

Provide a product number and quantity to receive product information such as pricing, available quantity, and the  best  packaging type for the requested quantity of the product.  For example, given a requested quantity larger than a standard reel, this will return information about the  standard tape and reel as well as either cut tape or DKR depending on the provided preference.  Made for Cut Tape, Tape and Reel, and Digi-Reel products only. Other packaging types can be searched for, but  results may vary.  Locale information is required in the headers for accurate pricing and currencies. Locale defaults to United  States.

### Example
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
product_number = 'product_number_example' # str | A product number. Can be either Digi-Key or Manufacturer, but some manufacturer product  numbers are ambiguous and will not be found. A DKR product number will override a CT packagingPreference.
requested_quantity = 56 # int | The quantity of the product that you are interested in. This will be used to determined  the quantity to purchase in standard tape and reel, and also in your product preference for the remainder.
x_digikey_client_id = 'x_digikey_client_id_example' # str | The Client Id for your App.
packaging_preference = '' # str | Can be either \"CT\" for Cut Tape or \"DKR\" for Digi-Reel. This will select what package  type to use for the remainder of quantity outside of a standard reel. (optional) (default to )
x_digikey_locale_site = 'x_digikey_locale_site_example' # str | Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. (optional)
x_digikey_locale_language = 'x_digikey_locale_language_example' # str | Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. (optional)
x_digikey_locale_currency = 'x_digikey_locale_currency_example' # str | Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. (optional)
x_digikey_customer_id = 'x_digikey_customer_id_example' # str | Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. (optional)

try:
    # Provide a product number and quantity to receive product information such as pricing, available quantity, and the  best  packaging type for the requested quantity of the product.  For example, given a requested quantity larger than a standard reel, this will return information about the  standard tape and reel as well as either cut tape or DKR depending on the provided preference.  Made for Cut Tape, Tape and Reel, and Digi-Reel products only. Other packaging types can be searched for, but  results may vary.  Locale information is required in the headers for accurate pricing and currencies. Locale defaults to United  States.
    api_response = api_instance.package_type_by_quantity(product_number, requested_quantity, x_digikey_client_id, packaging_preference=packaging_preference, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSearchApi->package_type_by_quantity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_number** | **str**| A product number. Can be either Digi-Key or Manufacturer, but some manufacturer product  numbers are ambiguous and will not be found. A DKR product number will override a CT packagingPreference. | 
 **requested_quantity** | **int**| The quantity of the product that you are interested in. This will be used to determined  the quantity to purchase in standard tape and reel, and also in your product preference for the remainder. | 
 **x_digikey_client_id** | **str**| The Client Id for your App. | 
 **packaging_preference** | **str**| Can be either \&quot;CT\&quot; for Cut Tape or \&quot;DKR\&quot; for Digi-Reel. This will select what package  type to use for the remainder of quantity outside of a standard reel. | [optional] [default to ]
 **x_digikey_locale_site** | **str**| Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. | [optional] 
 **x_digikey_locale_language** | **str**| Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. | [optional] 
 **x_digikey_locale_currency** | **str**| Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. | [optional] 
 **x_digikey_customer_id** | **str**| Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. | [optional] 

### Return type

[**PackageTypeByQuantityResponse**](PackageTypeByQuantityResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_details**
> ProductDetails product_details(product_number, x_digikey_client_id, includes=includes, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)

Retrieve detailed product information including real time pricing and availability.

Works best with a Digi-Key product number. Some manufacturer product numbers conflict with unrelated products and  may not  return the correct product.  Locale information is required in the headers for accurate pricing and currencies. Locale defaults to United  States.

### Example
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
product_number = 'product_number_example' # str | The product to retrieve details for.
x_digikey_client_id = 'x_digikey_client_id_example' # str | The Client Id for your App.
includes = 'includes_example' # str |  (optional)
x_digikey_locale_site = 'x_digikey_locale_site_example' # str | Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. (optional)
x_digikey_locale_language = 'x_digikey_locale_language_example' # str | Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. (optional)
x_digikey_locale_currency = 'x_digikey_locale_currency_example' # str | Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. (optional)
x_digikey_customer_id = 'x_digikey_customer_id_example' # str | Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. (optional)

try:
    # Retrieve detailed product information including real time pricing and availability.
    api_response = api_instance.product_details(product_number, x_digikey_client_id, includes=includes, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSearchApi->product_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_number** | **str**| The product to retrieve details for. | 
 **x_digikey_client_id** | **str**| The Client Id for your App. | 
 **includes** | **str**|  | [optional] 
 **x_digikey_locale_site** | **str**| Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. | [optional] 
 **x_digikey_locale_language** | **str**| Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. | [optional] 
 **x_digikey_locale_currency** | **str**| Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. | [optional] 
 **x_digikey_customer_id** | **str**| Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. | [optional] 

### Return type

[**ProductDetails**](ProductDetails.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recommended_products**
> RecommendedProductsResponse recommended_products(product_number, x_digikey_client_id, limit=limit, search_option_list=search_option_list, exclude_market_place_products=exclude_market_place_products, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency)

Returns a list of recommended products for the given Product number.

### Example
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
product_number = 'product_number_example' # str | The Product being searched for
x_digikey_client_id = 'x_digikey_client_id_example' # str | The Client Id for your App.
limit = 1 # int | The number of records to be returned (optional) (default to 1)
search_option_list = 'search_option_list_example' # str | A comma delimited list of filters that can be used to limit results. Available filters  are the following: LeadFree, CollapsePackingTypes, ExcludeNonStock, Has3DModel, InStock, ManufacturerPartSearch,  NewProductsOnly, RoHSCompliant. (optional)
exclude_market_place_products = false # bool | Used to exclude MarkPlace products from search results. Default is false (optional) (default to false)
x_digikey_locale_site = 'x_digikey_locale_site_example' # str | Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. (optional)
x_digikey_locale_language = 'x_digikey_locale_language_example' # str | Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. (optional)
x_digikey_locale_currency = 'x_digikey_locale_currency_example' # str | Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. (optional)

try:
    # Returns a list of recommended products for the given Product number.
    api_response = api_instance.recommended_products(product_number, x_digikey_client_id, limit=limit, search_option_list=search_option_list, exclude_market_place_products=exclude_market_place_products, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSearchApi->recommended_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_number** | **str**| The Product being searched for | 
 **x_digikey_client_id** | **str**| The Client Id for your App. | 
 **limit** | **int**| The number of records to be returned | [optional] [default to 1]
 **search_option_list** | **str**| A comma delimited list of filters that can be used to limit results. Available filters  are the following: LeadFree, CollapsePackingTypes, ExcludeNonStock, Has3DModel, InStock, ManufacturerPartSearch,  NewProductsOnly, RoHSCompliant. | [optional] 
 **exclude_market_place_products** | **bool**| Used to exclude MarkPlace products from search results. Default is false | [optional] [default to false]
 **x_digikey_locale_site** | **str**| Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. | [optional] 
 **x_digikey_locale_language** | **str**| Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. | [optional] 
 **x_digikey_locale_currency** | **str**| Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. | [optional] 

### Return type

[**RecommendedProductsResponse**](RecommendedProductsResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **substitutions**
> ProductSubstitutesResponse substitutions(product_number, x_digikey_client_id, includes=includes, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)

Retrieve Substitutions for a given product

Works best with a Digi-Key Product number. Some manufacturer product numbers conflict with unrelated products and  may not  return the correct product.  Locale information is required in the headers for accurate pricing and currencies. Locale defaults to United  States.

### Example
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
product_number = 'product_number_example' # str | 
x_digikey_client_id = 'x_digikey_client_id_example' # str | The Client Id for your App.
includes = 'includes_example' # str |  (optional)
x_digikey_locale_site = 'x_digikey_locale_site_example' # str | Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. (optional)
x_digikey_locale_language = 'x_digikey_locale_language_example' # str | Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. (optional)
x_digikey_locale_currency = 'x_digikey_locale_currency_example' # str | Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. (optional)
x_digikey_customer_id = 'x_digikey_customer_id_example' # str | Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. (optional)

try:
    # Retrieve Substitutions for a given product
    api_response = api_instance.substitutions(product_number, x_digikey_client_id, includes=includes, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSearchApi->substitutions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_number** | **str**|  | 
 **x_digikey_client_id** | **str**| The Client Id for your App. | 
 **includes** | **str**|  | [optional] 
 **x_digikey_locale_site** | **str**| Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. | [optional] 
 **x_digikey_locale_language** | **str**| Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. | [optional] 
 **x_digikey_locale_currency** | **str**| Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. | [optional] 
 **x_digikey_customer_id** | **str**| Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. | [optional] 

### Return type

[**ProductSubstitutesResponse**](ProductSubstitutesResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

