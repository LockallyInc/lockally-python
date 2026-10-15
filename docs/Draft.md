# Draft


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**mailbox_id** | **UUID** |  | 
**mailbox** | **str** |  | [optional] 
**thread_id** | **UUID** |  | [optional] 
**to** | **List[str]** |  | 
**cc** | **List[str]** |  | [optional] 
**subject** | **str** |  | [optional] 
**body_text** | **str** |  | [optional] 
**status** | **str** |  | 
**policy_flags** | **Dict[str, object]** |  | 
**reviewed_at** | **datetime** |  | [optional] 
**sent_message_id** | **UUID** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from lockally.models.draft import Draft

# TODO update the JSON string below
json = "{}"
# create an instance of Draft from a JSON string
draft_instance = Draft.from_json(json)
# print the JSON string representation of the object
print(Draft.to_json())

# convert the object into a dict
draft_dict = draft_instance.to_dict()
# create an instance of Draft from a dict
draft_from_dict = Draft.from_dict(draft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


