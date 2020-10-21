# GIT Procedures

The following page is a cheat sheet taken from [Atlasian](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet). It is a list of commands that can be run from the command line enabling a sound workflow.

![](/Users/james/Desktop/DSP_AT2/ASX/images/GIT_page1.png)

![Atlasian Cheatsheet](/Users/james/Desktop/DSP_AT2/ASX/images/GIT_page2.png)

In addition, this [link](http://marklodato.github.io/visual-git-guide/index-en.html) is an excellent reference for what is happening when the commands are executed. These two documents form the basis of the workflow that will be employed.

## GIT Policies Implemented for the group

Some rules for the following items:

### Master
  - the master branch is managed by one person.
  - Folders are created on the master and they are directly relatable to the project and an aspect of the complete pipeline - example folder are below:
    - Data collection and Database management
    - Data Analysis and insight gathering
    - Publication of the results to production

### Branch Policy
    - Branches are to be made close to the 'Trunk' where fixes and features are built then integrated quickly back to the master.
    - Branches are to be names in accordance with the following conventions:
      - /name/description
    - Once a feature or change had been integrated back into the master the branch is to be pruned.
    - Ideally, a branch is *grown* for a single feature or change - the change is integrated back into the master and the branch is pruned. This will allow the master to be the single source of truth that can go into production at any time.

### Commit Messages
    - All commit messages are to have the following format
        -m 'THIS THING WAS CHANGED OR FIXED

            This is a more detailed description of what has been changed or fixed and why'

### Pull Requests
    - All pull requests are to be in accordance with the template in the repository. The template has the following format
      - Issue - what was wrong/ what needed changing
      - Solution - what was done to fix the solution
      - An image of before and after if applicable
      - The way this can be tested before putting it back into production on the **Master** branch.
