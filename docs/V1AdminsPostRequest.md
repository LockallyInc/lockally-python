# V1AdminsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**role** | **str** |  | [optional] [default to 'admin']

## Example

```python
from lockally.models.v1_admins_post_request import V1AdminsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1AdminsPostRequest from a JSON string
v1_admins_post_request_instance = V1AdminsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1AdminsPostRequest.to_json())

# convert the object into a dict
v1_admins_post_request_dict = v1_admins_post_request_instance.to_dict()
# create an instance of V1AdminsPostRequest from a dict
v1_admins_post_request_from_dict = V1AdminsPostRequest.from_dict(v1_admins_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


