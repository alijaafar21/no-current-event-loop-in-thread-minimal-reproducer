import modal
import asyncio, nest_asyncio

# try:
#     asyncio.get_event_loop()
#     nest_asyncio.apply()
# except RuntimeError:
#     pass

query_mistral_7b_instruct_v0p2 = modal.Function.lookup(app_name='philosophy-question-answerer', tag='query_mistral_7b_instruct_v0p2')
response = query_mistral_7b_instruct_v0p2.remote('Is there such thing as a private language?')