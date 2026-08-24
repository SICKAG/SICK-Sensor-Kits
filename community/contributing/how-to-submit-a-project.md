# How to Submit a Community Project

This guide explains how to prepare and submit a community or university project for the SICK Sensor Starter Kits.

Before submitting a project, please read the Community Project Guidelines:

community_project_guidelines.md

## Contribution Process

The submission process consists of the following steps:

1. Copy the project template.
2. Move the copied folder into the correct Starter Kit directory.
3. Add the project information, source code and images.
4. Complete `project-info.yml`.
5. Complete the project `README.md`.
6. Test the project locally.
7. Create a separate Git branch.
8. Commit and push the project.
9. Create a Pull Request.
10. Add requested changes during the review.
11. The project is merged after approval.
12. The SICK team may add the project to the GitHub.io project overview.

## 1. Copy the Project Template

Copy the complete folder:

```text
contributing/project_template/
```

Move the copied folder into the correct community directory.

Examples:

```text
community/vision/community-color-sorter/
community/lidar/air-piano/
community/iolink/status-light-dashboard/
```

Rename the copied folder to match the project.

Use lowercase letters and hyphens:

```text
community-color-sorter
distance-estimation-game
status-light-dashboard
```

Avoid spaces, underscores and special characters.

## 2. Complete the Project Structure

The copied project folder contains:

```text
your-project/
├── README.md
├── project-info.yml
├── requirements.txt
├── src/
└── images/
```

Add the project files to the appropriate locations:

- Place source code in `src/`.
- Place screenshots and the preview image in `images/`.
- List required Python packages in `requirements.txt`.
- Add the project information to `project-info.yml`.
- Replace the placeholder content in `README.md`.

Remove `requirements.txt` if the project does not require external Python packages.

## 3. Complete `project-info.yml`

The `project-info.yml` file contains the standardized project metadata.

Complete all applicable fields, including:

- project name
- Starter Kit
- project type
- difficulty
- estimated duration
- requirements
- short description
- preview image
- programming language
- repository path
- affiliation, where applicable

Example:

```yaml
project_name: "Community Color Sorter"
starter_kit: "Vision"
project_type: "Community Project"
difficulty: "Beginner"
estimated_duration: "45 minutes"

short_description: >
  Classify colored objects with the Vision Starter Kit and process
  the result in a Python application.

requirements: >
  Vision Starter Kit, colored test objects and Python.

preview_image: "images/preview.png"

language:
  - "Python"

author_type: "University"
affiliation: "Example University"

repository_path: "community/vision/community-color-sorter"
github_io_page: ""

status: "Submitted"
```

The SICK team may use this information to create a project card on GitHub.io after the project has been reviewed and merged.

A project submission does not automatically create a GitHub.io page.

## 4. Complete the Project README

Use the README included in the project template.

The README should explain:

- what the project does
- which Starter Kit is required
- which additional hardware is required
- which software and libraries are required
- how to install the project
- how to configure the sensor
- how to run the project
- what result is expected
- which limitations are known
- which environment was tested

Community project READMEs should contain enough information for another user to reproduce the project without requiring a separate GitHub.io page.

Remove all unused sections and placeholder text before submitting.

## 5. Add Source Code and Images

Place editable source code in:

```text
src/
```

Example:

```text
src/main.py
```

Place screenshots and the preview image in:

```text
images/
```

A preview image is strongly recommended.

Recommended path:

```text
images/preview.png
```

Do not provide the source code exclusively inside a ZIP file. Users should be able to inspect and modify the source files directly.

## 6. Document Dependencies

If the project requires Python packages, add them to:

```text
requirements.txt
```

Example:

```text
pygame-ce
flask
```

The README should include the installation command:

```bash
python -m pip install -r requirements.txt
```

Only include packages that are actually required by the project.

## 7. Test the Project

Before submitting, follow the instructions in the README from beginning to end.

Verify that:

