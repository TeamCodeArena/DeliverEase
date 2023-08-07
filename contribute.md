## Contributing to DeliverEase

Welcome to DeliverEase! We are excited to have you contribute to our project. Your contributions can help us improve and enhance the platform, empowering delivery partners and connecting communities even more effectively.

## How to Contribute

To contribute to DeliverEase, please follow these guidelines:

1. Fork the repository to your GitHub account.

2. Clone your fork into your system

3. Create a virtual environment 

4. IF you are using virtualenv, install all the dependencies to your system by: `pip install -r requirements.txt`.

5. OR if you are using poetry, install all the dependencies to your system by: `poetry install`

6. Make migrations into the Database : `python manage.py migrate`

7. Run the server locally: `python manage.py  runserver`

8. Check if there is a stale issue by asking out the current assignee or the maintainer about the progress of the issue or if  there is a unassigned issue.

9. In either case get the issue assigned to yourself by commenting on the issue like I would like to work on this issue please assign me and tag a maintainer, and start working on it after you are assigned the issue.

10. checkout to a new branch whose name will be similar to the issue you worked on . For ex. you worked on the readme you can name it as "docs/readme".

11. Make your changes to the codebase or documentation in your branch. Be sure to follow the coding style and conventions used in the project.

12. Test your changes thoroughly to ensure they work as expected.

13. Update or create new tests where applicable and also update the dependencies if you have used a new software.

14. Ensure that all existing tests pass successfully before submitting your changes.

15. Add your changes to git.

16. Commit your changes. 

17. Write clear and concise commit messages for your changes and add GH-(issue number) for ex.add  GH-9 in the end of commit message  if you are working on issue 9.

18. Add the remote upstream branch to git :  `git remote add upstream https://github.com/TeamCodeArena/DeliverEase`

19. Fetch all the updates in the remote branch while you were working on the issue: `git fetch upstream`

20. Merge your local  branch with the remote branch: `git merge upstream/main`.

21. Add a remote origin : `git remote add origin <link_to_your_forked_copy>` 

22. Push your changes to the new branch : `git push origin <name_of_ur_current_branch>`

23. Go to your forked repo on Github and you will see a option to create a PR. select the option and create a PR.

24. Provide a detailed description of your changes in the pull request, including the problem you are solving, the approach you took, and any relevant information for reviewers.

25. Attach an issue number in the description while creating the PR so that GitHub can automatically link it to the issue. For. ex: add #9 if you are making PR for issue number 9 and also make sure to tag @SID262000. So that he can be notified about your PR and review it accordingly.

26. Be responsive to feedback and comments on your pull request. If changes are requested, make the necessary adjustments.

27. Once your pull request is approved and meets the project's quality standards, it will be merged into the main repository.

## Code Style and Guidelines

To maintain a consistent codebase, we follow specific code style and guidelines. Please adhere to the following conventions when contributing:


- Python code should be according to the latest PEP style guide 
- HTML and CSS should follow best practices and conventions for web development.
- Write clear and well-documented code.
- Use meaningful variable and function names.
- Include comments where necessary to explain complex logic or processes.

## Join our Mailing List
Slack Group: https://join.slack.com/t/deliverease-group/shared_invite/zt-20af47vjo-msHq~8~PRsmi3x5~rMzs7g

## Reporting Issues

If you come across any issues, bugs, or have suggestions for improvements, please report them using GitHub Issues. When reporting issues, provide as much relevant information as possible, including steps to reproduce the problem, your operating system, browser details, etc.


## Code of Conduct

We expect all contributors to adhere to our Code of Conduct, which promotes a welcoming and inclusive community. Please be respectful and considerate of others' opinions and contributions.
Please Checkout [`**CODE_OF_CONDUCT**`](CODE_OF_CONDUCT.md)


## Thank You

Thank you for your intrest in contributing to DeliverEase. Your contributions are valuable and help us create a better platform for everyone. Happy contributing!
