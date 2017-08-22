GovReady Sample Apps
====================

Sample compliance apps for GovReady Q.

Configuring in GovReady
-----------------------

To use these apps, add a ModuleSource entry to your GovReady Q admin page at `https://yourserver/admin/guidedmodules/modulesource/`. The namespace name can be any string. The spec field should contain:

	{
	  "type": "git",
	  "url": "https://github.com/GovReady/govready-sample-apps"
	}

Since this repository is public, no authentication information is necessary. If this repository is checked out locally, instead use:

	{
	  "type":" local",
	  "path": "path/to/this/directory"
	}

