# GetEncryptionStatus200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligible** | **bool** |  | [optional] 
**active** | **bool** |  | [optional] 
**mailboxes** | [**List[GetEncryptionStatus200ResponseMailboxesInner]**](GetEncryptionStatus200ResponseMailboxesInner.md) |  | [optional] 

## Example

```python
from lockally.models.get_encryption_status200_response import GetEncryptionStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEncryptionStatus200Response from a JSON string
get_encryption_status200_response_instance = GetEncryptionStatus200Response.from_json(json)
# print the JSON string representation of the object
print(GetEncryptionStatus200Response.to_json())

# convert the object into a dict
get_encryption_status200_response_dict = get_encryption_status200_response_instance.to_dict()
# create an instance of GetEncryptionStatus200Response from a dict
get_encryption_status200_response_from_dict = GetEncryptionStatus200Response.from_dict(get_encryption_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


