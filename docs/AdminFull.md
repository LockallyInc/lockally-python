# AdminFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**email** | **str** |  | 
**display_name** | **str** |  | [optional] 
**role** | **str** |  | 
**last_login_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**disabled** | **bool** |  | 
**disabled_at** | **datetime** |  | [optional] 
**password** | **str** | Present ONLY on POST response when lockally generated the password. Shown once. | [optional] 

## Example

```python
from lockally.models.admin_full import AdminFull

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFull from a JSON string
admin_full_instance = AdminFull.from_json(json)
# print the JSON string representation of the object
print(AdminFull.to_json())

# convert the object into a dict
admin_full_dict = admin_full_instance.to_dict()
# create an instance of AdminFull from a dict
admin_full_from_dict = AdminFull.from_dict(admin_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


