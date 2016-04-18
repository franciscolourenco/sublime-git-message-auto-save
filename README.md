#Sublime Git Commit Message Auto Save
Sublime Text 3 plugin to save git commit messages automatically when the message window is closed.
This allows the user to close the window without having to save beforehand, or having to deal with the "Save File" popup.

##Usage
Use git to make a commit, write the commit message using Sublime Text, and close the window without saving.
If you wish to abort the commit, delete the message before closing the window.

If you don't have Sublime Text setup as your default git editor, follow these [instructions](https://help.github.com/articles/associating-text-editors-with-git/#using-sublime-text-as-your-editor).


##Install

Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `git commit`. Among the entries you should see `Git Commit Message Auto Save`. If that entry is not highlighted, use the keyboard or mouse to select it.

