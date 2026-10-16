# CreateBillingCheckout200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_url** | **str** |  | 
**reference** | **str** |  | 

## Example

```python
from lockally.models.create_billing_checkout200_response import CreateBillingCheckout200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBillingCheckout200Response from a JSON string
create_billing_checkout200_response_instance = CreateBillingCheckout200Response.from_json(json)
# print the JSON string representation of the object
print(CreateBillingCheckout200Response.to_json())

# convert the object into a dict
create_billing_checkout200_response_dict = create_billing_checkout200_response_instance.to_dict()
# create an instance of CreateBillingCheckout200Response from a dict
create_billing_checkout200_response_from_dict = CreateBillingCheckout200Response.from_dict(create_billing_checkout200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


