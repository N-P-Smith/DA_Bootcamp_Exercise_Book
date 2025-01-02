## GIT

-------------------------------------


## What is GitHub?

- Collaborate effectively online based on git (see below)
- Open-source community and contribution
- Follow others, find and star interesting repositories
- Show others what you did, invite to collaborate and collaborate yourself
- Demonstrate that you are actively working on projects
- Learn from code


 If you want to learn more about git & GitHub, you can watch this video.

https://www.youtube.com/watch?v=EVe3UBGEc_s



# Exercise 1

## Using Git with Remote Repository

- Create and clone new repo on your local machine
- Create new branch
- Commit and push changes to new branch
- Open a pull request (pr)
- Review code and approve pull request
- Merge branch into main / Deal with merge conflicts (if one occurs)
- Synchronize branches (check if everything is up to date)
- Open a pull request, approve and merge


# Exercise 2

## Let’s work in pairs.

##### New Repo
- ***ONE:*** creates new public repo on github with README.md, .gitignore, and Licence (MIT)
- Invites partner as collaborator
- ***BOTH:*** Clone it to your machine
#### New Branches
- ***BOTH:*** create and switch to a new branch locally: git switch -c <new_branch>
- ***BOTH:*** Make some changes! Create a new file and add, commit your change
- ***BOTH:*** Push a local branch to a new remote branch. Use: git push --set-upstream origin <branch_name>
#### Open Pull Request
- ***ONE:*** opens pull request and adds partner as reviewer
#### Code Review
- ***TWO:*** reviews changes and approves pull request




#### Merge Branch
***ONE:*** merges approved pull request into main branch and deletes remote branch
#### Syncing Branches Locally
- Now branch of TWO will be behind main branch
- Switch to main branch: git switch main
- pull changes: git pull
- switch to your branch: git switch <branch_name>
- merge new changes from main branch in your branch: git merge main
- add commit message (vim will open automatically) if necessary and push again


```python
# Merging should be done with the person who did pull request
```
```python
- Notes: git push -u origin <branch_name>
```
# Exercise 3

#### Second pull request
- TWO: opens pull request for his branch
- ONE: reviews changes and approves pull request
- TWO: merges approved pull request into main branch and deletes remote branch
- Last but not least..

- BOTH: switch to main branch locally and pull changes


```python
## Reflection Questions


```


## Resources

- Git Basics - https://www.youtube.com/watch?v=_OZVJpLHUaI

- Reference Manual - https://www.git-scm.com/docs

- Pro Git Book - https://www.git-scm.com/book/en/v2


