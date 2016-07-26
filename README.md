# Q SSP Module

A [GovReady Q](https://github.com/GovReady/govready-q) content module of questions and templates to assemble a System Security Plan for a Federal government information system.


## Deployment

The govready-q-ssp-module is checked out onto the q server at `~site/govready-q-ssp-module`.

GovRead Q server finds these modules through a symbolic link `ssp` inside the `/site/q/modules` directory where Q looks for modules. 

Github would not allow the reuse of the deploy key, so a second deploy key is in `~/.ssh/id_rsa_qssprepo`.

But git needs to know to use that key, e.g.:

```
GIT_SSH_COMMAND="ssh -i ~/.ssh/id_rsa_qssprepo" git pull
```

The script `~site/govready-q-ssp-module/git` (yes, `git`) contains the minus the "pull" command, so you can log into q server and refresh the module content with the commands:

```
sudo -ui site
cd ~/govready-q-ssp-module
./git pull
```

After refreshing module content remember to `load_modules` to update the database.

```
python3 manage.py load_modules
```