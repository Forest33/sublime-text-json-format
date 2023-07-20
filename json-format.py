import sublime
import sublime_plugin
import json


class JsonFormatCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selection = self.view.sel()
		for region in selection:
			region_text = self.view.substr(region)
			if len(region_text) == 0:
				return

			region_text = region_text.replace("\\\"", "\"").replace("\\n", "")
		
			try:
				json_object = json.loads(region_text)
			except json.decoder.JSONDecodeError as e:
				print(e)
				return

			json_formatted = json.dumps(json_object, indent=2)

			self.view.replace(edit, region, json_formatted)