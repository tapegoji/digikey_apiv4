# Resistor search using Digikey API. theis code is only for resistor search
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import requests 

class DigiKeyKeyWordSearch:
    def __init__(self, client_id, client_secret, grant_type="client_credentials", normally_stocked=True, in_stock = True, minimum_quantity_available=1):
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type
        self.normally_stocked = normally_stocked
        self.in_stock = in_stock
        self.minimum_quantity_available = minimum_quantity_available
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

    def gen_res_keyword(self, resistance_max, resistance_min, supplier_device_package):
        #lets convert the resistance to mOhms, kOhms, MOhms, GOhms
        # if resistance_max == resistance_min:
        #     resistanc_exact = resistance_max
        #     if resistanc_exact < 1:
        #         res_keyword = str(resistance_max)*1000 + ' mOhms'
        #     elif resistanc_exact < 1e3:
        #         res_keyword = str(resistance_max) + ' Ohms'
        #     elif resistanc_exact < 1e6:
        #         res_keyword = str(resistance_max/1000) + ' kOhms'
        #     elif resistanc_exact < 1e9:
        #         res_keyword = str(resistance_max/1e6) + ' MOhms'
        #     else:
        #         res_keyword = str(resistance_max/1e9) + ' GOhms'
        #     return 'resistor '+ res_keyword + ' ' + supplier_device_package
        # else:
        return 'resistor ' + supplier_device_package

    def gen_cap_keyword(self, capacitance_max, capacitance_min, supplier_device_package):
        #lets convert the capacitance to uF, nF, pF
        # if capacitance_max == capacitance_min:
        #     capacitance_exact = capacitance_max
        #     if capacitance_exact < 0.01e-6:
        #         if capacitance_exact*1e12 < 1:
        #             cap_keyword = "{:.2f}".format(capacitance_max*1e12) + ' pF'
        #         else:
        #             cap_keyword = str(capacitance_max*1e12) + ' pF'
        #     else:
        #         if capacitance_exact*1e6 < 1:
        #             cap_keyword = "{:.2f}".format(capacitance_max*1e6) + ' µF'
        #         else:
        #             cap_keyword = str(capacitance_max*1e6) + ' µF'
        #     return 'capacitor '+ cap_keyword + ' ' + supplier_device_package
        # else:
        return 'capacitor ' + supplier_device_package

    # make the call here
    def call_api(self, keyword_request):
        try:
            # Retrieve Associations for a given product
            api_response = self.api_instance.keyword_search(self.x_digikey_client_id, x_digikey_locale_site=self.x_digikey_locale_site, x_digikey_locale_language=self.x_digikey_locale_language, x_digikey_locale_currency=self.x_digikey_locale_currency, x_digikey_customer_id=self.x_digikey_customer_id, body = keyword_request)
            return api_response
        except ApiException as e:
            print("Exception when calling ProductSearchApi->associations: %s\n" % e)
            return None
    
    def general_search(self, keyword, category_id=None, parameter_filter_request=None, categor_name=None):
        # do a broad search to get the top categories. Only look for parts with status active and the ones that contain the keyword 
        # Build the filter options request
        filter_options_request = swagger_client.FilterOptionsRequest()
        filter_options_request.status_filter = [{'Id': 0}]  # set the status filter to active
        if category_id:
            filter_options_request.category_filter = [{'Id': category_id}]
        if parameter_filter_request:
            filter_options_request.parameter_filter_request = parameter_filter_request
        filter_options_request.minimum_quantity_available = self.minimum_quantity_available
        if self.normally_stocked:
            filter_options_request.search_options = ["NormallyStocking"]
        else:
            filter_options_request.search_options = []
        if self.in_stock:
            filter_options_request.search_options.append("InStock")
        # filter_options_request.manufacturer_filter = [{'Id' :19}]

        # Build body of the request
        keyword_request = swagger_client.KeywordRequest()
        keyword_request.keywords = keyword
        keyword_request.limit = 1
        keyword_request.filter_options_request = filter_options_request
        api_response = self.call_api(keyword_request) # call the api
        print('Total products found:', api_response.products_count)
        # pprint(api_response.products_count)
        if api_response.products_count:
            if parameter_filter_request:
                return api_response.products[0].product_variations[0].digi_key_product_number  # return the digikey part number for the first
        else:
            return 
        if category_id:  # if category id is provided, we will return the api response
            return api_response
        # if category id is not provided, we will get the top categories
        if api_response.filter_options.top_categories:
            for category in api_response.filter_options.top_categories:
                # digikey resisotr category is "Chip Resistor" or "Chip Resistor - Surface Mount"
                if categor_name in category.category.name:
                    return category.category.id
        else:
            print("No top categories found, refine your search by selecting a different keyword")
            exit()     
      
    def resistor_parameter_filter_request(self, category_id, api_response, resistance_max, resistance_min, package_case, supplier_device_package, power_min, tolerance_max, temperature_max, temperature_min):
        # Build the parameter filter request
        category_filter_id = category_id
        parametric_category_list = []

        def add_resistance_filter(filter_option):
            parametric_category = swagger_client.ParametricCategory()
            parametric_category.parameter_id = filter_option.parameter_id
            filter_values_list = []
            for filter_value in filter_option.filter_values:
                try:
                    res_val = float(filter_value.value_name.split(' ')[0])
                    res_unit = filter_value.value_name.split(' ')[1]
                    if 'mOhms' in res_unit:
                        res_val = res_val / 1000
                    elif 'MOhms' in res_unit:
                        res_val = res_val * 1000000
                    elif 'kOhms' in res_unit:
                        res_val = res_val * 1000
                    elif 'GOhms' in res_unit:
                        res_val = res_val * 1000000000
                    if res_val <= resistance_max and res_val >= resistance_min:
                        filter_values_list.append({'Id': filter_value.value_id})
                except:
                    pass
            if filter_values_list:
                parametric_category.filter_values = filter_values_list
                parametric_category_list.append(parametric_category)
                return
            else:
                return "Warning: No filter values found for the given resistance range"

        def add_package_case_filter(filter_option):
            parametric_category = swagger_client.ParametricCategory()
            parametric_category.parameter_id = filter_option.parameter_id
            parametric_category.filter_values = [{'Id': filter_value.value_id} for filter_value in filter_option.filter_values if package_case == filter_value.value_name]
            parametric_category_list.append(parametric_category)
            return 

        def add_supplier_device_package_filter(filter_option):
            parametric_category = swagger_client.ParametricCategory()
            parametric_category.parameter_id = filter_option.parameter_id
            parametric_category.filter_values = [{'Id': filter_value.value_id} for filter_value in filter_option.filter_values if supplier_device_package == filter_value.value_name]
            parametric_category_list.append(parametric_category)
            return

        def add_power_filter(filter_option):
            parametric_category = swagger_client.ParametricCategory()
            parametric_category.parameter_id = filter_option.parameter_id
            filter_values_list = []
            for filter_value in filter_option.filter_values:
                try:
                    res_power = filter_value.value_name.split(' ')[0]
                    if ',' in res_power:
                        res_power = res_power.replace(',', '')
                    if 'W' in res_power:
                        res_power = res_power.split('W')[0]
                    if '/' in res_power:
                        res_power = float(res_power.split('/')[0]) / float(res_power.split('/')[1])
                    else:
                        res_power = float(res_power)
                    if res_power >= power_min:
                        filter_values_list.append({'Id': filter_value.value_id})
                except:
                    pass
            if filter_values_list:
                parametric_category.filter_values = filter_values_list
                parametric_category_list.append(parametric_category)
                return
            else:
                return "Warning: No filter values found for the given power range"

        def add_tolerance_filter(filter_option):
            parametric_category = swagger_client.ParametricCategory()
            parametric_category.parameter_id = filter_option.parameter_id
            filter_values_list = []
            for filter_value in filter_option.filter_values:
                try:
                    tol_val = float(filter_value.value_name.split('%')[0].split('±')[1])
                    if tol_val <= tolerance_max:
                        filter_values_list.append({'Id': filter_value.value_id})
                except:
                    pass
            if filter_values_list:
                parametric_category.filter_values = filter_values_list
                parametric_category_list.append(parametric_category)
                return 
            else:
                return "Warning: No filter values found for the given tolerance range"

        def add_temperature_filter(filter_option):
            parametric_category = swagger_client.ParametricCategory()
            parametric_category.parameter_id = filter_option.parameter_id
            filter_values_list = []
            for filter_value in filter_option.filter_values:
                try:
                    min_temp = int(filter_value.value_name.split('~')[0].split('°C')[0])
                    max_temp = int(filter_value.value_name.split('~')[1].split('°C')[0])
                    if temperature_max <= max_temp and temperature_min >= min_temp:
                        filter_values_list.append({'Id': filter_value.value_id})
                except:
                    pass
            if filter_values_list:
                parametric_category.filter_values = filter_values_list
                parametric_category_list.append(parametric_category)
                return 
            else:
                return "Warning: No filter values found for the given temperature range"

        if api_response.filter_options.parametric_filters:
            for filter_option in api_response.filter_options.parametric_filters:
                if "Resistance" in filter_option.parameter_name:
                    ret_val = add_resistance_filter(filter_option)
                elif "Package" in filter_option.parameter_name or "Case" in filter_option.parameter_name:
                    ret_val = add_package_case_filter(filter_option)
                elif "Supplier Device Package" in filter_option.parameter_name:
                    ret_val = add_supplier_device_package_filter(filter_option)
                elif "Power" in filter_option.parameter_name:
                    ret_val = add_power_filter(filter_option)
                elif "Tolerance" in filter_option.parameter_name:
                    ret_val = add_tolerance_filter(filter_option)
                elif "Operating Temperature" in filter_option.parameter_name:
                    ret_val = add_temperature_filter(filter_option)

                if ret_val:
                    if "Warning" in ret_val:
                        return ret_val
        parameter_filter_request = swagger_client.ParameterFilterRequest()
        parameter_filter_request.category_filter = {'Id': category_filter_id}
        parameter_filter_request.parameter_filters = parametric_category_list
        return parameter_filter_request

    def capacitor_parameter_filter_request(self, category_id, api_response, capacitance_max, capacitance_min, package_case, supplier_device_package, voltage,  tolerance_max, temperature_max, temperature_min):
        # Build the parameter filter request
        category_filter_id = category_id
        parametric_category_list = []

        def add_capacitance_filter(filter_option):
            parametric_category = swagger_client.ParametricCategory()
            parametric_category.parameter_id = filter_option.parameter_id
            filter_values_list = []
            for filter_value in filter_option.filter_values:                
                try:
                    # capacitor values are in thr format of 10 pF or 10 uF
                    cap_val = float(filter_value.value_name.split(' ')[0])
                    cap_unit = filter_value.value_name.split(' ')[1]
                    if 'pF' in cap_unit:
                        cap_val = cap_val / 1e12
                    elif 'µF' in cap_unit:
                        cap_val = cap_val / 1e6
                    if cap_val <= capacitance_max and cap_val >= capacitance_min:
                        filter_values_list.append({'Id': filter_value.value_id})
                except:
                    pass
            if filter_values_list:
                parametric_category.filter_values = filter_values_list
                parametric_category_list.append(parametric_category)
            else:
                return "Warning: No filter values found for the given capacitance range"

        def add_package_case_filter(filter_option):
            parametric_category = swagger_client.ParametricCategory()
            parametric_category.parameter_id = filter_option.parameter_id
            parametric_category.filter_values = [{'Id': filter_value.value_id} for filter_value in filter_option.filter_values if package_case == filter_value.value_name]
            parametric_category_list.append(parametric_category)
            return 

        def add_supplier_device_package_filter(filter_option):
            parametric_category = swagger_client.ParametricCategory()
            parametric_category.parameter_id = filter_option.parameter_id
            parametric_category.filter_values = [{'Id': filter_value.value_id} for filter_value in filter_option.filter_values if supplier_device_package == filter_value.value_name]
            parametric_category_list.append(parametric_category)
            return

        def add_voltage_filter(filter_option):
            parametric_category = swagger_client.ParametricCategory()
            parametric_category.parameter_id = filter_option.parameter_id
            filter_values_list = []
            for filter_value in filter_option.filter_values:
                try:
                    # capacitor values are in thr format of 10V. if there is VAC lets skip it
                    if filter_value.value_name.split('V')[1] == '':
                        rated_voltage = float(filter_value.value_name.split('V')[0])
                        if rated_voltage >= voltage:
                            filter_values_list.append({'Id': filter_value.value_id})
                except:
                    pass
            if filter_values_list:
                parametric_category.filter_values = filter_values_list
                parametric_category_list.append(parametric_category)
            else:
                return "Warning: No filter values found for the given voltage range"

        def add_tolerance_filter(filter_option):
            parametric_category = swagger_client.ParametricCategory()
            parametric_category.parameter_id = filter_option.parameter_id
            filter_values_list = []
            for filter_value in filter_option.filter_values:
                try:
                    tol_val = float(filter_value.value_name.split('%')[0].split('±')[1])
                    if tol_val <= tolerance_max:
                        filter_values_list.append({'Id': filter_value.value_id})
                except:
                    pass
            if filter_values_list:
                parametric_category.filter_values = filter_values_list
                parametric_category_list.append(parametric_category)
            else:
                return "Warning: No filter values found for the given tolerance range"
            
        def add_temperature_filter(filter_option):
            parametric_category = swagger_client.ParametricCategory()
            parametric_category.parameter_id = filter_option.parameter_id
            filter_values_list = []
            for filter_value in filter_option.filter_values:
                try:
                    min_temp = int(filter_value.value_name.split('~')[0].split('°C')[0])
                    max_temp = int(filter_value.value_name.split('~')[1].split('°C')[0])
                    if temperature_max <= max_temp and temperature_min >= min_temp:
                        filter_values_list.append({'Id': filter_value.value_id})
                except:
                    pass
            if filter_values_list:
                parametric_category.filter_values = filter_values_list
                parametric_category_list.append(parametric_category)
            else:
                return "Warning: No filter values found for the given temperature range"
            
        if api_response.filter_options.parametric_filters:
            for filter_option in api_response.filter_options.parametric_filters:
                # for testing lets dump the filter options into a py file to see the structure
                # with open('filter_options.py', 'w') as f:
                #     f.write(str(filter_option))                
                if "Capacitance" in filter_option.parameter_name:
                    ret_val = add_capacitance_filter(filter_option)
                elif "Package" in filter_option.parameter_name or "Case" in filter_option.parameter_name:
                    ret_val = add_package_case_filter(filter_option)
                elif "Voltage - Rated" in filter_option.parameter_name:
                    ret_val = add_voltage_filter(filter_option)
                elif "Tolerance" in filter_option.parameter_name:
                    ret_val = add_tolerance_filter(filter_option)
                elif "Operating Temperature" in filter_option.parameter_name:
                    ret_val = add_temperature_filter(filter_option)

                if ret_val:
                    if "Warning" in ret_val:
                        return ret_val
        parameter_filter_request = swagger_client.ParameterFilterRequest()
        parameter_filter_request.category_filter = {'Id': category_filter_id}
        parameter_filter_request.parameter_filters = parametric_category_list
        return parameter_filter_request
    
    def find_resistor_pn(self, resistance_max, resistance_min, package_case, supplier_device_package, power_min, tolerance_max, temperature_max, temperature_min):
        # lets built a kewrod using resisance, package and supplier device package
        keyword = self.gen_res_keyword(resistance_max, resistance_min, supplier_device_package)
        # do a broad search to get the top categories. Only look for parts with status active and the ones that contain the keyword 
        category_id = self.general_search(keyword, None, None, categor_name='Chip Resistor - Surface Mount')
        # Build the parameter filter request
        parameter_filter_request = self.resistor_parameter_filter_request(category_id, self.general_search(keyword, category_id, None), resistance_max, resistance_min, package_case, supplier_device_package, power_min, tolerance_max, temperature_max, temperature_min)
        if type(parameter_filter_request) == str:
            if "Warning" in parameter_filter_request:
                return parameter_filter_request
        # do a narrow search to get the top categories. Only look for parts with status active and the ones that contain the keyword 
        digikey_pn = self.general_search(keyword, category_id, parameter_filter_request)
        return digikey_pn

    def find_capacitor_pn(self, capacitance_max, capacitance_min, package_case, supplier_device_package, voltage,  tolerance_max, temperature_max, temperature_min):
        # lets built a kewrod using capacitance, package and supplier device package
        keyword = self.gen_cap_keyword(capacitance_max, capacitance_min, supplier_device_package)
        # do a broad search to get the top categories. Only look for parts with status active and the ones that contain the keyword
        category_id = self.general_search(keyword, None, None, categor_name='Ceramic Capacitors')
        if not category_id:
            return "can't find the category for the given keyword"
        # Build the parameter filter request
        parameter_filter_request = self.capacitor_parameter_filter_request(category_id, self.general_search(keyword, category_id, None), capacitance_max, capacitance_min, package_case, supplier_device_package, voltage,  tolerance_max, temperature_max, temperature_min)
        if type(parameter_filter_request) == str:
            if "Warning" in parameter_filter_request:
                return parameter_filter_request
        # do a narrow search to get the top categories. Only look for parts with status active and the ones that contain the keyword
        digikey_pn = self.general_search(keyword, category_id, parameter_filter_request)
        return digikey_pn
    
    def find_inductor_pn(self, inductance_max, inductance_min, package_case, supplier_device_package, current_max, current_min, power_max, power_min, tolerance_max, temperature_max, temperature_min):
        pass

    def find_diode_pn(self, voltage_max, voltage_min, current_max, current_min, power_max, power_min, tolerance_max, temperature_max, temperature_min):
        pass

    def find_transistor_pn(self, voltage_max, voltage_min, current_max, current_min, power_max, power_min, tolerance_max, temperature_max, temperature_min):
        pass
    
    def find_ic_pn(self, voltage_max, voltage_min, current_max, current_min, power_max, power_min, tolerance_max, temperature_max, temperature_min):
        pass

    def find_connector_pn(self, voltage_max, voltage_min, current_max, current_min, power_max, power_min, tolerance_max, temperature_max, temperature_min):
        pass

