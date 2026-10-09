# CreateEncryptionRecoveryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mailbox_email** | **str** |  | 
**recovery_blob** | **str** |  | 

## Example

```python
from lockally.models.create_encryption_recovery_request import CreateEncryptionRecoveryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEncryptionRecoveryRequest from a JSON string
create_encryption_recovery_request_instance = CreateEncryptionRecoveryRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEncryptionRecoveryRequest.to_json())

# convert the object into a dict
create_encryption_recovery_request_dict = create_encryption_recovery_request_instance.to_dict()
# create an instance of CreateEncryptionRecoveryRequest from a dict
create_encryption_recovery_request_from_dict = CreateEncryptionRecoveryRequest.from_dict(create_encryption_recovery_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


