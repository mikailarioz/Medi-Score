def AirOxy(airoxy):
    if airoxy.lower() == "yes" or airoxy.lower() == "true":
        return 2

def Consciousness(consciousness):
    if consciousness.lower() == "no" or consciousness.lower() == "false":
        return 3

def Respiration(respiration):
    if 12 <= respiration <= 20:
        return  0
    elif 21 <= respiration <= 24:
        return 2
    elif 9 <= respiration <= 11:
        return 1
    else:
        return 3

def OxySat(oxysat):
    if 88 <= oxysat <= 92 or (oxysat >= 93 and airoxy == "no"):
        return 0
    elif 86 <= oxysat <= 87 or (93 <= oxysat <= 94 and airoxy == "yes"):
        return 1
    elif 84 <= oxysat <= 85 or (95 <= oxysat <= 96 and airoxy == "yes"):
        return 2
    else:
        return 3
def Temperature(temperature):
    if 36.1 <= temperature <= 38.0:
        return 0
    elif 35.1 <= temperature <= 36.0 or 38.1 <= temperature <= 39.0:
        return 1
    elif temperature >= 39.1:
        return 2
    else:
        return 3

def CBG_score(fasting, cbg_score):
    if fasting == "false":
        if 4.0 <= cbg_score <= 5.4:
            return  0
        elif 3.5 <= cbg_score <= 3.9 or 5.5 <= cbg_score <= 5.9:
            return 2
        else:
            return 3
    else:
        if 5.9 <= cbg_score <= 7.8:
            return  0
        elif 4.5 <= cbg_score <= 5.8 or 7.9 <= cbg_score <= 8.9:
            return 2
        else:
            return 3

def check_none(value):
    if value is None:
        return 0
    else:
        return value

def get_last_result(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1].strip()
            return last_line
        else:
            return None



airoxy = input("Does the patient require supplemental oxygen? ").lower()
consciousness = input("Is the patient conscious? ").lower()
respiration = int(input("What is the respiration rate of the patient? "))
oxysat = int(input("What is the patient's Oxygen saturation? ").lower())
temperature = float(input("What is the temperature of the patient? "))
fasting = input("Has it been more than 2 hours after the patient is eaten?").lower()
cbg_score = float(input("What is the patient's CBG level? "))

medi_score = check_none(AirOxy(airoxy)) + check_none(Consciousness(consciousness)) + check_none(Respiration(respiration)) + check_none(OxySat(oxysat)) + check_none(Temperature(temperature) + check_none(CBG_score(fasting, cbg_score)))


print("The patient's recent medi score is " + str(medi_score))

file_path = "test_results.txt"


if medi_score >= (int(get_last_result(file_path))+2):
    print("Patient's medi score went up by more than 2!")

with open(file_path, "a") as file:
    file.write("\n" + str(medi_score))

