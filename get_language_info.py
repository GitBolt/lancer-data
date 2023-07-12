
def lang_to_ext(extension):
  programming_languages = {
      "ts": "Typescript",
      "js": "JavaScript",
      "css": "CSS",
      "html": "HTML",
      "py": "Python",
      # "rb": "Ruby",
      "go": "Go",
      # "java": "Java",
      "rs": "Rust",
      "sol": "Solidity",
      # "cs": "C#",
      "c": "C",
      "cpp": "C++",
      # "h": "C++",
      # "json": "JSON",
  }

  return programming_languages.get(extension, None)

def get_language_breakdown(commit_data):
  languages_used = {}
  for file in commit_data["files"]:
      filename, extension = file["filename"].rsplit(".", 1)

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