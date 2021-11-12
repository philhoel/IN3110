import flask
from flask_wtf import form
from flask import request
import data
import fitting
import visualize

app = flask.Flask(__name__)

df_t, df_v = data.setup('diabetes.csv')
catagory_list = [i for i in df_t]
catagory_list = catagory_list[:-1]

def get_plot(file, x, y):

    """
    Gets plot and saves the picture

    Parameters:
        file - file to be used
        x - x-axis
        y - y-axis
    """

    score = visualize(file, [x, y])
    plt.save_fig('plot.png')

    return score

def get_score(file, array, algo, n):

    """
    Gets the score. When using fitting.fit() if more than two values
    are choosen, will use this function instead to only get accuracy score
    """

    train, vali = data.setup(file)
    clf, score = fitting.fit(train, vali, array, algorithm=algo, n=n)
    return score


documentation = \
    {
        'setup': data.setup.__doc__,
        'plot': data.plot.__doc__,
        'fit': fitting.fit.__doc__,
        'visualization': visualize.visualization.__doc__,
        'get_plot': get_plot.__doc__,
        'get_score': get_score.__doc__
    }
    

@app.route("/")
@app.route("/plot_page")
def plot_page():

    """
    Creates plot page
    """

    """
    #Attempt to get plot on website
    score = False
    arguments = request.form.get_list('catagory')
    plot_button = request.form['Plot']
    if plot_button:
        if len(arguments) == 2:
            score = get_plot('diabetes.csv', arguments[0], arguments[1])
        elif len(arguments) > 2:
            score = get_score('diabetes.csv', arguments, algo='knn', n=1)

    """

    return flask.render_template('plot_page.html', posts=catagory_list)

@app.route("/help")
def help():
    """
    Creates help page
    """
    return flask.render_template('help_page.html', posts=documentation)


if __name__ == "__main__":
    app.run(debug=True)