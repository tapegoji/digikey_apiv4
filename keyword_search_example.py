# testng the swagger file
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import requests 

def get_access_token(client_id, client_secret, grant_type="client_credentials"):
    # Exchange the authorization code for an access token
    token_url = "https://api.digikey.com/v1/oauth2/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": grant_type
    }
    response = requests.post(token_url, data=payload)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        raise Exception("Failed to get access token")
# Configure API key authorization: apiKeySecurity
configuration = swagger_client.Configuration()
configuration.api_key['X-DIGIKEY-Client-Id'] = 'BHAgR5K3PdjmcP3qNq2icY6io0GtQ9f6'
configuration.api_key['X-DIGIKEY-Client-Secret'] = 'mGTTaG8fCuJRJyOG'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-DIGIKEY-Client-Id'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2ApplicationSecurity
configuration.access_token = get_access_token(configuration.api_key['X-DIGIKEY-Client-Id'], configuration.api_key['X-DIGIKEY-Client-Secret'])

# create an instance of the API class 

api_instance = swagger_client.ProductSearchApi(swagger_client.ApiClient(configuration))
x_digikey_client_id = configuration.api_key['X-DIGIKEY-Client-Id']  # str | The Client Id for your App.
x_digikey_locale_site = 'US' # str | Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. (optional)
x_digikey_locale_language = 'en' # str | Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. (optional)
x_digikey_locale_currency = 'USD' # str | Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. (optional)
x_digikey_customer_id = '0' # str | Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. (optional)



# do a broad search to get the top categories. Only look for parts with status active and the ones that contain the keyword 
# Build the filter options request
filter_options_request = swagger_client.FilterOptionsRequest()
filter_options_request.status_filter = [{'Id': 0}]  # set the status filter to active

# Build body of the request
keyword = 'resistor' # str | The product to retrieve substitutions for. This is arbitrary text does not have to be exact
keyword_request = swagger_client.KeywordRequest()
keyword_request.keywords = keyword
keyword_request.limit = 1
keyword_request.filter_options_request = filter_options_request

try:
    # Retrieve Associations for a given product
    api_response = api_instance.keyword_search(x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id, body = keyword_request)   
    pprint(api_response.products_count)    
except ApiException as e:
    print("Exception when calling ProductSearchApi->associations: %s\n" % e)

for category in api_response.filter_options.top_categories:
    if "Chip Resistor" in category.category.name or "Chip Resistor - Surface Mount" in category.category.name:
        category_id = category.category.id

# Now that we have the category id, we can narrow down the search by adding category id to the filter options
        
filter_options_request = swagger_client.FilterOptionsRequest()
filter_options_request.status_filter = [{'Id': 0}]  # set the status filter to active
filter_options_request.category_filter = [{'Id': category_id}]  # set the category filter to resistors

# Build body of the request
keyword = 'resistor' # str | The product to retrieve substitutions for. This is arbitrary text does not have to be exact
keyword_request = swagger_client.KeywordRequest()
keyword_request.keywords = keyword
keyword_request.limit = 1
keyword_request.filter_options_request = filter_options_request

try:
    # Retrieve Associations for a given product
    api_response = api_instance.keyword_search(x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id, body = keyword_request)
    pprint(api_response.products_count)    
except ApiException as e:
    print("Exception when calling ProductSearchApi->associations: %s\n" % e)

# Now check if the api_response.filter_options.parameter_filters is not empty. If it is not empty, then we can use the parameter filters to narrow down the search even further
if api_response.filter_options.parametric_filters:
    for filter_option in api_response.filter_options.parametric_filters:
        if "Resistance" in filter_option.parameter_name:
            resistance_filter_id = filter_option.parameter_id
            resistance_category_filter_id = filter_option.category.id
            break

parametric_filter_id = resistance_filter_id
category_filter_id = resistance_category_filter_id

filter_value = swagger_client.FilterValue()
filter_value.value_id = "10 KOhms"
# filter_value.range_filter_type = ""
# print filter_option into a json file with identation
# with open('filter_option.py', 'w') as f:
#     f.write(filter_option.to_str())
    

# Build the parametric category
parametric_category = swagger_client.ParametricCategory()
parametric_category.parameter_id = parametric_filter_id
parametric_category.filter_values = [{'Id' : '10 kOhms'}] # set the category to resistors


# Build the parameter filter request
parameter_filter_request = swagger_client.ParameterFilterRequest()
parameter_filter_request.category_filter = [{'Id': category_filter_id}]
parameter_filter_request.parameter_filters = parametric_category


# Build the filter options request
filter_options_request = swagger_client.FilterOptionsRequest()
filter_options_request.status_filter = [{'Id': 0}]  # set the status filter to active
filter_options_request.category_filter = [{'Id': category_id}]  # set the category filter to resistors
# filter_options_request.parameter_filter_request = parameter_filter_request
# filter_options_request.manufacturer_filter = [{'Id' :19}]

# Build eht e
keyword_request = swagger_client.KeywordRequest()
keyword_request.keywords = keyword
keyword_request.limit = 10
keyword_request.filter_options_request = filter_options_request

try:
    # Retrieve Associations for a given product
    api_response = api_instance.keyword_search(x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id, body = keyword_request)    
    pprint(api_response.products_count)
    # pprint(api_response.products)
   
except ApiException as e:
    print("Exception when calling ProductSearchApi->associations: %s\n" % e)


print("done")