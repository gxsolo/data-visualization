import requests

from operator import itemgetter

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make the API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Process information about each submission.
submission_ids = r.json()
submission_dicts, titles = [], []
for submission_id in submission_ids[:30]:
	# Make a separate API call for each submission.
	url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
	submission_r = requests.get(url)
	print(submission_r.status_code)
	response_dict = submission_r.json()

	title = response_dict['title']


	submission_dict = {
		'value': response_dict.get('descendants', 0),
		'label': response_dict['title'],
		'xlink': 'https://hacker-news.firebaseio.com/item?id=' + str(submission_id)
	}
	titles.append(title)
	submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('value'), reverse=True)


# Make the visualization.
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_level = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-commented submissions on Hacker News'
chart.x_labels = titles

chart.add('', submission_dicts)
chart.render_to_file('hn_submissions.svg')