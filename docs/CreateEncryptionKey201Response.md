# CreateEncryptionKey201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**mailbox_id** | **UUID** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from lockally.models.create_encryption_key201_response import CreateEncryptionKey201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEncryptionKey201Response from a JSON string
create_encryption_key201_response_instance = CreateEncryptionKey201Response.from_json(json)
# print the JSON string representation of the object
print(CreateEncryptionKey201Response.to_json())

# convert the object into a dict
create_encryption_key201_response_dict = create_encryption_key201_response_instance.to_dict()
# create an instance of CreateEncryptionKey201Response from a dict
create_encryption_key201_response_from_dict = CreateEncryptionKey201Response.from_dict(create_encryption_key201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


