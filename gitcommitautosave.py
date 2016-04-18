"""Git Commit Auto Save.

Sublime Text 3 package to auto save commit messages when the window is closed.
This allows the user to close the window without having to save before,
or having to deal with the "Save File" popup.
"""
import sublime_plugin


class GitCommitAutoSave(sublime_plugin.EventListener):
	def on_load(self, view):
		if view.file_name().endswith('COMMIT_EDITMSG'):
			view.set_scratch(True)  # disable save file dialog on exit

	def on_pre_close(self, view):
		if view.file_name().endswith('COMMIT_EDITMSG'):
			view.run_command("save")
