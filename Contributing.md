## Contributing to DeliverEase

Welcome to DeliverEase! We are excited to have you contribute to our project. Your contributions can help us improve and enhance the platform, empowering delivery partners and connecting communities even more effectively.

## Guide to Setting up the Project Locally

1. Fork the repository into your GitHub account.

2. Clone your fork into your system

3. Create a virtual environment 

4. If you are using virtualenv, install all the dependencies on your system by: `pip install -r requirements.txt`.

5. Or if you are using poetry, install all the dependencies on your system by: `poetry install`

6. Make migrations into the codebase: `python manage.py makemigrations`

7. Migrate your changes: `python manage.py migrate`

8. Run the server locally: `python manage.py  runserver`

9. Now we need to enable the git hooks, so for that, you need to cd to the _hooks directory and run hooks_setup file.
 
    Step 1: `cd _hooks`
   
    Step 2: `./hooks_setup`

10. Now you can setup HTML & CSS Linter by following the steps given below:
    
  • Step 1: NodeJS latest version must be installed in your system. If not then install it from [here](https://nodejs.org/en/download/).

  • Step 2: ```npm install --save-dev htmlhint```to install HTML linter.

  • Step 3: ```npm install stylelint-config-standard --save-dev``` to install the CSS linter.


• To run all HTML files in the project directory, run ```npx htmlhint "**/*.html"```(to run only one file; cd into that folder -> replace "**/*.html"(npx htmlhint example.html) with the file name.)
    
• To run all CSS files in the project directory, run ```npx stylelint "**/*.css"```(to run only one file; cd into that folder -> replace "**/*.css"(npx stylelint example.css) with the file name.)

11. Now that the Project's setup is complete, Thank you for setting up the project locally. Now you can start contributing to the project.

## Guidelines for Contributors

To contribute to DeliverEase, please follow these guidelines:
 
1. Check if there is a stale issue by asking out the current assignee or the maintainer about the progress of the issue or if there is a unassigned issue.

2. In either case get the issue assigned to yourself by commenting on the issue like I would like to work on this issue please assign me and tag a maintainer, and start working on it after you are assigned the issue.

3. Check out a new branch whose name will be similar to the issue you worked on. For example, if you worked on the readme, you can name it as "docs/readme": `git checkout -b docs/readme`

4. Make your changes to the codebase or documentation in your branch. Be sure to follow the coding style and conventions used in the project.

5. Test your changes thoroughly to ensure they work as expected.

6. Update or create new tests where applicable, and also update the dependencies if you have used a new software.

7. Ensure that all existing tests pass successfully before submitting your changes.

8. Add your changes to git.

9. Commit your changes.

10. Write clear and concise commit messages for your changes and add GH-(issue number), for example, add GH-9, in the end of the commit message  if you are working on issue 9.

11. Add the remote upstream branch to git: `git remote add upstream https://github.com/TeamCodeArena/DeliverEase`

12. Fetch all the updates in the remote branch while you were working on the issue: `git fetch upstream`

13. Merge your local branch with the remote branch: `git merge upstream/main`.

14. Add a remote origin: `git remote add origin <link_to_your_forked_copy>` 

15. Push your changes to the new branch: `git push origin <name_of_ur_current_branch>`

16. Go to your forked repo on Github, and you will see an option to create a PR. Select the option and create a PR.

17. Provide a detailed description of your changes in the pull request, including the problem you are solving, the approach you took, and any relevant information for reviewers.

18. Attach an issue number in the description while creating the PR so that GitHub can automatically link it to the issue. For. ex: add #9 if you are making PR for issue number 9 and also make sure to tag **@SID262000**. So that he can be notified about your PR and review it accordingly.

19. Be responsive to feedback and comments on your pull request. If changes are requested, make the necessary adjustments.

20. Once your pull request is approved and meets the project's quality standards, it will be merged into the main repository.

## Code Style and Guidelines

To maintain a consistent codebase, we follow specific code styles and guidelines. Please adhere to the following conventions when contributing:


- Python code should conform to the latest PEP style guide 
- HTML and CSS should follow best practices and conventions for web development.
- Write clear and well-documented code.
- Use meaningful variable and function names.
- Include comments where necessary to explain complex logic or processes.

## Join our Mailing List
[**Click on this link to join our Slack community.**](https://join.slack.com/t/deliverease-group/shared_invite/zt-20af47vjo-msHq~8~PRsmi3x5~rMzs7g)

## Reporting Issues

If you come across any issues, or bugs, or have suggestions for improvements, please report them using GitHub Issues. When reporting issues, provide as much relevant information as possible, including steps to reproduce the problem, your operating system, browser details, etc.


## Code of Conduct

We expect all contributors to adhere to our Code of Conduct, which promotes a welcoming and inclusive community. Please be respectful and considerate of others' opinions and contributions.
Please check out [**`CODE_OF_CONDUCT`**](CODE_OF_CONDUCT.md).


## Thank You

Thank you for your interest in contributing to DeliverEase. Your contributions are valuable and help us create a better platform for everyone. Happy contributing!
