# Q SSP Module

A [GovReady Q](https://github.com/GovReady/govready-q) content module of questions and templates to assemble a System Security Plan for a Federal government information system.

## Writer's Guide

Questions fall into three categories:

* Epistemic questions: Q asks about what is true or false in the user's environment. How large is their organization? Is their system hosted by a cloud provider? These questions should occur early and in setup phases of their work. These are probably easy for the user to answer.

  Example:

  * Since you are hosting in your agency's an internal data center, your communications boundary protection is provided your enterprise IT organization. Do you plan for your system to use these enterprise services?

* Intertitials.

  Example:

  * You know, hey, it's organization policy to have boundary protections. You said you are not using your enterprise services. Let's talk about why not.

* Deontic questions: These questions have a premise about what the user has a obligation to be doing. The prompts have two sentences: first is the premise, second is a question. e.g. You want to protect communication at the boundary, and we know you are using AWS, therefore you should be using AWS security groups.... Are you using AWS security groups?

  Example:

  * Since you are hosting in your agency's an internal data center, your communications boundary protection is normally provided your enterprise IT organization. You said you are not using those services but your organiation policy says that you should have boundary protections. . . . Do you have boundary protections / an alternative solution / would you like to request a waiver?

Thought on "training": Training is something a dog does. It's about rote/muscle memory. When we talk about training and rote activity, we should guard against insulting users who have been _hired to think creatively_ by always talking at the same time about how the training is _for_ and _in the service of_ a higher-level actitivty that does involve creative thinking.

### Managing image assets

Place all image and other file assets associated with module in the `modules/assets` directory

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
