from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect, url_for
app = Flask(__name__)

startimages = ["/static/pina-colada1.jpg", "/static/martini1.jpg", "/static/whiskey-sour1.jpg", "/static/mojito1.jpg"]

data = {
    "1":{
        "drinkname":"Pina Colada",
        "drink_id":"1",
        "images":["/static/pina-colada1.jpg"],
        # "images":["/static/pina-colada1.jpg", "/static/pina-colada2.jpg", "/static/pina-colada3.jpg", "/static/pina-colada4.jpg"],
        "ingredients":[
            {"name":"unsweetened pineapple juice", "amount":"1.5", "unit":"oz", "image":"/static/pineapple-juice.jpg"},
            {"name":"cream of coconut", "amount":"1.5", "unit":"oz", "image":"/static/cream-of-coconut.jpg"},
            {"name":"crushed ice", "amount":"1", "unit":"cup", "image":"/static/crushed-ice.jpg"},
            {"name":"light rum", "amount":"1.5", "unit":"oz","image":"/static/light-rum.jpg"},
            {"name":"pineapple wedge", "amount":"1", "unit":"piece", "image":"/static/pineapple-wedge.jpg"}],
        "steps":{
            "1":"In a <b>2-qt. pitcher</b>, <b>combine</b> pineapple juice, cream of coconut and rum.",
            "2":"<b>Refrigerate</b>, covered, until <b>chilled</b>.",
            "3":"For each serving, add a generous cup of <b>rum mixture</b> and 1 cup ice to a <b>blender</b>.",
            "4":"Process, covered, until <b>smooth</b>.",
            "5":"<b>Pour</b> into a <b>chilled hurricane</b> or <b>highball glass</b>.",
            "6":"Cut a 1-in. slit into tip of a pineapple wedge; <b>slide wedge</b> over rim of glass"},
        "fact":"The first known reference to the <b>Pina Colada</b> was in the 19th century, when Puerto Rican pirate Roberto Cofresí gave his crew  a beverage that contained coconut, pineapple and white rum, to boost their morale.",
    },
    "2":{
        "drinkname":"Martini",
        "drink_id":"2",
        "images":[ "/static/martini2.jpg"],
        # "images":["/static/martini1.jpg", "/static/martini2.jpg", "/static/martini3.jpg"],
        "ingredients":[
            {"name":"old tom gin", "amount":"1", "unit":"oz", "image":"/static/gin.jpg"},
            {"name":"dry vermouth", "amount":"0.5", "unit":"oz", "image":"/static/vermouth.jpg"},
            {"name":"ice cubes", "amount":"1", "unit":"cup", "image":"/static/crushed-ice.jpg"},
            {"name":"pimiento-stuffed olives", "amount":"2", "unit":"pieces","image":"/static/olives.jpg"}],
        "steps":{
            "1":"Fill a <b>shaker</b> three-fourths full with ice",
            "2":"Add <b>gin</b> and <b>vermouth</b>",
            "3":"<b>Cover and shake</b> until condensation forms on outside of shaker",
            "4":"Strain into a <b>chilled cocktail glass</b>",
            "5":"<b>Garnish</b> with olives",},
        "fact":"During Prohibition in the United States, during the mid-20th century, the relative ease of illegal gin manufacture led to the <b>martini's</b> rise as the locally predominant cocktail.",
    },
    "3":{
        "drinkname":"Whiskey Sour",
        "drink_id":"3",
        "images":["/static/whiskey-sour1.jpg"],
        # "images":["/static/whiskey-sour1.jpg", "/static/whiskey-sour2.jpg", "/static/whiskey-sour3.jpg", "/static/whiskey-sour4.jpg"],
        "ingredients":[
            {"name":"whiskey", "amount":"2", "unit":"oz", "image":"/static/whiskey.jpg"},
            {"name":"sour mix", "amount":"1.5", "unit":"oz", "image":"/static/sour-mix.jpg"},
            {"name":"ice cubes", "amount":"1", "unit":"cup", "image":"/static/crushed-ice.jpg"},
            {"name":"orange wedge", "amount":"1", "unit":"piece","image":"/static/orange.jpg"},
            {"name":"maraschino cherry", "amount":"1", "unit":"piece","image":"/static/cherry.jpg"}],
        "steps":{
            "1":"Fill a <b>shaker</b> three-fourths full with ice",
            "2":"Add <b>whiskey</b> and sour mix",
            "3":"<b>Cover and shake</b> until condensation forms on outside of shaker",
            "4":"Strain into a <b>chilled wine</b> or <b>sour glass</b>",
            "5":"<b>Garnish</b> with orange wedge and cherry",},
        "fact":"The oldest historical mention of a <b>whiskey sour</b> was published in the Wisconsin newspaper, Waukesha Plain Dealer, in 1870.",
    },
    "4":{
        "drinkname":"Mojito",
        "drink_id":"4",
        "images":["/static/mojito3.jpg"],
        # "images":["/static/mojito1.jpg", "/static/mojito2.jpg", "/static/mojito3.jpg", "/static/mojito4.jpg"],
        "ingredients":[
            {"name":"club soda", "amount":"0.5", "unit":"cup", "image":"/static/club-soda.jpg"},
            {"name":"sugar", "amount":"2", "unit":"teaspoons", "image":"/static/sugar.jpg"},
            {"name":"ice cubes", "amount":"1", "unit":"cup", "image":"/static/crushed-ice.jpg"},
            {"name":"light rum", "amount":"0.25", "unit":"cup","image":"/static/light-rum.jpg"},
            {"name":"mint sprig", "amount":"3", "unit":"pieces","image":"/static/mint.jpg"},
            {"name":"lime wedge", "amount":"3", "unit":"pieces","image":"/static/lime.jpg"}],
        "steps":{
            "1":"<b>Squeeze</b> 2 lime wedges into a highball glass and then <b>drop</b> the lime into the glass.",
            "2":"Add the <b>sugar and muddle</b>.",
            "3":"Add ice. Then gently <b>press</b> 2 mint sprigs or slap mint and add to glass.",
            "4":"Pour <b>rum and club soda</b> into glass; stir",
            "5":"<b>Garnish</b> with last lime wedge and last mint sprig",},
        "fact":"Havana, Cuba, is the birthplace of the <b>mojito</b>. Some historians contend that African slaves who worked in the Cuban sugar cane fields during the 19th century were instrumental in the cocktail's origin. "
    }
}

