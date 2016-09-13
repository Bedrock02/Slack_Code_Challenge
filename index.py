from flask import render_template
from flask import request
from flask import Flask
from collections import defaultdict
import urllib, re
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
  query = request.args.get('query')
  url_to_fetch = str(query) if query else None

  # If there is nothing to fetch then don't do anything
  if not url_to_fetch:
    return render_template('index.html', site_content='No Site Searched', tag_counts={})
  try:
    f = urllib.urlopen(url_to_fetch)
  except(IOError):
    return render_template('index.html', site_content="Please use another site", tag_counts={})

  html_content = f.read()
  html_content = html_content.decode('utf-8', "ignore")
  
  #clear out the contents for search and count tags
  html_contents = html_content.replace("\t", "")
  tag_count = defaultdict(int)
  for content in html_contents.splitlines():
    match = re.search('<[a-z]+', content)
    tag = match.group(0)[1:] if match else None
    if tag:
      tag_count[tag] += 1
  return render_template('index.html', site_content=html_content, tag_counts=tag_count, query=query)

if __name__ == "__main__":
  app.run()

