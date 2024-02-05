# ProductVariation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digi_key_product_number** | **str** | DigiKey Product number of the variation | [optional] 
**package_type** | [**PackageType**](PackageType.md) |  | [optional] 
**standard_pricing** | [**list[PriceBreak]**](PriceBreak.md) | Standard pricing for the validated locale. | [optional] 
**my_pricing** | [**list[PriceBreak]**](PriceBreak.md) | Your pricing for the account with which you authenticated. Also dependent on locale information. | [optional] 
**market_place** | **bool** | Product is a Marketplace product that ships direct from the supplier. A separate shipping fee may apply | [optional] 
**tariff_active** | **bool** | Indicates if there is a tariff on the item. | [optional] 
**supplier** | [**Supplier**](Supplier.md) |  | [optional] 
**quantity_available** | **int** | The quantity available for the specified variation. | [optional] 
**max_quantity_for_distribution** | **int** | Maximum order quantity for Distribution | [optional] 
**minimum_order_quantity** | **int** | The Minimum Order Quantity | [optional] 
**standard_package** | **int** | The number of products in the manufacturer&#39;s standard package. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


