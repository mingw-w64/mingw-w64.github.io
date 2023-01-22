# git-revert

Reverting gets more complicated depending on how far it has been
committed.

## Reverting before commit

Revert everything in the tree to last commit  
`git checkout -f HEAD`  
Revert a particular file to last commit  
`git checkout -f HEAD -- path/to/file`

## Reverting commits before it is pushed

Revert previous n-number of commits, roll back working tree  
`git reset --hard HEAD~3 #In this case, roll back by 3`  
Revert previous n-number of commits, **without** rolling back working
tree  
`git reset --mixed HEAD~3`
