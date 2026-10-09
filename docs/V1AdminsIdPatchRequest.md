# V1AdminsIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 

## Example

```python
from lockally.models.v1_admins_id_patch_request import V1AdminsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1AdminsIdPatchRequest from a JSON string
v1_admins_id_patch_request_instance = V1AdminsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(V1AdminsIdPatchRequest.to_json())

# convert the object into a dict
v1_admins_id_patch_request_dict = v1_admins_id_patch_request_instance.to_dict()
# create an instance of V1AdminsIdPatchRequest from a dict
v1_admins_id_patch_request_from_dict = V1AdminsIdPatchRequest.from_dict(v1_admins_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