- dependencies can be installed
- source code starts without syntax errors
- file paths are correct
- configuration values are explained
- required files are included
- the expected result can be reproduced
- screenshots match the current project version
- no sensitive information is included

Document the tested environment in the README.

Example:

```text
Tested with:

- Windows 11
- Python 3.12
- picoScan150
- pygame-ce 2.5
```

## 8. Create a Branch

Update the local `main` branch:

```bash
git checkout main
git pull origin main
```

Create a separate branch for the contribution:

```bash
git checkout -b community/vision-color-sorter
```

Recommended branch format:

```text
community/<starter-kit>-<project-name>
```

Examples:

```text
community/vision-color-sorter
community/lidar-air-piano
community/iolink-status-dashboard
```

Do not add the project directly to `main`.

## 9. Stage and Commit the Project

Check the changed files:

```bash
git status
```

Add only the new project folder:

```bash
git add community/vision/community-color-sorter
```

Check the staged files again:

```bash
git status
```

Create a clear commit:

```bash
git commit -m "Add Vision community color sorter project"
```

Avoid unclear commit messages such as:

```text
Update
Changes
Final version
Test
```

## 10. Push the Branch

For the first push of the branch:

```bash
git push -u origin community/vision-color-sorter
```

After the upstream connection has been created, later updates normally require only:

```bash
git push
```

Pushing the branch does not change `main`.

The project is added to `main` only after the Pull Request has been approved and merged.

## 11. Create the Pull Request

After pushing the branch:

1. Open the repository on GitHub.
2. Open the Pull Requests tab.
3. Select **New Pull Request**.
4. Select `main` as the base branch.
5. Select the contribution branch as the compare branch.
6. Review the changed files.
7. Select **Create Pull Request**.
8. Complete the Pull Request template.
9. Submit the Pull Request.

Use a clear title:

```text
Add Vision community color sorter project
```

You do not need to select an Assignee, Project or Milestone. The SICK team assigns the appropriate reviewers.

## 12. Review and Requested Changes

The SICK team reviews the project before it is merged.

Reviewers may request changes to:

- project structure
- metadata
- README instructions
- source code
- dependencies
- images
- security
- licensing
- reproducibility

Make requested changes in the same local branch.

Then commit and push them:

```bash
git add community/vision/community-color-sorter
git commit -m "Address project review feedback"
git push
```

The existing Pull Request updates automatically.

Do not create a new Pull Request for every correction.

## 13. Approval and Merge

The project can be merged when:

- required files are present
- automated checks pass
- review comments are resolved
- required approvals are available
- no merge conflicts remain
- the project follows the Community Project Guidelines

The SICK team performs or approves the final merge.

## 14. After the Merge

After the project has been merged:

- the project is available in the community area of the repository
- users can access the code and downloadable files
- the contribution branch can be deleted
- future changes are submitted through a new branch and Pull Request
- the SICK team may add the project manually to GitHub.io

The GitHub.io project card can contain:

- project name
- project type
- difficulty
- estimated duration
- requirements
- short description
- preview image
- link to the project folder

The final wording and presentation are maintained by the SICK team.

## Submission Checklist

Before creating the Pull Request:

- [ ] The correct project template was copied.
- [ ] The project is stored in the correct Starter Kit folder.
- [ ] The folder name follows the naming convention.
- [ ] `README.md` contains no placeholder text.
- [ ] `project-info.yml` is complete.
- [ ] Source code is stored in `src/`.
- [ ] Dependencies are documented.
- [ ] A preview image is included if possible.
- [ ] The project was tested.
- [ ] The tested environment is documented.
- [ ] No credentials or confidential information are included.
- [ ] Third-party content is documented.
- [ ] The Pull Request template is complete.

## Need Help?

Use GitHub Discussions for:

- questions about the submission process
- early feedback on a project idea
- help with the project template
- general Starter Kit questions

Use GitHub Issues for:

- reproducible repository problems
- errors in the project template
- errors in the contribution documentation