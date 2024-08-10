import numpy as np
def create_train_data():
    data = [['Sunny', 'Hot', 'High', 'Weak','no'],
            ['Sunny', 'Hot', 'High', 'Strong', 'no'],
            ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
            ['Rain', 'Mild', 'High', 'Weak', 'yes'],
            ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
            ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
            ['Overcast', 'Cool', 'Normal', 'Strong', 'no'],
            ['Overcast', 'Mild', 'High', 'Weak', 'yes'],
            ['Rain', 'Mild', 'Normal', 'Weak', 'yes']]
    return np.array(data)
train_data = create_train_data()
print(train_data)
print(train_data.shape)
def compute_prior_probability(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))
    for data in train_data:
        if data[4] == "no":
            prior_probability[0] += 1
        else:
            prior_probability[1] += 1
    prior_probability = prior_probability / len(train_data)
    return prior_probability
prior_probability = compute_prior_probability(train_data)
print("P(play tennis = No)", round(prior_probability[0], 1))
print("P(play tennis = Yes)", round(prior_probability[1], 1))

def compute_conditional_probability(train_data):
    y_unique = ['no', 'yes']
    conditional_probability = []
    list_x_name = []
    for i in range (0, train_data.shape[1]-1): #find list_x_name
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)
    for i, x_values in enumerate(list_x_name):
        x_conditional_probability = {}
        for x in x_values:
            x_conditional_probability[x] = {}
            for y in y_unique:
                x_and_y_count = np.sum((train_data[:, i] == x) & (train_data[:,-1]==y))
                y_count = np.sum(train_data[:, -1] == y)
                if y_count > 0:
                    x_conditional_probability[x][y] = x_and_y_count / y_count
                else:
                    x_conditional_probability[x][y] == 0.0
        conditional_probability.append(x_conditional_probability)

    return conditional_probability, list_x_name
_, list_x_name = compute_conditional_probability(train_data)
print ("x1 =", list_x_name[0])
print ("x2 =", list_x_name[1])
print ("x3 =", list_x_name[2])
print ("x4 =", list_x_name[3])

def get_index_from_value (feature_name, list_features) :
    return np.where (list_features == feature_name)[0][0]

_, list_x_name = compute_conditional_probability(train_data)
outlook = list_x_name[0]
i1 = get_index_from_value("Overcast", outlook)
i2 = get_index_from_value("Rain", outlook)
i3 = get_index_from_value("Sunny", outlook)
print (i1 ,i2 ,i3)

conditional_probability, list_x_name = compute_conditional_probability(train_data)
#Compute P("Outlook" = "Sunny"|Play Tennis "="Yes")
x1 = "Sunny"
y1 = "yes"
outlook_conditional_prob = conditional_probability[0]  # Outlook là cột đầu tiên
prob_yes = outlook_conditional_prob[x1].get(y1, 0.0)
print("P('Outlook'='Sunny'|Play Tennis'='Yes') =", np.round(prob_yes, 2))

# Compute P(" Outlook "=" Sunny "| Play Tennis "=" No ")
y2 = "no"
prob_no = outlook_conditional_prob[x1].get(y2, 0.0)
print("P('Outlook'='Sunny'|Play Tennis'='No') =", np.round(prob_no, 2))

# Train Naive Bayes Model
def train_naive_bayes(train_data):
    # Step 1: calculate Prior Probability
    prior_probability = compute_prior_probability(train_data)
    # Step 2: Calculate Conditional Probability
    conditional_probability, list_x_name = compute_conditional_probability(train_data)
    return prior_probability, conditional_probability, list_x_name

# Prediction
def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    x1 = X[0]
    x2 = X[1]
    x3 = X[2]
    x4 = X[3]

    p0 = prior_probability[0]
    p1 = prior_probability[1]

    for x, conditional_prob, list_x in zip([x1, x2, x3, x4], conditional_probability, list_x_name):
        p0 *= conditional_prob[x].get('no', 0.0)
        p1 *= conditional_prob[x].get('yes', 0.0)

    if p0 > p1:
        y_pred = 0
    else:
        y_pred = 1

    return y_pred

# Example usage
X = ['Sunny', 'Cool', 'High', 'Strong']
data = create_train_data()
prior_probability, conditional_probability, list_x_name = train_naive_bayes(data)
pred = prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability)

if pred:
    print("Ad should go!")
else:
    print("Ad should not go!")
