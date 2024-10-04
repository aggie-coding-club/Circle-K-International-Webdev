# Circle-K-International-Webdev

This is a web development project meant to create a website for one of the volunteering orgs at A&M.

---
## Installation
'''cmd
pip install -r requirements.txt
'''
=======
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/aggie-coding-club/Circle-K-International-Webdev.git
    cd Circle-K-International-WebDev
    ```
2. **Create a venv for the project:**
    ```console
    python -m venv .venv
    ```
3. **Install requirements into your venv:**
   ```console
   pip install -r requirements.txt
   ```
# Code Commit Process
This section will detail the process you can use to commit code (Add code to the GitHub). Follow this process every time you want to contribute to the project.

Make sure you have a GitHub classic personal access token and check all permissions. 
Information can be found here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

Start by getting the latest version of the application. Making sure you're in the directory of your project, run this command:

    git merge origin/main

Then, you want to create a new branch. You are going to work off this branch exclusively for your code. For ease of naming, please name the branch ***Your first name and last initial***. So, my name being Declan Staunton, I would run:

    git checkout -b declanS

Once you're done, edit your code as you please.

Once you're ready to add your code to the GitHub, add the files you want to change/add to the GitHub using:

    git add <filename>

Then, commit (initiate) your file by using:

    git commit -m "(Type any message)"

When you finish, push your code to the main repository using this command:

    git push origin declanS

It will ask for a username and password. Enter your GitHub username and your personal access token as the password.

Once you've done that, visit GitHub and create a pull request. You can learn more about pull requests here: [https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

Once you're done, you can switch back to the main branch and delete the feature branch you were using. You can do it using the following 2 commands:

    git checkout main
    git branch -D declanS
>>>>>>> 3479f946fd7c923718f52ef55e3e9cf89a3b4f2f
