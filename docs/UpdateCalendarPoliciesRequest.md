# UpdateCalendarPoliciesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_meeting_duration_mins** | **int** |  | [optional] 
**working_hours_start** | **str** |  | [optional] 
**working_hours_end** | **str** |  | [optional] 
**booking_window_days** | **int** |  | [optional] 
**recurring_meeting_limit** | **int** |  | [optional] 
**resource_approval_mode** | **str** |  | [optional] 
**external_invites_allowed** | **bool** |  | [optional] 
**external_sharing_allowed** | **bool** |  | [optional] 
**public_links_enabled** | **bool** |  | [optional] 

## Example

```python
from lockally.models.update_calendar_policies_request import UpdateCalendarPoliciesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCalendarPoliciesRequest from a JSON string
update_calendar_policies_request_instance = UpdateCalendarPoliciesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCalendarPoliciesRequest.to_json())

# convert the object into a dict
update_calendar_policies_request_dict = update_calendar_policies_request_instance.to_dict()
# create an instance of UpdateCalendarPoliciesRequest from a dict
update_calendar_policies_request_from_dict = UpdateCalendarPoliciesRequest.from_dict(update_calendar_policies_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


