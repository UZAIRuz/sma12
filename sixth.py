import os
import json
import facebook
from argparse import ArgumentParser
def get_parser():
 parser = ArgumentParser()
 parser.add_argument('--page')
 return parser


def getTokenFromFile(fileName):
 with open(fileName, encoding='utf-8') as fp:
  return fp.readline()


if __name__ == '__main__':
 parser = get_parser()
 args = parser.parse_args()
 token = getTokenFromFile("my_token.txt")
 fields = [
 'id',
 'name',
 'about',
 'likes',
 'website',
 'link'
 ]
 fields = ','.join(fields)
 graph = facebook.GraphAPI(token)
 page = graph.get_object(args.page, fields=fields)
 print(json.dumps(page, indent=4))
