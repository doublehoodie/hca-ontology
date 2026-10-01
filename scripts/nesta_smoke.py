from ojd_daps_skills.extract_skills.extract_skills import SkillsExtractor
sm = SkillsExtractor(taxonomy_name="esco")
out = sm.extract_skills(["The job involves Python programming and SQL database design."])
doc = out[0]
print("SPANS:", doc._.skill_spans)
print("MAPPED:", doc._.mapped_skills)
from ojd_daps_skills.extract_skills.extract_skills import SkillsExtractor
sm = SkillsExtractor(taxonomy_name="esco")
print([m for m in dir(sm) if not m.startswith("_")])
import inspect
from ojd_daps_skills.extract_skills.extract_skills import SkillsExtractor

sm = SkillsExtractor(taxonomy_name="esco")
text = ["The job involves Python programming and SQL database design."]

print(inspect.getsource(sm.extract_skills))
print("map_skills signature:", inspect.signature(sm.map_skills))

docs = sm.get_skills(text)
mapped = sm.map_skills(docs)
print("TYPE:", type(mapped))
print("RESULT:", mapped)
for d in (mapped if isinstance(mapped, list) else [mapped]):
    try:
        print("SPANS:", d._.skill_spans, "| MAPPED:", d._.mapped_skills)
    except AttributeError:
        pass