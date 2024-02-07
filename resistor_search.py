# Resistor search using Digikey API. theis code is only for resistor search
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import requests 
class ResistorSearch:
    def __init__(self, client_id, client_secret, grant_type="client_credentials"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type
        self.configuration = swagger_client.Configuration()
        self.configuration.api_key['X-DIGIKEY-Client-Id'] = client_id
        self.configuration.api_key['X-DIGIKEY-Client-Secret'] = client_secret
        self.configuration.access_token = self.get_access_token()
        self.api_instance = swagger_client.ProductSearchApi(swagger_client.ApiClient(self.configuration))
        self.x_digikey_client_id = client_id
        self.x_digikey_locale_site = 'US'
        self.x_digikey_locale_language = 'en'
        self.x_digikey_locale_currency = 'USD'
        self.x_digikey_customer_id = '0'

    def get_access_token(self):
        # Exchange the authorization code for an access token
        token_url = "https://api.digikey.com/v1/oauth2/token"
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": self.grant_type
        }
        response = requests.post(token_url, data=payload)
        if response.status_code == 200:
            return response.json().get("access_token")
        else:
            raise Exception("Failed to get access token")

    def gen_keyword(self, resistance_max, resistance_min, supplier_device_package):
        #lets convert the resistance to mOhms, kOhms, MOhms, GOhms
        if resistance_max == resistance_min:
            resistanc_exact = resistance_max
            if resistanc_exact < 1:
                res_keyword = str(resistance_max)*1000 + ' mOhms'
            elif resistanc_exact < 1e3:
                res_keyword = str(resistance_max) + ' Ohms'
            elif resistanc_exact < 1e6:
                res_keyword = str(resistance_max/1000) + ' kOhms'
            elif resistanc_exact < 1e9:
                res_keyword = str(resistance_max/1e6) + ' MOhms'
            else:
                res_keyword = str(resistance_max/1e9) + ' GOhms'
            return 'resistor '+ res_keyword + ' ' + supplier_device_package
        else:
            return 'resistor ' + supplier_device_package

    # make the call here
    def call_api(self, keyword_request):
        try:
            # Retrieve Associations for a given product
            api_response = self.api_instance.keyword_search(self.x_digikey_client_id, x_digikey_locale_site=self.x_digikey_locale_site, x_digikey_locale_language=self.x_digikey_locale_language, x_digikey_locale_currency=self.x_digikey_locale_currency, x_digikey_customer_id=self.x_digikey_customer_id, body = keyword_request)
            return api_response
        except ApiException as e:
            print("Exception when calling ProductSearchApi->associations: %s\n" % e)
            return None
    
    def general_search(self, keyword, category_id=None, parameter_filter_request=None, minimum_quantity_available=1):
        # do a broad search to get the top categories. Only look for parts with status active and the ones that contain the keyword 
        # Build the filter options request
        filter_options_request = swagger_client.FilterOptionsRequest()
        filter_options_request.status_filter = [{'Id': 0}]  # set the status filter to active
        if category_id:
            filter_options_request.category_filter = [{'Id': category_id}]
        if parameter_filter_request:
            filter_options_request.parameter_filter_request = parameter_filter_request
        filter_options_request.minimum_quantity_available = minimum_quantity_available
        # filter_options_request.manufacturer_filter = [{'Id' :19}]

        # Build body of the request
        keyword_request = swagger_client.KeywordRequest()
        keyword_request.keywords = keyword
        keyword_request.limit = 1
        keyword_request.filter_options_request = filter_options_request
        api_response = self.call_api(keyword_request) # call the api
        print('Total products found:', api_response.products_count)
        # pprint(api_response.products_count)
        if category_id:  # if category id is provided, we will return the api response
            return api_response
        # if category id is not provided, we will get the top categories
        if api_response.filter_options.top_categories:
            for category in api_response.filter_options.top_categories:
                # digikey resisotr category is "Chip Resistor" or "Chip Resistor - Surface Mount"
                if "Chip Resistor" in category.category.name or "Chip Resistor - Surface Mount" in category.category.name:
                    return category.category.id
        else:
            print("No top categories found, refine your search by selecting a different keyword")
            exit()     
      
    def build_parameter_filter_request(self, category_id, api_response, resistance_max, resistance_min, package_case, supplier_device_package, power_min, tolerance_max, temperature_max, temperature_min):
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
                            
                        except:
                            pass 
                    parametric_category.filter_values = filter_values_list
                    parametric_category_list.append(parametric_category)
                
                if "Package" in filter_option.parameter_name or "Case" in filter_option.parameter_name:
                    for filter_value in filter_option.filter_values:
                        if package_case == filter_value.value_name:
                            parametric_category = swagger_client.ParametricCategory()
                            parametric_category.parameter_id = filter_option.parameter_id
                            parametric_category.filter_values = [{'Id' : filter_value.value_id}]
                            parametric_category_list.append(parametric_category)
                
                if "Supplier Device Package" in filter_option.parameter_name:
                    for filter_value in filter_option.filter_values:
                        if supplier_device_package == filter_value.value_name:
                            parametric_category = swagger_client.ParametricCategory()
                            parametric_category.parameter_id = filter_option.parameter_id
                            parametric_category.filter_values = [{'Id' : filter_value.value_id}]
                            parametric_category_list.append(parametric_category)
                            
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
                        except:
                            pass 
                    parametric_category.filter_values = filter_values_list
                    parametric_category_list.append(parametric_category)
        # Build the parameter filter request
        parameter_filter_request = swagger_client.ParameterFilterRequest()
        parameter_filter_request.category_filter = {'Id': category_filter_id}  # cagtory id is the same for
        parameter_filter_request.parameter_filters = parametric_category_list
        return parameter_filter_request

    def do_search(self, resistance_max, resistance_min, package_case, supplier_device_package, power_min, tolerance_max, temperature_max, temperature_min, minimum_quantity_available):
        # lets built a kewrod using resisance, package and supplier device package
        keyword = self.gen_keyword(resistance_max, resistance_min, supplier_device_package)
        # do a broad search to get the top categories. Only look for parts with status active and the ones that contain the keyword 
        category_id = self.general_search(keyword, None, None, minimum_quantity_available)
        # Build the parameter filter request
        parameter_filter_request = self.build_parameter_filter_request(category_id, self.general_search(keyword, category_id, None, minimum_quantity_available), resistance_max, resistance_min, package_case, supplier_device_package, power_min, tolerance_max, temperature_max, temperature_min)
        # do a broad search to get the top categories. Only look for parts with status active and the ones that contain the keyword 
        self.general_search(keyword, category_id, parameter_filter_request, minimum_quantity_available)
#####################################################################################################################
# if we run this file directly, we will run the following code
if __name__ == "__main__":
    res_search = ResistorSearch(client_id='BHAgR5K3PdjmcP3qNq2icY6io0GtQ9f6', client_secret='mGTTaG8fCuJRJyOG')
    resistance_max = 10           # resistance in ohms
    resistance_min = 10
    package_case = '0603 (1608 Metric)'         # package or case size in Digikey format
    supplier_device_package = '0603'  # supplier device package in Digikey format
    power_min = 0.1             # power in watts
    tolerance_max = 0.25 # tolerance in percentage  # Tolerance in ±%. example 0.25 means ±0.25%
    temperature_max = 155  # temperature range max desired in degree celsius
    temperature_min = -55  # temperature range min desired in degree celsius
    minimum_quantity_available = 1  # minimum quantity available to avoid out of stock parts
    # lets built a kewrod using resisance, package and supplier device package
    res_search.do_search(resistance_max, resistance_min, package_case, supplier_device_package, power_min, tolerance_max, temperature_max, temperature_min, minimum_quantity_available)
    print('done')    