#####################################################################################################################
# if we run this file directly, we will run the following code
if __name__ == "__main__":
    
    def resisotr_test():
         # make a list from 0.001 to 10e12 in log scale
        # resistance_exact_list = [0.001, 0.01, 0.1, 1, 10, 100, 1e3, 10e3, 100e3, 1e6, 10e6, 100e6, 1e9, 10e9, 100e9, 1e12]
        resistance_exact_list = [10e6]
        for resistance_exact in resistance_exact_list:
            print('Resistance:', resistance_exact)
            if resistance_exact:  # if the exact value is given but not min and max then make them equal
                resistance_max = resistance_exact
                resistance_min = resistance_exact
            else:
                resistance_max = 10           # resistance in ohms
                resistance_min = 1
            package_case = '0603 (1608 Metric)'         # package or case size in Digikey format
            supplier_device_package = '0603'  # supplier device package in Digikey format
            power_min = 0.1             # power in watts
            tolerance_max = 0.25 # tolerance in percentage  # Tolerance in ±%. example 0.25 means ±0.25%
            temperature_max = 155  # temperature range max desired in degree celsius
            temperature_min = -55  # temperature range min desired in degree celsius
            minimum_quantity_available = 1  # minimum quantity available to avoid out of stock parts
            normally_stocked = True  # only show parts that are normally stocked
            in_stock = True  # only show parts that are in stock
            client_id = 'BHAgR5K3PdjmcP3qNq2icY6io0GtQ9f6'  # client id for the Digikey API
            client_secret = 'mGTTaG8fCuJRJyOG'  # client secret for the Digikey API
            kw_search = DigiKeyKeyWordSearch(client_id=client_id, client_secret=client_secret,normally_stocked=normally_stocked, in_stock= in_stock, minimum_quantity_available=minimum_quantity_available)
            
            # call the function to get the part number
            digikey_pn = kw_search.find_resistor_pn(resistance_max, resistance_min, package_case, supplier_device_package, power_min, tolerance_max, temperature_max, temperature_min)
            print('Digikey part number:', digikey_pn)    

    def capacitor_test():
        # capacitance_exact = 10e-9  # capacitance in farads
        capacitance_exact_list = [0.1e-12, 1e-12, 10e-12,100e-12, 1e-9, 10e-9, 100e-9, 1e-6, 10e-6, 100e-6, 1e-3, 10e-3, 100e-3, 1]
        # define the capacitance. it is a very small value so we will use the exact value
        # Noee: it can be a list of values less than 0.1pF
        # capacitance_exact_list = [100000e-12]  
        for capacitance_exact in capacitance_exact_list:
            print('Capacitance:', capacitance_exact)
            if capacitance_exact:
                capacitance_max = capacitance_exact
                capacitance_min = capacitance_exact
            else:
                capacitance_max = 10e-6
                capacitance_min = 1e-6
            package_case = '0603 (1608 Metric)'         # package or case size in Digikey format
            supplier_device_package = '0603'
            voltage = 50
            tolerance_max = 20
            temperature_max = 125
            temperature_min = -55
            minimum_quantity_available = 1
            normally_stocked = True
            in_stock = True
            client_id = 'BHAgR5K3PdjmcP3qNq2icY6io0GtQ9f6'
            client_secret = 'mGTTaG8fCuJRJyOG'
            kw_search = DigiKeyKeyWordSearch(client_id=client_id, client_secret=client_secret,normally_stocked=normally_stocked, in_stock= in_stock, minimum_quantity_available=minimum_quantity_available)

            # call the function to get the part number
            digikey_pn = kw_search.find_capacitor_pn(capacitance_max, capacitance_min, package_case, supplier_device_package, voltage,  tolerance_max, temperature_max, temperature_min)
            print('Digikey part number:', digikey_pn)

# call the capacitor test
    # capacitor_test()
    resisotr_test()