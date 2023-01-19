def latest(scores):
    return scores[-1]



def personal_best(scores):
    high_score = 0
    for score in scores:
        if score > high_score:
            high_score = score
    return high_score



def personal_top_three(scores):
    top_three = [0,0,0]
    for score in scores:
        if score >= top_three[0]:
            if top_three[0] != score:
                top_three[1]=top_three[0]
            top_three[0] = score


        elif score>=top_three[1]:
            if top_three[1] != score:

                top_three[2]=top_three[1]
            top_three[1] = score


        elif score >= top_three[2]:
            top_three[2] = score
    return top_three




    

high_score = [2,1,3,4,5,6,2,2,1,3,4,5,4,6]
