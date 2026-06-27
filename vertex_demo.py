from google import genai

PROMPT = """
Rol: Experto en computacion en la nube e inteligencia artificial generativa
Tarea: Presenta un cuadro comparativo entre modelos de servicio en la nube: IaaS, PaaS, SaaS.
- Agrega principales servicios de cada modelo disponibles en GCP.
- Lista un caso de uso practico para cada modelo.
"""

client = genai.Client(
    enterprise=True,
    project="clocus-ai-dev",
    location="global",
)

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=PROMPT
)

print(response.text)
