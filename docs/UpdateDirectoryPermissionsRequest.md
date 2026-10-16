# UpdateDirectoryPermissionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_view_access** | **str** |  | [optional] 
**contact_edit_access** | **str** |  | [optional] 
**list_manage_access** | **str** |  | [optional] 
**external_sharing** | **str** |  | [optional] 

## Example

```python
from lockally.models.update_directory_permissions_request import UpdateDirectoryPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDirectoryPermissionsRequest from a JSON string
update_directory_permissions_request_instance = UpdateDirectoryPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDirectoryPermissionsRequest.to_json())

# convert the object into a dict
update_directory_permissions_request_dict = update_directory_permissions_request_instance.to_dict()
# create an instance of UpdateDirectoryPermissionsRequest from a dict
update_directory_permissions_request_from_dict = UpdateDirectoryPermissionsRequest.from_dict(update_directory_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


