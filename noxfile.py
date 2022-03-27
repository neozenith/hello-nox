import nox
SOME = [
    "2.7"
    , "3.9"
]
MOST=["2.7.18","3.6.15", "3.7.13", "3.8.12", "3.9.10", "3.10.3"]
ALL=["2.7","3.4", "3.5", "3.6", "3.7", "3.8", "3.9", "3.10"]
@nox.session(python=MOST)
def tests(session):
    session.install('pytest', '-vvv')
    session.run('pytest')
