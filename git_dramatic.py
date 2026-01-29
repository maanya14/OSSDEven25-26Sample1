# this is a fun program i wrote to learn about git commands for people who love to read classic literature, have fun!
import re
git_jokes = {
    "git commit": "‘I am made and remade continually.’ —Virginia Woolf, *The Waves*",
    "git push": "‘Into the abyss I throw myself… let me not fall too fast.’ —Dostoevsky, *Notes from Underground*",
    "git merge": "‘The meeting of two personalities is like the contact of two chemical substances: if there is any reaction, both are transformed.’ —Carl Jung",
    "git branch": "‘I have always imagined that Paradise will be a kind of library.’ —Borges, *The Library of Babel*",
    "git rebase": "‘Who controls the past controls the future. Who controls the present controls the past.’ —George Orwell, *1984*",
    "git checkout": "‘We are all time travelers moving at the speed of exactly 60 minutes per hour.’ —Douglas Adams, *The Hitchhiker’s Guide to the Galaxy*",
    "git log": "‘The past is never dead. It’s not even past.’ —William Faulkner, *Requiem for a Nun*",
    "git status": "‘To be, or not to be, that is the question.’ —Shakespeare, *Hamlet*",
    "git clone": "‘And God created man in His own image…’ —Genesis 1:27 (the first recorded `git clone`?)",
    "git diff": "‘Look on my Works, ye Mighty, and despair!’ —Percy Bysshe Shelley, *Ozymandias*",
    "git stash": "‘Do I dare disturb the universe?’ —T.S. Eliot, *The Love Song of J. Alfred Prufrock*",
    "git reset": "‘Burn it! Burn it all!’ —Ray Bradbury, *Fahrenheit 451*",
    "git fetch": "‘I have traveled through madness to find me.’ —Nietzsche",
    "git pull": "‘You can’t step into the same river twice.’ —Heraclitus",
    "git blame": "‘Hell is other people.’ —Jean-Paul Sartre, *No Exit*",
    "git cherry-pick": "‘You must have chaos within you to give birth to a dancing star.’ —Nietzsche, *Thus Spoke Zarathustra*",
    "git revert": "‘What’s done cannot be undone.’ —Shakespeare, *Macbeth* (unless you use `git revert`, then it actually can)",
    "git bisect": "‘All that we see or seem is but a dream within a dream.’ —Edgar Allan Poe",
    "git tag": "‘These fragments I have shored against my ruins.’ —T.S. Eliot, *The Waste Land*",
    "git gc": "‘I must create a system or be enslaved by another man’s.’ —William Blake, *Jerusalem*"
}
patterns = {
    re.compile(r"\bcommit\b"): git_jokes["git commit"],
    re.compile(r"\bpush\b"): git_jokes["git push"],
    re.compile(r"\bmerge\b"): git_jokes["git merge"],
    re.compile(r"\bcheckout\b"): git_jokes["git checkout"],
    re.compile(r"\breset\b"): git_jokes["git reset"],
    re.compile(r"\brebase\b"): git_jokes["git rebase"],
     re.compile(r"\bclone\b"): git_jokes["git clone"],  # Added pattern for "clone"
    re.compile(r"\bstatus\b"): git_jokes["git status"]
}
def git_funny_explanation(command):
    if command in git_jokes:
        return git_jokes[command]
    
    for pattern in patterns:
        if re.search(pattern, command):
            return patterns[pattern]
        
    return "‘I know not what the future holds, but I am certain it holds only uncertainty.’ —H.G. Wells, *The War of the Worlds.*"
            
def main():
    print("welcome to dramatic git\nsay byebye to exit\ngit gitting:")
    while True:
        command = input()
        if command.lower() == 'byebye':
            print("adios!")
            break
        else:
            print(git_funny_explanation(command))

if __name__ == "__main__":
    main()
