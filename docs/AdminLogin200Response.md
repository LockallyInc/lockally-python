# AdminLogin200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**expires_at** | **datetime** |  | 
**admin** | [**Admin**](Admin.md) |  | 
**tenant** | [**Tenant**](Tenant.md) |  | 

## Example

```python
from lockally.models.admin_login200_response import AdminLogin200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AdminLogin200Response from a JSON string
admin_login200_response_instance = AdminLogin200Response.from_json(json)
# print the JSON string representation of the object
print(AdminLogin200Response.to_json())

# convert the object into a dict
admin_login200_response_dict = admin_login200_response_instance.to_dict()
# create an instance of AdminLogin200Response from a dict
admin_login200_response_from_dict = AdminLogin200Response.from_dict(admin_login200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


