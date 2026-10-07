from app.database import Base, engine, SessionLocal
from app.crud import (
    inserir_tutor,
    inserir_animal,
    inserir_atendimento
)

# Cria todas as tabelas
Base.metadata.create_all(bind=engine)

# Cria a sessão
db = SessionLocal()

try:

    # =========================
    # TUTORES
    # =========================

    tutor1 = inserir_tutor(
        db,
        "Beatriz Riquelme",
        "61986613445",
        "ily.beatriz015@gmail.com"
    )

    print(
        f"Tutor inserido: "
        
        f"{tutor1.nome_completo} "
        f"(id={tutor1.id})"
    )

    tutor2 = inserir_tutor(
        db,
        "Sarah Vitoria",
        "61965684374",
        "sarahvitoriaffranca@gmail.com"
    )

    print(
        f"Tutor inserido: "
        f"{tutor2.nome_completo} "
        f"(id={tutor2.id})"
    )

    # =========================
    # ANIMAIS
    # =========================

    animal1 = inserir_animal(
        db,
        "Lua",
        "gato",
        "Persa",
        4.5,
        tutor1.id
    )

    print(
        f"Animal inserido: "
        f"{animal1.nome_animal} - "
        f"{animal1.especie}"
    )

    animal2 = inserir_animal(
        db,
        "Thor",
        "cão",
        "Pinscher",
        25.3,
        tutor1.id
    )

    print(
        f"Animal inserido: "
        f"{animal2.nome_animal} - "
        f"{animal2.especie}"
    )

    animal3 = inserir_animal(
        db,
        "Sol",
        "ave",
        "Calopsita",
        0.09,
        tutor2.id
    )

    print(
        f"Animal inserido: "
        f"{animal3.nome_animal} - "
        f"{animal3.especie}"
    )

    # =========================
    # ATENDIMENTOS
    # =========================

    atend1 = inserir_atendimento(
        db,
        "07/10/2026",
        "Vacina anual",
        120.00,
        animal1.id
    )

    print(
        f"Atendimento: "
        f"{atend1.motivo} | "
        f"R$ {atend1.valor_cons:.2f}"
    )

    atend2 = inserir_atendimento(
        db,
        "07/10/2026",
        "Consulta de rotina",
        90.00,
        animal2.id
    )

    print(
        f"Atendimento: "
        f"{atend2.motivo} | "
        f"R$ {atend2.valor_cons:.2f}"
    )

    atend3 = inserir_atendimento(
        db,
        "07/10/2026",
        "Corte de unhas",
        75.50,
        animal3.id
    )

    print(
        f"Atendimento: "
        f"{atend3.motivo} | "
        f"R$ {atend3.valor_cons:.2f}"
    )

finally:
    db.close()