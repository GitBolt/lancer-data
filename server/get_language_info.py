
def lang_to_ext(extension):
  programming_languages = {
      "ts": "typescript",
      "js": "javascript",
      "css": "css",
      "html": "html",
      "py": "python",
      "rb": "ruby",
      "go": "golang",
      "java": "java",
      "rs": "rust",
      "sol": "solidity",
      "cs": "csharp",
      "c": "c",
      "cpp": "cpp",
      "h": "cpp",
      "json": "json",
  }

  return programming_languages.get(extension, None)

def get_language_breakdown(commit_data):
  languages_used = {}
  for file in commit_data["files"]:
      _filename, extension = file["filename"].rsplit(".", 1)

      language = lang_to_ext(extension)
      if language is None:
        continue
      
      if languages_used.get(language):
        additions = file["additions"] + languages_used[language]["additions"]
        deletions = file["deletions"] + languages_used[language]["deletions"]
      else:
        additions = file["additions"]
        deletions= file["deletions"]

      languages_used[language] = {"additions": additions, "deletions": deletions}

  return languages_used