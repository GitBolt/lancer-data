
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
    "cs": "c#",
    "c": "c",
    "cpp": "cpp",
    "h": "cpp",
    "json": "json",
    "php": "php",
    "swift": "swift",
    "kt": "kotlin",
    "pl": "perl",
    "lua": "lua",
    "r": "r",
    "m": "matlab",
    "dart": "dart",
    "scala": "scala",
    "hs": "haskell",
    "groovy": "groovy",
    "m": "objective-c",
    "sh": "shell script",
    "ps1": "powershell",
    "sql": "sql",
    "ex": "elixir",
    "perl6": "perl 6",
    "tsql": "t-sql",
    "jsx": "jsx",
    "tsx": "tsx",
    "vue": "vue",
    "perl6": "perl 6",
    "sql": "sql",
    "ex": "elixir",
    "rs": "racket",
    "plsql": "pl/sql",
    "yaml": "yaml",
    "toml": "toml",
    "erl": "erlang",
    "f#": "fsharp",
    "asm": "assembly",
    "awk": "awk",
    "bash": "bash",
    "csh": "csh",
    "fish": "fish",
    "scala": "scala",
    "tsv": "tsv",
    "csv": "csv",
    "html": "xml",
    "xhtml": "xhtml",
    "rdf": "rdf",
    "turtle": "turtle",
    "perl": "perl",
    "raku": "raku",
    "yaml": "yaml",
    "jsonld": "json-ld",
    "graphql": "graphql",
    "pl6": "perl6",
    "yaml": "yaml",
    "jsonld": "json-ld",
    "graphql": "graphql",
    "lisp": "lisp",
    "scheme": "scheme",
    "cl": "common lisp",
    "rkt": "racket",
    "gvy": "groovy",
    "feature": "gherkin",
    "cmake": "cmake",
    "dockerfile": "dockerfile",
    "dockerfile": "dockerfile",
    "vb": "vb.net",
    "vb": "vb",
    "fsharp": "f#",
    "haskell": "haskell",
    "ada": "ada",
    "matlab": "matlab",
    "tcl": "tcl",
    "raku": "raku",
    "twig": "twig",
    "ada": "ada",
    "plsql": "pl/sql",
    "bash": "bash",
    "csh": "csh",
    "fish": "fish",
    "makefile": "makefile",
    "cfg": "configuration file",
    "dockerignore": "dockerignore",
    "gitignore": "gitignore",
    "hgignore": "hgignore",
    "dockerignore": "dockerignore",
    "gitignore": "gitignore",
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