```
git log
```
View the commit history of the repository.

```
git log --oneline
```
View a concise, one-line log of the commit history.

```
git log -p
```
Display the commit history with the patch (differences) for each commit.

```
git branch improve-drawing-project
```
Create a new branch named "improve-drawing-project."

```
git checkout improve-drawing-project
```
Switch to the "improve-drawing-project" branch.

```
git checkout -b improve-drawing-project
```
Create a new branch "improve-drawing-project" and switch to it in a single command.

```
git mv file.txt text-file.txt
```
Rename "file.txt" to "text-file.txt and git add it in a single command."

```
git rm text-file.txt
```
Remove the file "text-file.txt" from the repository and git add it in a single command.

```
git diff
```
View the changes made to the repository.

```
git diff --staged
```
View the differences for the changes staged for the next commit.

```
git restore --staged .
```
Unstage changes that were previously staged.

```
git revert 15d15df27ca693f63bd9b92ed92a283289953316
```
Create a new commit that undoes the changes introduced by the specified commit.

```
git checkout main
```
Switch back to the "main" branch.

```
git merge improve-drawing-project
```
Merge changes from the "improve-drawing-project" branch into the "main" branch.

```
git branch -d improve-drawing-project
```
Delete the "improve-drawing-project" branch.