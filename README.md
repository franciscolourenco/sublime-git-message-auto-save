# Sublime Git Message Auto Save

<p>
  <img src="https://img.shields.io/github/release/aristidesfl/sublime-git-message-auto-save.svg" alt="Release version">
  <img src="https://img.shields.io/badge/stability-stable-green.svg" alt="Stability: Stable">
  <img src="https://img.shields.io/packagecontrol/dm/Git%20Message%20Auto%20Save.svg" alt="Package Control">
  <img src="https://img.shields.io/badge/license-MIT-lightgray.svg" alt="License: MIT">
</p>

Sublime Text 3 package to auto-save git messages for commit, rebase, merge, etc.. when the sublime window is closed.
It allows you to close the git message window without having to deal with the "Save File" pop-up, or pressing `⌘S` or `^S` before closing the window.

The package is extremely small, and in only active on commit messages.


## Usage
Use `git` to make a commit, write the commit message using Sublime Text, and close the window without saving.
If you wish to abort the commit, delete the message before closing the window.

If you don't have Sublime Text configured as your default git editor, follow these [instructions](https://help.github.com/articles/associating-text-editors-with-git/#using-sublime-text-as-your-editor).


## GitSavvy
If you also use GitSavvy and want to make the committing work flow homogeneous, enable the option `"commit_on_close": true` in GitSavvy.
This allows you to use GitSavvy and `git` to commit from the command line, interchangeably without any difference.


## Install

Please use [Package Control](https://sublime.wbond.net/installation) to install. This will ensure that the package will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the package list appears, type `git commit`. Among the entries you should see `Git Commit Message Auto Save`. If that entry is not highlighted, use the keyboard or mouse to select it.

