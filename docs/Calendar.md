# Calendar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**name** | **str** |  | 
**color** | **str** |  | [optional] 
**owner_email** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**visibility** | **str** |  | 
**feed_url** | **str** |  | [optional] 
**event_count** | **int** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from lockally.models.calendar import Calendar

# TODO update the JSON string below
json = "{}"
# create an instance of Calendar from a JSON string
calendar_instance = Calendar.from_json(json)
# print the JSON string representation of the object
print(Calendar.to_json())

# convert the object into a dict
calendar_dict = calendar_instance.to_dict()
# create an instance of Calendar from a dict
calendar_from_dict = Calendar.from_dict(calendar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


