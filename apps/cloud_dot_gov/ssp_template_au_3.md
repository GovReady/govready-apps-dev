id: ssp_template_au_3
format: markdown
...
## Cloud Checkr

CloudTrail Log File Name Format CloudTrail uses the following file name format for the log file objects it uploads to your S3 bucket: AccountID_CloudTrail_RegionName_YYYYMMDDTHHmmZ_UniqueString.FileNameFormat YYYY, MM, DD, HH, and mm are the digits of the year, month, day, hour, and minute (respectively) when the log file was delivered. Hours are in 24-hour format. The Z indicates that the time is in UTC.
## Cloud Controller
## ELKStack

The cloud.gov platform as a service generates audit logs from its Loggregator component and is passed through the ELK stack to produce audit records which contain sufficient information to establish at a minimum: what type of event occurred, when (date and time the event occurrence) the source of the event the outcome (success or failure) of the event the identity of any user/subject associated with the event
