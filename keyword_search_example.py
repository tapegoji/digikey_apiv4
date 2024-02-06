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
with open('keyword_request_1.py', 'w') as f:
    f.write(keyword_request.to_str())
with open('api_response_1.py', 'w') as f:
    f.write(api_response.to_str())

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
with open('keyword_request_2.py', 'w') as f:
    f.write(keyword_request.to_str())
with open('api_response_2.py', 'w') as f:
    f.write(api_response.to_str())




### Now that we have the category id, we can narrow down the search by adding category id to the filter options
resistance_max = 10e3           # resistance in ohms
resistance_min = 10e3
package_case = '0603 (1608 Metric)'         # package or case size in Digikey format
supplier_device_package = '0603'  # supplier device package in Digikey format
power_min = 0.1             # power in watts
tolerance_max = 0.25 # tolerance in percentage  # Tolerance in ±%. example 0.25 means ±0.25%
temperature_max = 155  # temperature range max desired in degree celsius
temperature_min = -55  # temperature range min desired in degree celsius
minimum_quantity_available = 1  # minimum quantity available to avoid out of stock parts


# Build the parameter filter request
category_filter_id = category_id
parametric_category_list = []
parametric_category = swagger_client.ParametricCategory()
if api_response.filter_options.parametric_filters:
    for filter_option in api_response.filter_options.parametric_filters:
        if "Resistance" in filter_option.parameter_name:
            parametric_category = swagger_client.ParametricCategory()
            parametric_category.parameter_id = filter_option.parameter_id
            filter_values_list = []
            for filter_value in filter_option.filter_values:
                # the value can be like  mOhms,  Ohms,  MOhms,  kOhms,  GOhms if its in not in the format 10 Ohms, we will calculate the value
                try:
                    res_val = float(filter_value.value_name.split(' ')[0])
                    res_unit = filter_value.value_name.split(' ')[1]
                    # now lets take a look at the unit
                    if 'mOhms' in res_unit:
                        res_val = res_val / 1000
                    elif 'MOhms' in res_unit:
                        res_val = res_val * 1000000
                    elif 'kOhms' in res_unit:
                        res_val = res_val * 1000
                    elif 'GOhms' in res_unit:
                        res_val = res_val * 1000000000
                    if res_val <= resistance_max  and res_val >= resistance_min:
                        filter_values_list.append({'Id' : filter_value.value_id})
                        # pprint(parametric_category_list)
                    
                except:
                    pass 
            parametric_category.filter_values = filter_values_list
            parametric_category_list.append(parametric_category)
        
        if "Package" in filter_option.parameter_name or "Case" in filter_option.parameter_name:
            for filter_value in filter_option.filter_values:
                if package_case == filter_value.value_name:
                    parametric_category = swagger_client.ParametricCategory()  # Create a new instance of ParametricCategory
                    parametric_category.parameter_id = filter_option.parameter_id
                    parametric_category.filter_values = [{'Id' : filter_value.value_id}]
                    parametric_category_list.append(parametric_category)
                    # pprint(parametric_category_list)
        if "Supplier Device Package" in filter_option.parameter_name:
            for filter_value in filter_option.filter_values:
                if supplier_device_package == filter_value.value_name:
                    parametric_category = swagger_client.ParametricCategory()
                    parametric_category.parameter_id = filter_option.parameter_id
                    parametric_category.filter_values = [{'Id' : filter_value.value_id}]
                    parametric_category_list.append(parametric_category)
                    # pprint(parametric_category_list)
    
        if "Power" in filter_option.parameter_name:
            parametric_category = swagger_client.ParametricCategory()
            parametric_category.parameter_id = filter_option.parameter_id
            filter_values_list = []
            for filter_value in filter_option.filter_values:
                try:
                    # power is in term of 0.1W, 1/10W we want to first split based on the space and comma and then remove W from it. if it is in form of 1/10 then convert it to float
                    res_power = filter_value.value_name.split(' ')[0]
                    # if there is  a comma in the value, we will remvoe the comma
                    if ',' in res_power:
                        res_power = res_power.replace(',', '')
                    # if there is W in the value, we will remove it too
                    if 'W' in res_power:
                        res_power = res_power.split('W')[0]
                    if '/' in res_power:
                        res_power = float(res_power.split('/')[0]) / float(res_power.split('/')[1])
                    else:
                        res_power = float(res_power)
                    if res_power >= power_min :
                        filter_values_list.append({'Id' : filter_value.value_id})
                        # pprint(parametric_category_list)
                except:
                    pass
            parametric_category.filter_values = filter_values_list
            parametric_category_list.append(parametric_category)
        
        if "Tolerance" in filter_option.parameter_name:
            parametric_category = swagger_client.ParametricCategory()
            parametric_category.parameter_id = filter_option.parameter_id
            filter_values_list = []
            for filter_value in filter_option.filter_values:
                # the value is ±30% so we split it and get the value in float
                try:
                    tol_val = float(filter_value.value_name.split('%')[0].split('±')[1])                
                    if tol_val <= tolerance_max:
                        filter_values_list.append({'Id' : filter_value.value_id})
                        # pprint(parametric_category_list)
                except:
                    pass
            parametric_category.filter_values = filter_values_list
            parametric_category_list.append(parametric_category)
        
        if "Operating Temperature" in filter_option.parameter_name:
            parametric_category = swagger_client.ParametricCategory()
            parametric_category.parameter_id = filter_option.parameter_id
            filter_values_list = []
            for filter_value in filter_option.filter_values:
                # value_name is like -55°C ~ 155°C. we split it and get the max temperature and min temperature in integer
                try:
                    min_temp = int(filter_value.value_name.split('~')[0].split('°C')[0])
                    max_temp = int(filter_value.value_name.split('~')[1].split('°C')[0])   
                    if temperature_max <= max_temp and temperature_min >= min_temp:  # remove oc from the value name
                        filter_values_list.append({'Id' : filter_value.value_id})
                        # pprint(parametric_category_list)
                except:
                    pass 
            parametric_category.filter_values = filter_values_list
            parametric_category_list.append(parametric_category)

# Build the parameter filter request
parameter_filter_request = swagger_client.ParameterFilterRequest()
parameter_filter_request.category_filter = {'Id': category_filter_id}  # cagtory id is the same for
parameter_filter_request.parameter_filters = parametric_category_list


# Build the filter options request
filter_options_request = swagger_client.FilterOptionsRequest()
filter_options_request.status_filter = [{'Id': 0}]  # set the status filter to active
filter_options_request.category_filter = [{'Id': category_id}]  # set the category filter to resistors
filter_options_request.parameter_filter_request = parameter_filter_request
filter_options_request.minimum_quantity_available = minimum_quantity_available
# filter_options_request.manufacturer_filter = [{'Id' :19}]

# Build eht e
keyword_request = swagger_client.KeywordRequest()
keyword_request.keywords = keyword
keyword_request.limit = 10
keyword_request.filter_options_request = filter_options_request
with open('keyword_request_3.py', 'w') as f:
    f.write(keyword_request.to_str())
try:
    # Retrieve Associations for a given product
    api_response = api_instance.keyword_search(x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id, body = keyword_request)    
    pprint(api_response.products_count)
    # pprint(api_response.products)
   
except ApiException as e:
    print("Exception when calling ProductSearchApi->associations: %s\n" % e)

with open('api_response_3.py', 'w') as f:
    f.write(api_response.to_str())

print("done")


''''
with open('body_3.py', 'w') as f:
    f.write(body.to_str())
'''