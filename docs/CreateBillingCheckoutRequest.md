# CreateBillingCheckoutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | **str** |  | 

## Example

```python
from lockally.models.create_billing_checkout_request import CreateBillingCheckoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBillingCheckoutRequest from a JSON string
create_billing_checkout_request_instance = CreateBillingCheckoutRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBillingCheckoutRequest.to_json())

# convert the object into a dict
create_billing_checkout_request_dict = create_billing_checkout_request_instance.to_dict()
# create an instance of CreateBillingCheckoutRequest from a dict
create_billing_checkout_request_from_dict = CreateBillingCheckoutRequest.from_dict(create_billing_checkout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


