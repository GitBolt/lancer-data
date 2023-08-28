def combine_dictionaries(dict1, dict2):

  new_dict = dict1.copy()
  for key, value in dict2.items():
    if key in new_dict:
      new_dict[key]["additions"] += value["additions"]
      new_dict[key]["deletions"] += value["deletions"]
    else:
      new_dict[key] = value
  return new_dict