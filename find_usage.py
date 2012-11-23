import sublime
import sublime_plugin


class FindUsageCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        search_start_regex = r'[:\.\s]'
        search_end_regex = r'[,!?}:\.\s\(\)\]]'

        for region in self.view.sel():
            search_term = None

            if region.empty():
                closest_word = self.view.word(region)
                search_term = self.view.substr(closest_word)
            else:
                search_term = self.view.substr(region)

            sublime.set_clipboard(search_start_regex + search_term + search_end_regex)
            self.view.window().run_command("show_panel", {"panel": 'find_in_files'})
            sublime.active_window().run_command('paste')
