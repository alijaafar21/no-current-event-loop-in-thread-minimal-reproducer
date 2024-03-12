import chainlit as cl
import modal
import asyncio, nest_asyncio

# try:
#     asyncio.get_event_loop()
#     nest_asyncio.apply()
# except RuntimeError:
#     pass


async def query_mistral(prompt):
    query_mistral_7b_instruct_v0p2 = modal.Function.lookup(app_name='philosophy-question-answerer',
                                                           tag='query_mistral_7b_instruct_v0p2')
    return query_mistral_7b_instruct_v0p2.remote('Is there such thing as a private language?')


@cl.on_message
async def main(message: cl.Message):
    response = await query_mistral(message)
    await cl.Message(
        content=response,
    ).send()