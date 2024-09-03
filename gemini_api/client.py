import google.generativeai as genai

def get_car_ai_bio(model, brand, year):
    prompt = '''Escreva uma descrição de venda para o veiculo {} {} {} em apenas 250 caracteres. Fale coisas especificas desse modelo.'''
    prompt = prompt.format(brand, model, year)
    genai.configure(api_key='AIzaSyCKD8Ez5g_JYzfwT2i_BMM2LLQrZy-e_FI')
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text