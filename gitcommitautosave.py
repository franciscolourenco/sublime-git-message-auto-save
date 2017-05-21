"""Git Commit Auto Save.

Sublime Text 3 package to auto save commit messages when the window is closed.
This allows the user to close the window without having to save before,
or having to deal with the "Save File" popup.
"""
import sublime_plugin


class GitCommitAutoSave(sublime_plugin.EventListener):
	def on_load(self, view):
		if is_git_file(view.file_name()):
			view.set_scratch(True)  # disable save file dialog on exit

	def on_pre_close(self, view):
		if is_git_file(view.file_name()):
			view.run_command("save")


def is_git_file(path):
	git_files = ('COMMIT_EDITMSG', 'git-rebase-todo', 'MERGE_MSG', 'PULLREQ_EDITMSG')
	if path and any(path.endswith(name) for name in git_files):
		return True