glasses_data = {
    "1":{
        "glasses_id":"1",
        "glasses_data":[
            {"name":"Hurricane glass", "image":"/static/hurricaineglass.jpg"},
            {"name":"Highball glass", "image":"/static/highballglass.jpg"},
            {"name":"Collins glass", "image":"/static/collinsglass.jpg"},
            {"name":"Sour glass", "image":"/static/sourglass.jpg"}]},
    "2":{
        "glasses_id":"2",
        "glasses_data":[
            {"name":"Martini glass", "image":"/static/martiniglass.jpg"},
            {"name":"Margarita glass", "image":"/static/margaritaglass.jpg"},
            {"name":"Coupe", "image":"/static/coupe.jpg"},
            {"name":"Rocks glass", "image":"/static/rocksglass.jpg"}]},
}


quiz_data = {
    "1":{
        "name":"pina colada",
        "drink_id":"1",
        "max_scores":[5,6,5],
        "user_scores":[0,0,0]
    },
    "2":{
        "name":"martini",
        "drink_id":"2",
        "max_scores":[5,6,5],
        "user_scores":[0,0,0]
    },
    "3":{
        "name":"whiskey sour",
        "drink_id":"3",
        "max_scores":[5,6,5],
        "user_scores":[0,0,0]
    },
    "4":{
        "name":"mojito",
        "drink_id":"4",
        "max_scores":[5,6,5],
        "user_scores":[0,0,0]
    },
    "5":{
        "name":"quiz all drinks",
        "drink_id":"5",
        "scores":{
            "1":{
                "drinkname":"pina_colada",
                "max_scores":[5,6,5],
                "user_scores":[0,0,0]
            },
            "2":{
                "drinkname":"martini",
                "max_scores":[5,5,5],
                "user_scores":[0,0,0]
            },
            "3":{
                "drinkname":"whiskey sour",
                "max_scores":[5,5,5],
                "user_scores":[0,0,0]
            },
            "4":{
                "drinkname":"mojito",
                "max_scores":[5,5,5],
                "user_scores":[0,0,0]
            }
        }
    }
} # end quiz data

