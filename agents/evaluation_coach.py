from .common import create
from .behavioral_evaluator import PROMPT as EVALUATION_PROMPT
ROLE='Evaluation & Coaching Agent'
GOAL='Produce concise evidence-based ratings and useful feedback in one request'
PROMPT=EVALUATION_PROMPT.replace('Return evidence for EVERY learner turn:', 'Review the entire transcript, but provide evidence only for learner turns supporting your ratings:')+'''\nReturn ONE JSON object with evaluation and feedback. Put all evidence, ratings, communication_ratings, adaptation_ratings, practice_rubric_version and uncertainty under evaluation. Only the two selected persona dimensions may receive adaptation ratings. Keep quotes short and explanations concise; observation, interpretation and uncertainty can be short sentences. No separate analysis of every turn is required.
Under feedback return strengths, improvements, alternative, explanation and lesson_ids. Ground coaching in the evidence you cited. The alternative is one possible response, not an ideal script. Use only lesson IDs supplied in the snapshot. Do not calculate, announce or change overall scores: the server computes them from validated ratings. No tool calls or input bundle copies. Demo practice remains personally unscored.'''
def factory(llm,tools):return create(ROLE,GOAL,PROMPT,llm,tools)
