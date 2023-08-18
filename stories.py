"""Madlibs Stories."""

from flask import Flask, render_template, request 

app = Flask(__name__)


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text, code, title, phrase):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text
        self.title = title 
        self.template = phrase 
        self.code = code 

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    "omg",
    "An Excited Adventure",
    ["noun", "verb"],
    """OMG!! OMG!! I love to {verb} a {noun}!"""
)

stories = {s.code: s for s in [story1, story2]}




@app.route("/")
def ask_story():
    """Show list-of-stories form."""

    return render_template("select-story.html",
                           stories=stories.values())


@app.route("/questions")
def ask_questions():
    """Generate and show form to ask words."""

    story_id = request.args["story_id"]
    story = stories[story_id]

    prompts = story.prompts

    return render_template("questions.html",
                           story_id=story_id,
                           title=story.title,
                           prompts=prompts)

@app.route("/story")
def show_story():

    story_id = request.args["story_id"]
    story = stories["story_id"]
    phrase = story.generate(request.args)
    return render_template('story.html',title=story.title, phrase=phrase)


        