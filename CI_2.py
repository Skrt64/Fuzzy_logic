import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Temperature
temperature = ctrl.Antecedent(np.arange(35, 41, 0.1), 'Temperature')
# Pain Level
pain = ctrl.Antecedent(np.arange(0, 11, 1), 'Pain')
# Treatment Level
treatment = ctrl.Consequent(np.arange(0, 101, 1), 'Treatment')

temperature['low'] = fuzz.trimf(temperature.universe, [35, 35, 37])
temperature['normal'] = fuzz.trimf(temperature.universe, [36, 37, 38.5])
temperature['high'] = fuzz.trimf(temperature.universe, [37.5, 40, 40])

pain['low'] = fuzz.trimf(pain.universe, [0, 0, 3])
pain['moderate'] = fuzz.trimf(pain.universe, [2, 5, 8])
pain['high'] = fuzz.trimf(pain.universe, [7, 10, 10])

treatment['low'] = fuzz.trimf(treatment.universe, [0, 0, 50])
treatment['medium'] = fuzz.trimf(treatment.universe, [25, 50, 75])
treatment['high'] = fuzz.trimf(treatment.universe, [50, 100, 100])

rule1 = ctrl.Rule(temperature['low'] | pain['low'], treatment['low'])
rule2 = ctrl.Rule(temperature['normal'] & pain['moderate'], treatment['medium'])
rule3 = ctrl.Rule(temperature['high'] | pain['high'], treatment['high'])

treatment_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

treatment_simulation = ctrl.ControlSystemSimulation(treatment_ctrl)

while True:
    temperature_value = float(input("กรอกค่าอุณหภูมิร่างกาย (35-40): "))
    pain_value = float(input("กรอกค่าระดับความปวด (0-10): "))

    treatment_simulation.input['Temperature'] = temperature_value
    treatment_simulation.input['Pain'] = pain_value

    treatment_simulation.compute()

    print("ระดับการรักษา:", treatment_simulation.output['Treatment'])

    treatment.view(sim=treatment_simulation)

    continue_simulation = input("ทำอีกหรือไม่? (Y/N): ")
    if continue_simulation.lower() != 'y':
        break





