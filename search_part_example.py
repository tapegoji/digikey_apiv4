# testng the swagger file
from __future__ import print_function
import time
import dk_api_client
from dk_api_client.rest import ApiException
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
configuration = dk_api_client.Configuration()
configuration.api_key['X-DIGIKEY-Client-Id'] = ''
configuration.api_key['X-DIGIKEY-Client-Secret'] = ''
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-DIGIKEY-Client-Id'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2ApplicationSecurity
configuration.access_token = get_access_token(configuration.api_key['X-DIGIKEY-Client-Id'], configuration.api_key['X-DIGIKEY-Client-Secret'])

#    create an instance of the API class
api_instance = dk_api_client.ProductSearchApi(dk_api_client.ApiClient(configuration))
product_number = 'RMCF0603FT10K0DKR-ND' # str | The product to retrieve substitutions for.
x_digikey_client_id = configuration.api_key['X-DIGIKEY-Client-Id']  # str | The Client Id for your App.
x_digikey_locale_site = 'US' # str | Two letter code for Digi-Key product website to search on. Different countries sites have different part restrictions, supported languages, and currencies. Acceptable values include: US, CA, JP, UK, DE, AT, BE, DK, FI, GR, IE, IT, LU, NL, NO, PT, ES, KR, HK, SG, CN, TW, AU, FR, IN, NZ, SE, MX, CH, IL, PL, SK, SI, LV, LT, EE, CZ, HU, BG, MY, ZA, RO, TH, PH. (optional)
x_digikey_locale_language = 'en' # str | Two letter code for language to search on. Langauge must be supported by the selected site. If searching on keyword, this language is used to find matches. Acceptable values include: en, ja, de, fr, ko, zhs, zht, it, es, he, nl, sv, pl, fi, da, no. (optional)
x_digikey_locale_currency = 'USD' # str | Three letter code for Currency to return part pricing for. Currency must be supported by the selected site. Acceptable values include: USD, CAD, JPY, GBP, EUR, HKD, SGD, TWD, KRW, AUD, NZD, INR, DKK, NOK, SEK, ILS, CNY, PLN, CHF, CZK, HUF, RON, ZAR, MYR, THB, PHP. (optional)
x_digikey_customer_id = '0' # str | Your Digi-Key Customer id. If your account has multiple Customer Ids for different regions, this allows you to select one of them. (optional)

try:
    # Retrieve Associations for a given product
    api_response = api_instance.associations(product_number, x_digikey_client_id, x_digikey_locale_site=x_digikey_locale_site, x_digikey_locale_language=x_digikey_locale_language, x_digikey_locale_currency=x_digikey_locale_currency, x_digikey_customer_id=x_digikey_customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductSearchApi->associations: %s\n" % e)