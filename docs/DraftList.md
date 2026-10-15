# DraftList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drafts** | [**List[Draft]**](Draft.md) |  | 

## Example

```python
from lockally.models.draft_list import DraftList

# TODO update the JSON string below
json = "{}"
# create an instance of DraftList from a JSON string
draft_list_instance = DraftList.from_json(json)
# print the JSON string representation of the object
print(DraftList.to_json())

# convert the object into a dict
draft_list_dict = draft_list_instance.to_dict()
# create an instance of DraftList from a dict
draft_list_from_dict = DraftList.from_dict(draft_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


