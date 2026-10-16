# SendEmail200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Present on a test-mode send; absent when suppressed. | [optional] 
**message_id** | **str** | RFC 5322 Message-ID. On a test send the domain is test.lockally.com. Absent when suppressed. | [optional] 
**status** | **str** |  | 
**warning** | **str** | On a suppressed send, explains that nothing was sent. | [optional] 

## Example

```python
from lockally.models.send_email200_response import SendEmail200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmail200Response from a JSON string
send_email200_response_instance = SendEmail200Response.from_json(json)
# print the JSON string representation of the object
print(SendEmail200Response.to_json())

# convert the object into a dict
send_email200_response_dict = send_email200_response_instance.to_dict()
# create an instance of SendEmail200Response from a dict
send_email200_response_from_dict = SendEmail200Response.from_dict(send_email200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


