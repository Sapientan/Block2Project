# prob_h = 0.003
# prob_pos_test = 0.9
# prob_false_pos = 0.03

prob_h = 0.1
prob_e_given_h = 0.95
prob_e_given_not_h = 0.1


print('By Bayes\' Theorem, we have ((' + str(prob_h) + ') * ' + str(prob_e_given_h) + ')/(((1-' + str(prob_h) + ')*' + str(prob_e_given_not_h) + ')+ ((' + str(prob_h) + ') * ' + str(prob_e_given_h) + '))) = ' + str(((prob_h) * prob_e_given_h)/(((1-prob_h)*prob_e_given_not_h)+ ((prob_h) * prob_e_given_h))) + ' ')