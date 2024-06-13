from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from Models import Answer, Question, Test

if __name__ == "__main__":
    engine = create_engine(
        "sqlite:///C:\\Users\\USER\\Desktop\\programacion\\lp-1\\test-app\\testsdb\\test.db"
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    questions = [
        Question(
            question_text="¿Cómo se define una lista?",
            answers=[
                Answer(
                    answer_text="lista=[1,2,3]",
                    is_correct=True
                ),
                Answer(
                    answer_text="lista=(1,2,3)",
                    is_correct=False
                ),
                Answer(
                    answer_text="lista={1,2,3}",
                    is_correct=False
                )
            ]
        ),
        Question(
            question_text="¿Qué tipo de dato es 'hola'?",
            answers=[
                Answer(
                    answer_text="str",
                    is_correct=True
                ),
                Answer(
                    answer_text="int",
                    is_correct=False
                ),
                Answer(
                    answer_text="float",
                    is_correct=False
                )
            ]
        ),
    ]

    test = Test(test_name="Python Basics", questions=questions)
    session.add(test)
    session.commit()