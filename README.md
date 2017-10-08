# govready-apps-800-171-collection

These are under development apps that have had initial modifications to represent 800-171 compliance.

# App Source Configuration

Navigate to your GovReady-Q Django database admin module and create an `App sources` record in your GovReady-Q database with the below information.

### GitHub Repository App Source

`Name`: `800-171-collection`

`Spec`:
```
{
  "type":"git",
  "url":"https://github.com/GovReady/govready-apps-800-171-collection",
  "ssh_key":"Add private key here as a single block (e.g., new lines replaced with '\n')",
}
```

### Local File App Source

`Name`: `800-171-collection`

`Spec`:
```
{
  "type":"local",
  "path":"/path/to/govready-apps-800-171-collection/apps"
}
```

### Local File App Source (for Docker)

NOTE: Assumes local directory path has been defined when launching GovReady-Q Docker image.

`Name`: `800-171-collection`

`Spec`:
```
{
  "type":"local",
  "path":"/mnt/apps/govready-apps-800-171-collection/apps"
}
```