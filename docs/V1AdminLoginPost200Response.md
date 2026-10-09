# V1AdminLoginPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**expires_at** | **datetime** |  | 
**admin** | [**Admin**](Admin.md) |  | 
**tenant** | [**Tenant**](Tenant.md) |  | 

## Example

```python
from lockally.models.v1_admin_login_post200_response import V1AdminLoginPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1AdminLoginPost200Response from a JSON string
v1_admin_login_post200_response_instance = V1AdminLoginPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1AdminLoginPost200Response.to_json())

# convert the object into a dict
v1_admin_login_post200_response_dict = v1_admin_login_post200_response_instance.to_dict()
# create an instance of V1AdminLoginPost200Response from a dict
v1_admin_login_post200_response_from_dict = V1AdminLoginPost200Response.from_dict(v1_admin_login_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


