#!/bin/env python
'''
Json Comparator
'''

import json
import sys
import types
import os

TYPE = 'TYPE'
PATH = 'PATH'
VALUE = 'VALUE'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Diff(object):
  def __init__(self, first, second, with_values=False):
    self.difference = []
    self.seen = []
    not_with_values = not with_values
    self.check(first, second, with_values=with_values)

  def check(self, first, second, path='', with_values=False):
    if with_values and second != None:
      if not isinstance(first, type(second)):
        message = '%s - %s, %s' % (path, type(first).__name__, type(second).__name__)
    #    self.save_diff(message, TYPE)

    if isinstance(first, dict):
      for key in first:
        # the first part of path must not have trailing dot.
        if len(path) == 0:
          new_path = key
        else:
          new_path = "%s.%s" % (path, key)

        if isinstance(second, dict):
          if second.has_key(key):
            sec = second[key]
          else:
            #  there are key in the first, that is not presented in the second
  #            self.save_diff(new_path, PATH)

            # prevent further values checking.
            sec = None

          # recursive call
          if sec != None:
            self.check(first[key], sec, path=new_path, with_values=with_values)
        else:
          # second is not dict. every key from first goes to the difference
  #          self.save_diff(new_path, PATH)
          self.check(first[key], second, path=new_path, with_values=with_values)

    # if object is list, loop over it and check.
    elif isinstance(first, list):
      for (index, item) in enumerate(first):
        new_path = "%s[%s]" % (path, index)
        # try to get the same index from second
        sec = None
        if second != None:
          try:
            sec = second[index]
          except (IndexError, KeyError):
            # goes to difference
              return

        # recursive call
        self.check(first[index], sec, path=new_path, with_values=with_values)

    # not list, not dict. check for equality (only if with_values is True) and return.
    else:
      if with_values and second != None:
        if first != second and ((type(second) is int) or (type(second) is float)) and ((type(first) is int) or (type(first) is float)) :
          self.save_diff('%s - %s | %s' % (path, first, second), VALUE)
      return

  def save_diff(self, diff_message, type_):
    if diff_message not in self.difference:
      self.seen.append(diff_message)
      self.difference.append((type_, diff_message))

def compare(json1,json2):
  with open(json1,'r') as output_file1:
    json1=json.load(output_file1)
  with open(json2,'r') as output_file2:
    json2=json.load(output_file2)
  diff1 = Diff(json1, json2, True).difference
  diff2 = Diff(json2, json1, False).difference
  diffs = []
  for type, message in diff1:
    newType = 'CHANGED'
    if type == PATH:
      newType = 'REMOVED'
    diffs.append({'type': newType, 'message': message})
  for type, message in diff2:
    diffs.append({'type': 'ADDED', 'message': message})
  return diffs

if __name__ == '__main__':
  print("Please enter file locations")
  while True:
    output1=raw_input("Json File1 Location >").strip()
    if not os.path.exists(output1):
      print bcolors.FAIL+"'{}' File not found. Please enter correct path".format(output1)+bcolors.ENDC
      continue
    output2=raw_input("Json File2 Location >").strip()
    if not os.path.exists(output2):
      print bcolors.FAIL+"'{}' File not found. Please enter correct path".format(output1)+bcolors.ENDC
      continue
    break
  diffs = compare(output1,output2)
  if len(diffs) > 0:
    print "\n"+bcolors.BOLD+bcolors.HEADER+"***********Found differences between FILE1 and FILE2***********"+bcolors.ENDC
  for diff in diffs:
    print "\n"+bcolors.FAIL+diff['type']+ ': ' +bcolors.ENDC+diff['message']
