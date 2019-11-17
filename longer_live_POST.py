from flask import Flask, request #import main Flask class and request object

app = Flask(__name__) #create the Flask app

dic_rest_bpm={"10":69,"11":59,"ideal":50,"sport":39}# used in get_my_bpm_value

@app.route('/my-extra-time', methods=['POST'])
def my_extra_time():
    req_data = request.get_json()#get jsaon object and store in dcitionary req_date

    my_bpm = req_data['my_bpm']
    var_age = req_data['var_age']


    if var_age > 10: #simple match the input age for the dictionary key and as input for get_my_bpm_value
        var_age=11
    else:
        var_age=10

    def get_my_bpm_value(val): #definition to get the value of the rest_bpm matching to the age
        for key, value in dic_rest_bpm.items():
             if val == int(key):
                 return value
        return "key doesn't exist"

    my_optimal_bpm=get_my_bpm_value(var_age)

    bpm_to_gain=(my_bpm - my_optimal_bpm)
    # ideal_bpm=dic_rest_bpm.get("ideal")
    # sport_bpm=dic_rest_bpm.get("sport")

    def give_bpm_roi(x):#number of heartbeats you receive when lowering current bpm with 1.
        var_hour=x*(60)
        return (var_hour)

    roi_mine=give_bpm_roi(bpm_to_gain)

    return '''
           Your rest bpm is {}
           For your age the optimal bpm in rest is {}
           The beats per minute you win with your optimal {} are {} heartbeats per hour'''.format(my_bpm, my_optimal_bpm, bpm_to_gain, roi_mine)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
