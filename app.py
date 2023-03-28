import openai
from flask import Flask, request, render_template

app = Flask(__name__, template_folder="templates")

openai.api_key = 'XXXX' # Add your Api key here

def generate_prompt(title):
    return '''You are a professional story writer. You create an imaginative and unique story that engages and entertains the reader. Your stories are always coherent and well-structured, with a logical flow that leads the reader through the narrative. You have a talent for crafting characters and worlds that readers can lose themselves in, and you take pride in your ability to use language to bring your stories to life.\n\nWrite a story on the topic "{}". Your story should be at least 1000 words long and incorporate elements of character development, setting, and plot to create a compelling and memorable narrative. Remember to use descriptive language and vivid imagery to bring your story to life. You have the freedom to explore different genres and styles of storytelling to create a story that is uniquely your own. Be sure to take your time crafting a story that captures the reader's imagination and leaves a lasting impression.'''.format(str(title))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_story", methods=["POST"])
def generate_story():
    prompt = request.form["prompt"]
    prompt = generate_prompt(prompt)
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500,
        top_p=1,
        temperature=1
    )
    message = completions.choices[0].text
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(port=8080, threaded=False)
