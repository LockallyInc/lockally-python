# V1AdminLoginPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from lockally.models.v1_admin_login_post_request import V1AdminLoginPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1AdminLoginPostRequest from a JSON string
v1_admin_login_post_request_instance = V1AdminLoginPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1AdminLoginPostRequest.to_json())

# convert the object into a dict
v1_admin_login_post_request_dict = v1_admin_login_post_request_instance.to_dict()
# create an instance of V1AdminLoginPostRequest from a dict
v1_admin_login_post_request_from_dict = V1AdminLoginPostRequest.from_dict(v1_admin_login_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


