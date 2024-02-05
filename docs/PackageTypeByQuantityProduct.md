# PackageTypeByQuantityProduct

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommended_quantity** | **int** | Recommended quantity for product | [optional] 
**digi_key_product_number** | **str** | The Digi-Key part number. | [optional] 
**quantity_available** | **int** | Quantity of the product available for immediate sale. | [optional] 
**product_description** | **str** | Catalog description of the product. | [optional] 
**detailed_description** | **str** | Extended catalog description of the product. | [optional] 
**manufacturer_name** | **str** | Manufacturer of the product. | [optional] 
**manufacturer_product_number** | **str** | The manufacturer part number. Note that some manufacturer part numbers may be used by multiple manufacturers for  different parts. | [optional] 
**minimum_order_quantity** | **int** | The minimum quantity to order from Digi-Key. | [optional] 
**primary_datasheet_url** | **str** | The URL to the product&#39;s datasheet. | [optional] 
**primary_photo_url** | **str** | The URL to the product&#39;s image. | [optional] 
**product_status** | **str** | Status of the product. Options include: Active, Obsolete, Discontinued at Digi-Key,  Last Time Buy, Not For New Designs, Preliminary. For obsolete parts the part  will become a non-stocking item when stock is depleted; minimums will apply.  Order the quantity available or the quantity available plus a multiple of the  minimum order quantity.  /// | [optional] 
**manufacturer_lead_weeks** | **str** | The number of weeks expected to receive stock from manufacturer. | [optional] 
**manufacturer_warehouse_quantity** | **int** | Quantity of this product available to order from manufacturer. | [optional] 
**rohs_status** | **str** | RoHS status. Can be RoHS Compliant, RoHS non-compliant, RoHS Compliant By Exemption, Not Applicable, Vendor  undefined, Request Inventory Verification, or ROHS3 Compliant. | [optional] 
**ro_hs_compliant** | **bool** | Boolean value for RoHS compliance. | [optional] 
**quantity_on_order** | **int** | Quantity of this product ordered but not immediately available. | [optional] 
**standard_pricing** | [**list[BreakPrice]**](BreakPrice.md) | Standard pricing for the validated locale. | [optional] 
**my_pricing** | [**list[BreakPrice]**](BreakPrice.md) | My pricing for the validated locale. | [optional] 
**product_url** | **str** | Full URL of the Digi-Key catalog page to purchase the product. This is based on your provided Locale values. | [optional] 
**market_place** | **bool** | Is this product a marketplace product | [optional] 
**supplier** | **str** | Name of product supplier | [optional] 
**stock_note** | **str** | Description of Digi-Key&#39;s current stocking status for the product. Possible values include: In Stock, Temporarily  Out of Stock, and Limited Supply - Call. | [optional] 
**package_types** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


