from crewai import Agent

industrial_iot_vibration_analyst = Agent(
    role="Industrial Iot Vibration Analyst",
    goal="Deliver high-precision autonomous Industrial Iot Vibration Analyst operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
