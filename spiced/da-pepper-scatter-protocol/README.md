# Daily Protocol How-To
Template for creating awesome markdown protocols

### Goal: Self Created Documentation
Class is required to write a protocol for each day. 
Students take turns being the note taker. You can find the order in the list [**HERE**](https://docs.google.com/spreadsheets/d/1RCQQTKYziD5R5nWcl7KuHGSBxcdkPu205-vPNtKOF1w/edit?gid=0#gid=0)

Using templates, `advanced_version.md` `beginner_version.md`, or any protocol from  previous days you create a summary of the current day.

The protocol is written in markdown. Basic formatting as in templates is sufficient, but feel free to be creative and add more features.
[Markdown CheatSheet example](https://github.com/lifeparticle/Markdown-Cheatsheet).

Keep the repository organized and clean. Agree on the ongoing file-naming in the same format and follow it. If there is any 1-digit numberings add a zero at the front (like '04', instead of '4').



### Git and GitHub Steps
1. **a:** $\color{Bittersweet}{If \ the \ first \ time \ protocol \ writer:}$ clone this repository to your local (to your laptop)  
   **b:** $\color{Bittersweet}{If \ you \ cloned \ it \ before:}$ 

   ​	**In Git Bash**:

   - navigate to your local repository of the protocol 
   - run `git pull` -> you should see updates or "Already up to date" message.




2. Create and switch to a new branch for the protocol repo.
		**In Git Bash**:
	
	- `git switch -c newBranchName` (**Modify the name the branch name! This is just a dummy.**)
	> A branch in Git is a separate line of development that allows you to create files or make changes to existing files independently from the main codebase.




3. Open the protocol repository in VS Code

   

4. **In VS Code:** Create a new markdown document for the current day 

   - Create a copy of a template or of one the previous day's reports
   - Rename it according to previous file-naming format



5. Fill the current day's report: 

    - Add intro
    - Fill out the Schedule Table
    - Add Summaries about the topics covered during the day
    - Add other noticable events. Leave space for questions
    - Feel free to be creative. [Markdown CheatSheet example](https://github.com/lifeparticle/Markdown-Cheatsheet).

     

6. Save the new file

     

7. To commit changes to your branch **locally**:

    ​	**In Git bash**: 

    - navigate to your local repository of the protocol
    - `git add .` 
    - `git commit -m "created a new daily report for 04.10.2024"` (modify the comment at your will)



8. To push your branch **for the first time** to GitHub (basically synchronizing GitHub repo with your local repo)
    
    (NOTE: if you just want to update a GitHub branch see Step 10)
    
    ​	**In Git Bash**: 
    
    - `git push -u origin new-branch`

  

9. **In a browser**:
   - Check the protocol Repo on GitHub
   - Find the dropdown button below the Repo Name
   - And switch to your branch. (Hint: if you don't see it, at the bottom of the dropdown click "View all branches")



10. If you need to make changes to your branch **after the branch was pushed to the GitHub**
    - make sure you are in your branch 
    	- Either `git status` or see in VS Code left bottom in the file-manager bar. 
    	- If not `git checkout <your_branch_name>` **(modify the branch-name!)**
    - make changes locally on you laptop
    - **In Git Bash**: 
      - `git add .` 
      - `git commit -m "short description of changes"` **(modify the comment!)**
      - `git push origin <your_branch_name>` **(modify the branch-name!)**



11. **On the next day**: between 09:00 and 09:30 

    - present to your colleagues the branch in GitHub on the big screen

    - ask if there are any questions to add to the Protocol

    - Add questions if there are any
    	- You can do changes locally (follow instructions in Step 10) 
    	- or directly in GitHub. In that case don't forget to update your local repository **in Git Bash**: `git pull` 

    

12. Create a **Pull Request**. When everything is set:

    - in the protocol repository you'll see the yellow notification with a button **Compare and pull request**. Click it

    - in the grey bar below intro text **DOUBLE-CHECK** that `base:main` and your branch is selected `compare:<your_branch_name>`

    - add a title, for example "protocol for 04.10.2024"

    - add description explaining the details about the change if necessary, for example "Besides the protocoll file I added a folder images where the images used in the markdown file are saved" 

    - click **Create pull request** button

      

13. Merging:

    - Github will check if there are any conflicts and mark them if any

    - If the merge can be done without any issues, you will see the green button. **DON't CLICK IT** just yet

    - Let others to review it. You can define reviewers on the right side by clicking the gear-wheel icon -> add GitHub handles of the reviewers

    - You can even assign the Pull Request to other students. Gear-wheel icon -> add GitHub handles of the reviewers

    - At least one reviewer or more should look at the Tabs in the Pull Request `Commits` and `Files changed`. Than back in the Tab `Conversation` the reviewer can add a comment, for example "All good! Well done!"

    - **NOW** there is a confirmation comment and you can click the **Merge pull request** button

    - confirm the merge by clicking **Confirm merge** button

      

14. Delete branch:

    - The field now changed color and has the message "Pull request successfully merged and closed" 

    - on the right side in that field you see the **Delete branch** button. Click it

      

**DONE**! 

Your branch was merged into the `main` branch and deleted
