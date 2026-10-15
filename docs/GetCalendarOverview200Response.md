# GetCalendarOverview200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_calendars** | **int** |  | [optional] 
**active_calendars** | **int** | Calendars with an event created, edited or held in the last 30 days. | [optional] 
**shared_calendars** | **int** | Calendars visible to the whole organization. | [optional] 
**events_this_month** | **int** | Events on every calendar, in the account&#39;s own timezone. | [optional] 
**upcoming_org_events** | **int** | Future events on organization-visible calendars. | [optional] 
**bookable_resources** | **int** | Resources that are not disabled. | [optional] 
**access_granted** | **int** | People who own a calendar or are named on one. | [optional] 
**access_org_wide** | **int** | Everyone who can see an organization calendar; 0 when none exists. | [optional] 
**activity** | [**List[GetCalendarOverview200ResponseActivityInner]**](GetCalendarOverview200ResponseActivityInner.md) |  | [optional] 

## Example

```python
from lockally.models.get_calendar_overview200_response import GetCalendarOverview200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCalendarOverview200Response from a JSON string
get_calendar_overview200_response_instance = GetCalendarOverview200Response.from_json(json)
# print the JSON string representation of the object
print(GetCalendarOverview200Response.to_json())

# convert the object into a dict
get_calendar_overview200_response_dict = get_calendar_overview200_response_instance.to_dict()
# create an instance of GetCalendarOverview200Response from a dict
get_calendar_overview200_response_from_dict = GetCalendarOverview200Response.from_dict(get_calendar_overview200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


