# import ask_sdk_core.utils as ask_utils
# from ask_sdk_core.dispatch_components import AbstractRequestHandler
# from ask_sdk_core.skill_builder import SkillBuilder
# from ask_sdk_model.ui import AskForPermissionsConsentCard

# SKILL_NAME = "Weather Skill"

# class LaunchRequestHandler(AbstractRequestHandler):
#     def can_handle(self, handler_input):
#         return ask_utils.is_request_type("LaunchRequest")(handler_input)

#     def handle(self, handler_input):
#         speak_output = (
#             f"Welcome to the {SKILL_NAME}. You can ask for the weather by saying, 'What is the weather in my city?'"
#         )
#         return handler_input.response_builder.speak(speak_output).response

# class GetWeatherIntentHandler(AbstractRequestHandler):
#     def can_handle(self, handler_input):
#         return ask_utils.is_intent_name("GetWeatherIntent")(handler_input)

#     def handle(self, handler_input):
#         request_envelope = handler_input.request_envelope
#         session_attributes = handler_input.attributes_manager.session_attributes
#         response_builder = handler_input.response_builder

#         if not ('location' in session_attributes):
#             return handler_input.response_builder.speak("I don't have your location. Please grant permission.").set_card(
#                 AskForPermissionsConsentCard(permissions=['read::alexa:device:all:address'])).response

#         location = session_attributes['location']
#         weather_info = get_weather(location)

#         speak_output = f"The current weather in your city is {weather_info}."
#         return handler_input.response_builder.speak(speak_output).response

# class AskForPermissionHandler(AbstractRequestHandler):
#     def can_handle(self, handler_input):
#         return (
#             ask_utils.is_request_type("Connections.Response")(handler_input)
#             and handler_input.request_envelope.request.name == "AskFor"
#         )

#     def handle(self, handler_input):
#         request = handler_input.request_envelope.request
#         session_attributes = handler_input.attributes_manager.session_attributes

#         if request.status == "ACCEPTED":
#             session_attributes['location'] = request.payload.location
#             return handler_input.response_builder.speak("Thank you for granting the location permission. You can now ask for the weather in your city.").response

#         return handler_input.response_builder.speak("I'm sorry, I can't provide weather information without your location.").response

# sb = SkillBuilder()

# sb.add_request_handler(LaunchRequestHandler())
# sb.add_request_handler(GetWeatherIntentHandler())
# sb.add_request_handler(AskForPermissionHandler())

# handler = sb.lambda_handler()
