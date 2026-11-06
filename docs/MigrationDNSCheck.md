# MigrationDNSCheck

Live DNS readiness of the destination domains, for deciding when to cut over. `ready` is true only when every domain's MX points at Lockally and its SPF authorises it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ready** | **bool** |  | 
**domains** | [**List[MigrationDomainDNS]**](MigrationDomainDNS.md) |  | 

## Example

```python
from lockally.models.migration_dns_check import MigrationDNSCheck

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationDNSCheck from a JSON string
migration_dns_check_instance = MigrationDNSCheck.from_json(json)
# print the JSON string representation of the object
print(MigrationDNSCheck.to_json())

# convert the object into a dict
migration_dns_check_dict = migration_dns_check_instance.to_dict()
# create an instance of MigrationDNSCheck from a dict
migration_dns_check_from_dict = MigrationDNSCheck.from_dict(migration_dns_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


