# DirectoryPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **UUID** |  | 
**contact_view_access** | **str** |  | 
**contact_edit_access** | **str** |  | 
**list_manage_access** | **str** |  | 
**external_sharing** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.directory_permissions import DirectoryPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of DirectoryPermissions from a JSON string
directory_permissions_instance = DirectoryPermissions.from_json(json)
# print the JSON string representation of the object
print(DirectoryPermissions.to_json())

# convert the object into a dict
directory_permissions_dict = directory_permissions_instance.to_dict()
# create an instance of DirectoryPermissions from a dict
directory_permissions_from_dict = DirectoryPermissions.from_dict(directory_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


