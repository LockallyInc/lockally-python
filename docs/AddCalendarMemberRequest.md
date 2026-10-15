# AddCalendarMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_email** | **str** |  | 
**role** | **str** |  | [optional] [default to 'viewer']

## Example

```python
from lockally.models.add_calendar_member_request import AddCalendarMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddCalendarMemberRequest from a JSON string
add_calendar_member_request_instance = AddCalendarMemberRequest.from_json(json)
# print the JSON string representation of the object
print(AddCalendarMemberRequest.to_json())

# convert the object into a dict
add_calendar_member_request_dict = add_calendar_member_request_instance.to_dict()
# create an instance of AddCalendarMemberRequest from a dict
add_calendar_member_request_from_dict = AddCalendarMemberRequest.from_dict(add_calendar_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