@app.route('/')
def welcome():
    return render_template('home.html', data=startimages)

@app.route('/quiz')
def MainQuiz():
   return render_template('mainquiz.html')

@app.route('/learnstart/<id>')
def LearnStart(id=None):
    drink = data[id]
    return render_template('learnstart.html', data=drink)

@app.route('/learnsteps/<id>')
def LearnSteps(id=None):
    drink = data[id]
    return render_template('learnsteps.html', data=drink)

@app.route('/learningredients/<id>')
def LearnIngredients(id=None):
    drink = data[id]
    return render_template('learningredients.html', data=drink)

@app.route('/learnglasses/<id>')
def LearnGlasses(id=None):
    glasses = glasses_data[id]
    return render_template('learnglasses.html', data=glasses)

pageEnteredTime = []
@app.route('/time', methods=['GET', 'POST'])
def addTime():
    global currentid
    json_data = request.get_json()
    pageEnteredTime.append(json_data)
    return jsonify(pageEnteredTime)

@app.route('/quizstep/<id>')
def QuizStep(id=None):
   drink = data[id]
   return render_template('quiz_step.html', data=drink)

@app.route('/quiz_ingredients/<id>')
def QuizIngredients(id=None):
   #drink = data[id]
   return render_template('question1.html', drink_data=data, drink_id=id)

@app.route('/quiz_quantity/<id>')
def QuizQuantity(id=None):
   drink = data[id]
   return render_template('question2.html', data=drink)


q1_score=0
q1_score_max=0
q1_ans = []
@app.route('/record_q1', methods=['GET', 'POST'])
def add_q1_score():
    global q1_score
    global q1_score_max
    global q1_ans
    json_data = request.get_json()
    q1_score = json_data[0]
    q1_score_max = json_data[1]
    q1_ans = json_data[2]
    print("server q1_score:", q1_score)
    print("server q1_score_max:", q1_score_max)
    print("server q1_ans:", q1_ans)
    return jsonify([q1_score,q1_score_max])


q2_score=0
q2_score_max=0
q2_ans = []
@app.route('/record_q2', methods=['GET', 'POST'])
def add_q2_score():
    global q2_score
    global q2_score_max
    global q2_ans
    json_data = request.get_json()
    q2_score = json_data[0]
    q2_score_max = json_data[1]
    q2_ans = json_data[2]
    print("server q2_score:", q2_score)
    print("server q2_score_max:", q2_score_max)
    print("server q2_ans:", q2_ans)
    return jsonify([q2_score,q2_score_max])


q3_score=0
q3_score_max=0
@app.route('/record_q3', methods=['GET', 'POST'])
def add_q3_score():
    json_data = request.get_json()
    global q3_score
    global q3_score_max
    q3_score = json_data[0]
    q3_score_max = json_data[1]
    print("server q3_score:", q3_score)
    print("server q3_score_max:", q3_score_max)
    return jsonify([q3_score,q3_score_max])

next=[]
@app.route('/quizscore/<id>')
def QuizScore(id=None):
   drink = data[id]
   print("server q3_score:", q3_score)
   print("server q3_score_max:", q3_score_max)
   scores=[q1_score,q1_score_max,q2_score,q2_score_max,q3_score,q3_score_max]
   next=[0,2,3,4,1]
   return render_template('quiz_score.html', data=drink, scores=scores,next=next)


if __name__ == '__main__':
   app.run(debug = True)
