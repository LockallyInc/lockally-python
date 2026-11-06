# SendEmailBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[SendMessage]**](SendMessage.md) |  | 
**variables** | **Dict[str, str]** | Template variables every message in the batch inherits. Each message&#39;s own &#x60;variables&#x60; override these key by key, so shared values are written once and per-recipient ones stay per-recipient.  Without this, a 500-message batch repeats every shared variable 500 times: most of the payload, and 500 places for one of them to differ by a typo.  | [optional] 

## Example

```python
from lockally.models.send_email_batch_request import SendEmailBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmailBatchRequest from a JSON string
send_email_batch_request_instance = SendEmailBatchRequest.from_json(json)
# print the JSON string representation of the object
print(SendEmailBatchRequest.to_json())

# convert the object into a dict
send_email_batch_request_dict = send_email_batch_request_instance.to_dict()
# create an instance of SendEmailBatchRequest from a dict
send_email_batch_request_from_dict = SendEmailBatchRequest.from_dict(send_email_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


