# UpdateAdminRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 

## Example

```python
from lockally.models.update_admin_request import UpdateAdminRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminRequest from a JSON string
update_admin_request_instance = UpdateAdminRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminRequest.to_json())

# convert the object into a dict
update_admin_request_dict = update_admin_request_instance.to_dict()
# create an instance of UpdateAdminRequest from a dict
update_admin_request_from_dict = UpdateAdminRequest.from_dict(update_admin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


