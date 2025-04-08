from fpdf import FPDF

# Criação do documento PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Definir título
pdf.set_font("Arial", size=16, style='B')
pdf.cell(200, 10, "Resumo e Conselhos para Superar a Situação", ln=True, align='C')

# Resumo da conversa
pdf.ln(10)
pdf.set_font("Arial", size=12)
texto_resumo = (
    "Após uma experiência frustrante em um relacionamento que parecia promissor, o jovem está enfrentando "
    "uma grande tristeza e se isolando emocionalmente. Ele guardou presentes e uma aliança, sinais de que "
    "a dor da situação ainda está muito presente. Nesse processo, ele perdeu a vontade de casar, o que antes "
    "era um objetivo importante para ele. Optou por evitar distrações, como filmes e séries, e se focou em "
    "trabalho e estudos para não enfrentar a dor de forma direta. É necessário ajudá-lo a compreender que esse "
    "momento de dor é transitório e que a proximidade com Deus e a reflexão podem proporcionar cura."
)
pdf.multi_cell(0, 10, texto_resumo)

# Conselhos para ele
pdf.ln(10)
pdf.set_font("Arial", size=14, style='B')
pdf.cell(200, 10, "Conselhos para Superar a Situação", ln=True, align='L')
pdf.set_font("Arial", size=12)
conselhos = [
    "1. Permita-se sentir a dor. Não há problema em passar por esse processo, ele é natural.",
    "2. Evite se isolar ainda mais. Buscar apoio, mesmo que de forma simples, pode ser útil.",
    "3. Lembre-se de que a vontade de Deus é sempre o melhor para sua vida, mesmo quando é difícil entender.",
    "4. Não se precipite em buscar outro relacionamento. Concentre-se em sua recuperação emocional.",
    "5. Aproximar-se mais de Deus por meio da oração, leitura da Bíblia e reflexão pode ser fundamental nesse processo.",
    "6. Use a dor como uma oportunidade para crescer e entender mais sobre você mesmo e sobre o propósito divino para sua vida."
]

for item in conselhos:
    pdf.multi_cell(0, 10, item)

# Regras para seguir sem questionar
pdf.ln(10)
pdf.set_font("Arial", size=14, style='B')
pdf.cell(200, 10, "Regras para Seguir Sem Questionar", ln=True, align='L')
pdf.set_font("Arial", size=12)
regras = [
    "1. Não se afaste mais de pessoas, busque ao menos um apoio emocional.",
    "2. Não inicie outro relacionamento até que tenha superado esta dor e esteja em paz consigo mesmo.",
    "3. Ore todos os dias, mesmo que seja apenas para expressar seus sentimentos para Deus.",
    "4. Não use filmes ou séries como uma forma de evitar confrontar seus sentimentos. Enfrente-os com coragem.",
    "5. Acredite que o tempo vai trazer cura, e Deus tem algo melhor preparado para o seu futuro.",
    "6. Não se apresse para tomar decisões importantes enquanto ainda estiver no processo de cura emocional."
]

for item in regras:
    pdf.multi_cell(0, 10, item)

# Salvar o arquivo PDF
pdf_output_path = "Conselhos_e_Regras.pdf"
pdf.output(pdf_output_path)

print("PDF gerado com sucesso! O arquivo foi salvo como 'Conselhos_e_Regras.pdf'.")
