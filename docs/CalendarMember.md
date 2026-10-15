# CalendarMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**calendar_id** | **UUID** |  | 
**tenant_id** | **UUID** |  | 
**user_email** | **str** |  | 
**role** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from lockally.models.calendar_member import CalendarMember

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarMember from a JSON string
calendar_member_instance = CalendarMember.from_json(json)
# print the JSON string representation of the object
print(CalendarMember.to_json())

# convert the object into a dict
calendar_member_dict = calendar_member_instance.to_dict()
# create an instance of CalendarMember from a dict
calendar_member_from_dict = CalendarMember.from_dict(calendar_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


