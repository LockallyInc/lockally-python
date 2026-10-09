# UserEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**event_at** | **datetime** |  | [optional] 
**days_inactive** | **int** |  | [optional] 

## Example

```python
from lockally.models.user_event import UserEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UserEvent from a JSON string
user_event_instance = UserEvent.from_json(json)
# print the JSON string representation of the object
print(UserEvent.to_json())

# convert the object into a dict
user_event_dict = user_event_instance.to_dict()
# create an instance of UserEvent from a dict
user_event_from_dict = UserEvent.from_dict(user_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


