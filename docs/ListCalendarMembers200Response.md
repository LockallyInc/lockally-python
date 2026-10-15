# ListCalendarMembers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CalendarMember]**](CalendarMember.md) |  | [optional] 

## Example

```python
from lockally.models.list_calendar_members200_response import ListCalendarMembers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListCalendarMembers200Response from a JSON string
list_calendar_members200_response_instance = ListCalendarMembers200Response.from_json(json)
# print the JSON string representation of the object
print(ListCalendarMembers200Response.to_json())

# convert the object into a dict
list_calendar_members200_response_dict = list_calendar_members200_response_instance.to_dict()
# create an instance of ListCalendarMembers200Response from a dict
list_calendar_members200_response_from_dict = ListCalendarMembers200Response.from_dict(list_calendar_members200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


