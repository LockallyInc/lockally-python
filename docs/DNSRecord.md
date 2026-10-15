# DNSRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**value** | **str** |  | 
**ttl** | **int** |  | 
**priority** | **int** | MX records only. | [optional] 
**purpose** | **str** |  | 

## Example

```python
from lockally.models.dns_record import DNSRecord

# TODO update the JSON string below
json = "{}"
# create an instance of DNSRecord from a JSON string
dns_record_instance = DNSRecord.from_json(json)
# print the JSON string representation of the object
print(DNSRecord.to_json())

# convert the object into a dict
dns_record_dict = dns_record_instance.to_dict()
# create an instance of DNSRecord from a dict
dns_record_from_dict = DNSRecord.from_dict(dns_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


