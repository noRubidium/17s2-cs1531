### Frequently encountered issues with git
1. doing `git add .` and `git commit ...` before creating any file in the project directory will result in no branches created and unable to push. Fix: Create a new file then run both commands
2. Not adding remote / adding non existing address as remote will result in push failure. Fix: `git remote set-url origin ${PROPER_URL}`
3. Sometimes git will refuse to merge unrelated histories. Fix: turn on the flag `--allow-unrelated-histories` in the command (merge / pull).
4. Make sure SSH key has been created and added for EVERY MACHINE THEY ARE WORKING ON
5. Make sure run `git pull` or (`git fetch` and `git merge`) if the local branch is behind the remote branch
6. If you see unable to switch branch because of untracked file, it means that student might have done the following sequence of operations:
    - branch out from `A` to `B`
    - add file `m` in branch `B`
    - git `add` and `commit`
    - switch back to branch `A`
    - create file `m`
    - switch branch to branch `B`
- Git is trying to prevent the file `m` from being overwritten by the file `m` in branch `B`.
- The fix to the problem is to either remove `m` or add `m` to branch `A`, then you can switch branch
7. Unable to create merge conflicts are generally caused by:
    - branch out after modifying the branch (probably will tell you everything up-to-date)
    - the modification is the same or at completely different places which can be auto-merged
    - and so on (please update if something else is discovered)
8. Current version of chrome on CSE isn't supported by github any more. Fix: Use Firefox :(
9. This by no means is an exhaustive list of issues that can happen with git, but most of the git error messages are pretty straight forward and guides you what to do to solve the error.
