## Git

**global conf stored in ~/.gitconfig**  

    git config --help

**Create from existing data**  

    cd my_project_dir
    git init
    git add .
    
**Create from existing repository**  
    
    git clone

**Show**  
    
    git status
    git diff
    
**Update**  
Fetch latests changes from origin, does not merge
    
    git fetch
    
Pull latest changes from origin and merge
    
    git pull

**Publish**

    git commit -am "message"
    git push