# soil_model_wrapper.py

def classify_soil_threshold(params):
    thresholds_dict = {
        'pH': {'optimal':(6,7.5), 'stable':(5.5,8), 'alert':(5,8.5), 'warning':(4.5,9)},
        'moisture': {'optimal':(30,50), 'stable':(20,60), 'alert':(10,70), 'warning':(5,80)},
        'salinity': {'optimal':(0,1), 'stable':(1,1.5), 'alert':(1.5,2), 'warning':(2,3)},
        'temperature': {'optimal':(20,30), 'stable':(15,35), 'alert':(10,40), 'warning':(5,45)},
        'N': {'optimal':(20,40), 'stable':(15,50), 'alert':(10,60), 'warning':(5,70)},
        'P': {'optimal':(15,30), 'stable':(10,35), 'alert':(5,40), 'warning':(2,45)},
        'K': {'optimal':(100,200), 'stable':(80,220), 'alert':(60,240), 'warning':(40,260)}
    }

    total_score = 0
    for key in params:
        value = params[key]
        t = thresholds_dict[key]
        if t['optimal'][0] <= value <= t['optimal'][1]:
            score = 0
        elif t['stable'][0] <= value <= t['stable'][1]:
            score = 1
        elif t['alert'][0] <= value <= t['alert'][1]:
            score = 2
        elif t['warning'][0] <= value <= t['warning'][1]:
            score = 3
        else:
            score = 4
        total_score += score

    if total_score <= 3:
        return "Optimal"
    elif total_score <= 7:
        return "Stable"
    elif total_score <= 12:
        return "Alert"
    elif total_score <= 17:
        return "Warning"
    else:
        return "Critical"


class SoilClassifierWithThreshold:
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def predict(self, X):
        final_preds = []
        for i, row in X.iterrows():
            params = row.to_dict()
            threshold_pred = classify_soil_threshold(params)
            final_preds.append(threshold_pred)
        return final_preds
