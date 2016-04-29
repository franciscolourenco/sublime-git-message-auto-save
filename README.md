#Sublime Git Message Auto Save
Sublime Text 3 plugin to autosave git messages for commit/rebase/rtc when the sublime window is closed.
It allows you to close the git message window without having to save beforehand, or having to deal with the "Save File" popup.

##Usage
Use git to make a commit, write the commit message using Sublime Text, and close the window without saving.
If you wish to abort the commit, delete the message before closing the window.

If you don't have Sublime Text configured as your default git editor, follow these [instructions](https://help.github.com/articles/associating-text-editors-with-git/#using-sublime-text-as-your-editor).


##Rationale
I use [GitSavvy](https://github.com/divmain/GitSavvy) to do most of my git stuff in Sublime Text. However I still use git from the command line to do other things quite often.
Since I still have to `save` when using git from the command line, I keep inserting accidental signatures when using GitSavvy, since the shortcuts are the same and muscle memory.
This is an attempt to prevent that from happening, by bringing the editing experience of normal git cli and GitSavvy closer together.

The plugin is extremely small, and in only active on commit messages. To make GitSavvy commit on close like git cli, set `"commit_on_close": true` in your GitSavvy preferences.


##Install

Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `git commit`. Among the entries you should see `Git Commit Message Auto Save`. If that entry is not highlighted, use the keyboard or mouse to select it.

