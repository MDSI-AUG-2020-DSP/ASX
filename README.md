1. Python is the programming language chosen.
2. Create data into a folder called data for now.
3. Do not push your local branch to Master branch.

create a new repository on the command line
echo "# test" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/MDSI-AUG-2020-DSP/ASX.git
git push -u origin master
              
push an existing repository from the command line
git remote add origin https://github.com/MDSI-AUG-2020-DSP/ASX.git
git branch -M master
git push -u origin master

