# ExportMailbox201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Relative download URL. Caller appends to the API host. | 
**expires_at** | **datetime** |  | 
**format** | **str** |  | 

## Example

```python
from lockally.models.export_mailbox201_response import ExportMailbox201Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExportMailbox201Response from a JSON string
export_mailbox201_response_instance = ExportMailbox201Response.from_json(json)
# print the JSON string representation of the object
print(ExportMailbox201Response.to_json())

# convert the object into a dict
export_mailbox201_response_dict = export_mailbox201_response_instance.to_dict()
# create an instance of ExportMailbox201Response from a dict
export_mailbox201_response_from_dict = ExportMailbox201Response.from_dict(export_mailbox201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


