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
**calendar_type** | **str** | What the calendar is for. Separate from visibility, which is who may see it: a team calendar can be open to everyone and a department one restricted to named people. \&quot;personal\&quot; is a person&#39;s own and is not listed in the console&#39;s management table.  | [optional] 
**owner_unit** | **str** | The owning department or office. Empty on a personal calendar, which is owned by owner_email. | [optional] 
**visibility** | **str** |  | 
**access_department** | **str** | Which department may see it, when visibility is \&quot;department\&quot;. Matched against the department recorded on a user, so access follows a person between departments with no membership list to maintain.  | [optional] 
**status** | **str** | Archived keeps the calendar, its events and its feed, and stops it taking new events. | [optional] 
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


