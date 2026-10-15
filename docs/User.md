# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**email** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**title** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**status** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**mailbox_count** | **int** |  | [optional] 

## Example

```python
from lockally.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


